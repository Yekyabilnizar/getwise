/**
 * GetWise – Worker kecil untuk menerima masukan pengunjung.
 * POST /api/masukan  ->  membuat issue di repo GitHub PRIVAT milik Anda.
 * Semua halaman lain tetap disajikan langsung dari folder dist/ (aset statis).
 *
 * Pengaturan (Cloudflare → Worker getwise → Settings → Variables and secrets, bagian Runtime):
 *   GITHUB_TOKEN   (Secret)  fine-grained token, akses Issues: Read and write, hanya ke repo masukan
 *   FEEDBACK_REPO  (Text)    contoh: Yekyabilnizar/getwise-masukan   (sudah diisi di wrangler.jsonc)
 */
const JENIS = {
  saran: 'Saran / ide fitur',
  kesalahan: 'Laporan kesalahan hitung',
  kalkulator: 'Usulan kalkulator atau artikel baru',
  tampilan: 'Masalah tampilan / teknis',
  lainnya: 'Lainnya',
};
const LIMIT = { pesan: 3000, nama: 80, email: 120, halaman: 200 };

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });

// cegah mention/tautan otomatis di GitHub dan potong panjang
const clean = (s, max) => String(s == null ? '' : s).replace(/\r/g, '').replace(/@/g, '@​').replace(/[<>]/g, (c) => (c === '<' ? '&lt;' : '&gt;')).trim().slice(0, max);

async function handleMasukan(request, env) {
  if (request.method !== 'POST') return json({ ok: false, error: 'Metode tidak diizinkan.' }, 405);
  if (!env.GITHUB_TOKEN || !env.FEEDBACK_REPO) return json({ ok: false, error: 'Layanan masukan belum dikonfigurasi.' }, 503);

  // hanya terima dari situs sendiri
  const origin = request.headers.get('origin') || '';
  const host = new URL(request.url).host;
  if (origin && new URL(origin).host !== host) return json({ ok: false, error: 'Asal permintaan tidak valid.' }, 403);

  const len = +(request.headers.get('content-length') || 0);
  if (len > 20000) return json({ ok: false, error: 'Pesan terlalu panjang.' }, 413);

  let d;
  try { d = await request.json(); } catch (e) { return json({ ok: false, error: 'Format data tidak valid.' }, 400); }

  // jebakan bot: kolom tersembunyi harus kosong dan formulir tidak diisi terlalu cepat
  if (d.website) return json({ ok: true });
  if (typeof d.t === 'number' && d.t < 3000) return json({ ok: false, error: 'Terlalu cepat. Coba lagi beberapa detik lagi.' }, 429);

  const pesan = clean(d.pesan, LIMIT.pesan);
  if (pesan.length < 10) return json({ ok: false, error: 'Tulis masukan minimal 10 karakter.' }, 400);
  const jenis = JENIS[d.jenis] ? d.jenis : 'lainnya';
  const nama = clean(d.nama, LIMIT.nama);
  const email = clean(d.email, LIMIT.email);
  if (email && !/^[^\s]+@​[^\s]+\.[^\s]+$/.test(email)) return json({ ok: false, error: 'Format email tidak valid.' }, 400);
  const halaman = clean(d.halaman, LIMIT.halaman);

  const ringkas = pesan.split('\n')[0].slice(0, 60) + (pesan.length > 60 ? '…' : '');
  const waktu = new Date().toLocaleString('id-ID', { timeZone: 'Asia/Jakarta' });
  const negara = (request.cf && request.cf.country) || '-';
  const body = [
    `**Jenis:** ${JENIS[jenis]}`,
    `**Halaman terkait:** ${halaman || '-'}`,
    `**Nama:** ${nama || '-'}`,
    `**Email:** ${email ? email.replace('@​', ' [at] ') : '-'}`,
    `**Waktu:** ${waktu} WIB · **Negara:** ${negara}`,
    '',
    '---',
    '',
    pesan.split('\n').map((l) => '> ' + l).join('\n'),
  ].join('\n');

  const res = await fetch(`https://api.github.com/repos/${env.FEEDBACK_REPO}/issues`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${env.GITHUB_TOKEN}`,
      accept: 'application/vnd.github+json',
      'x-github-api-version': '2022-11-28',
      'user-agent': 'getwise-masukan',
      'content-type': 'application/json',
    },
    body: JSON.stringify({ title: `[${JENIS[jenis]}] ${ringkas}`, body }),
  });
  if (!res.ok) {
    console.log('GitHub error', res.status, (await res.text()).slice(0, 300));
    return json({ ok: false, error: 'Masukan belum bisa dikirim. Silakan coba lagi nanti.' }, 502);
  }
  return json({ ok: true });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/api/masukan') {
      try { return await handleMasukan(request, env); }
      catch (e) { console.log('error', e && e.stack); return json({ ok: false, error: 'Terjadi kesalahan. Silakan coba lagi.' }, 500); }
    }
    return env.ASSETS.fetch(request);
  },
};
