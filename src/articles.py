"""Artikel panduan GetWise: pengertian dan tips untuk setiap topik kalkulator."""
from charts import C, D, E, G, M, bars, figure, lines


def jt(v):
    s = f"{v/1e6:.1f}".replace(".", ",")
    return ("Rp" + s.replace(",0", "") + " jt") if v else "0"


def rb(v):
    return f"Rp{round(v/1000):,}".replace(",", ".") + " rb" if v else "0"


def pctf(v):
    return f"{v:.1f}%".replace(".", ",")


def _anuitas(P, r, n):
    r /= 12
    return P / n if r == 0 else P * r / (1 - (1 + r) ** -n)


def _efektif(P, cic, n):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if _anuitas(P, mid * 12, n) > cic else (mid, hi)
    return (lo + hi) / 2 * 12


BLN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]

# ---------- grafik (dihitung dengan mesin yang sama dengan kalkulator) ----------
CH_PPH = figure(bars(BLN, [("PPh 21", E, [261350, 261350, 261350, 1840860, 261350, 261350, 261350, 261350, 261350, 261350, 261350, 322840])], rb,
                     "Potongan PPh 21 per bulan", values_on_top=rb),
                "Contoh: gaji Rp10 juta, status TK/0, bonus Rp10 juta di bulan April, ikut semua program BPJS. Potongan melonjak di bulan bonus, lalu disesuaikan di Desember. Total setahun Rp4.777.200.")
CH_GAJI = figure(bars(["Gaji kotor", "Iuran BPJS", "PPh 21", "Diterima"], [("", E, [10e6, 400000, 261350, 9338650])], jt, "Dari gaji kotor ke gaji bersih",
                      values_on_top=lambda v: f"Rp{round(v):,}".replace(",", ".")),
                 "Gaji Rp10 juta (TK/0, semua program BPJS): dipotong BPJS Rp400.000 dan PPh 21 Rp261.350, sehingga yang diterima Rp9.338.650 per bulan.")
CH_BPJS = figure(bars(["Kesehatan", "JHT", "JP", "JKK", "JKM"], [("Perusahaan", E, [320000, 296000, 160000, 19200, 24000]), ("Karyawan", G, [80000, 160000, 80000, 0, 0])], rb,
                      "Iuran BPJS per program"),
                 "Iuran per bulan untuk upah Rp8 juta. Perusahaan menanggung bagian terbesar; karyawan hanya membayar Kesehatan 1%, JHT 2%, dan JP 1%.")
CH_THR = figure(bars([str(i) for i in range(1, 13)], [("THR", G, [6e6 * i / 12 for i in range(1, 13)])], jt, "THR menurut masa kerja", values_on_top=jt),
                "THR untuk upah Rp6 juta menurut masa kerja (bulan). Mulai 12 bulan, THR penuh 1 bulan upah.")
_kpr = [3671968] * 3 + [5114414] * 12
CH_KPR = figure(bars([str(i) for i in range(1, 16)], [("Cicilan per bulan", E, _kpr)], jt, "Cicilan KPR per tahun", values_on_top=lambda v: jt(v)),
                "KPR Rp480 juta (rumah Rp600 juta, DP 20%), tenor 15 tahun, bunga fixed 4,5% selama 3 tahun lalu floating 11%. Cicilan naik sekitar 39% di tahun ke-4.")
_rates = [3, 4, 5, 6, 7, 8, 9, 10]
_eff = []
for r in _rates:
    P, n = 24e6, 36
    _eff.append(_efektif(P, (P + P * r / 100 * 3) / n, n) * 100)
CH_FLAT = figure(bars([f"{r}%" for r in _rates], [("Bunga flat", G, _rates), ("Bunga efektif setara", E, _eff)], lambda v: f"{v:.0f}%", "Bunga flat dan bunga efektif"),
                 "Untuk tenor 36 bulan, bunga efektif kira-kira 1,8 kali bunga flat. Flat 6% setara efektif sekitar 11% per tahun.")
_dr = [3, 4, 5, 6]
CH_DEPO = figure(bars([f"{r}%" for r in _dr], [("Bunga kotor", M, [1e8 * r / 100 for r in _dr]), ("Bunga bersih (setelah pajak 20%)", E, [1e8 * r / 100 * .8 for r in _dr])], jt,
                      "Bunga deposito setahun"),
                 "Bunga setahun untuk deposito Rp100 juta pada beberapa tingkat suku bunga. Pajak 20% memotong seperlima hasil.")
_y = [str(i) for i in range(1, 21)]
CH_INV = figure(lines(_y, [("Imbal 10%", G, [12.5, 26.3, 41.5, 58.2, 76.6, 96.8, 119, 143.4, 170.3, 199.9, 232.4, 268.2, 307.5, 350.8, 398.4, 450.8, 508.5, 571.8, 641.6, 718.3]),
                           ("Imbal 6%", E, [12.3, 25.4, 39.2, 53.9, 69.5, 86, 103.5, 122, 141.6, 162.5, 184.5, 207.9, 232.8, 259, 286.9, 316.5, 347.8, 381, 416.1, 453.4]),
                           ("Hanya ditabung (0%)", M, [12 * i for i in range(1, 21)])],
                      lambda v: f"{v:.0f} jt", "Pertumbuhan investasi Rp1 juta per bulan", step=2),
                "Menabung Rp1 juta per bulan selama 20 tahun: total setoran Rp240 juta. Dengan imbal 6% per tahun menjadi sekitar Rp453 juta, dengan 10% sekitar Rp718 juta.")

TIP = lambda t: f'<div class="note info"><b>Tips:</b> {t}</div>'

ARTICLES = []


def A(**k):
    ARTICLES.append(k)


A(slug="apa-itu-pph-21-ter", calc="pph21", img="pph21", date="27 November 2026",
  title="Apa Itu PPh 21 dan Metode TER? Penjelasan Lengkap untuk Karyawan",
  h1="Apa Itu PPh 21 dan Metode TER?",
  desc="Pengertian PPh 21, cara kerja tarif efektif rata-rata (TER), kenapa potongan Desember berbeda, dan tips agar tidak kaget melihat slip gaji.",
  lead="PPh 21 adalah pajak yang dipotong dari gaji Anda setiap bulan. Sejak 2024 cara potongnya berubah menjadi metode TER. Berikut penjelasan sederhananya.",
  body=[
      ("Pengertian PPh 21", """<p><b>PPh Pasal 21</b> adalah pajak penghasilan atas gaji, upah, honorarium, tunjangan, dan pembayaran lain yang diterima orang pribadi karena pekerjaan. Yang unik, karyawan tidak menyetor sendiri: <b>pemberi kerja memotong</b> pajak dari gaji, menyetorkannya ke kas negara, dan melaporkannya. Di akhir tahun, perusahaan memberi bukti potong (formulir 1721-A1) yang Anda pakai untuk mengisi SPT Tahunan.</p>
<p>Besarnya pajak tidak sama untuk semua orang. Ada dua hal utama yang menentukan: <b>berapa penghasilan Anda</b> dan <b>status keluarga Anda</b> (PTKP). Semakin besar penghasilan, semakin tinggi lapisan tarifnya; semakin banyak tanggungan, semakin besar bagian penghasilan yang bebas pajak.</p>"""),
      ("PTKP: bagian penghasilan yang tidak kena pajak", """<p><b>Penghasilan Tidak Kena Pajak (PTKP)</b> adalah batas penghasilan setahun yang dibebaskan dari pajak. Besarnya Rp54 juta untuk diri sendiri, ditambah Rp4,5 juta bila sudah menikah, dan Rp4,5 juta untuk setiap tanggungan (anak atau keluarga sedarah/semenda yang ditanggung penuh), paling banyak tiga orang.</p>
<ul><li><b>TK/0</b> (lajang tanpa tanggungan): Rp54.000.000</li><li><b>K/0</b> (menikah tanpa anak): Rp58.500.000</li><li><b>K/2</b> (menikah, dua anak): Rp67.500.000</li><li><b>K/3</b> (menikah, tiga anak): Rp72.000.000</li></ul>
<p>Artinya, karyawan lajang dengan penghasilan neto setahun di bawah Rp54 juta tidak terutang PPh 21 sama sekali.</p>"""),
      ("Cara kerja metode TER", """<p>Sebelum 2024, perusahaan menghitung pajak setahun lalu membaginya per bulan, perhitungan yang cukup rumit. Lewat PP 58/2023 dan PMK 168/2023, pemerintah memperkenalkan <b>tarif efektif rata-rata (TER)</b> untuk menyederhanakannya:</p>
<ol><li><b>Januari sampai November</b>: pajak = penghasilan bruto bulan itu × tarif TER. Tarif diambil dari tabel kategori A (TK/0, TK/1, K/0), B (TK/2, TK/3, K/1, K/2), atau C (K/3), sesuai besarnya bruto bulanan.</li>
<li><b>Desember</b>: pajak setahun dihitung ulang dengan tarif progresif Pasal 17 (5%, 15%, 25%, 30%, 35%), lalu dikurangi pajak yang sudah dipotong. Sisanya menjadi potongan Desember.</li></ol>
<p>Karena TER dihitung per bulan tanpa melihat bulan lain, potongan bisa melonjak di bulan Anda menerima bonus atau THR. Lonjakan itu bukan pajak tambahan; semuanya akan &ldquo;dirapikan&rdquo; di Desember.</p>
[[CH_PPH]]"""),
      ("Komponen yang sering terlupa", """<p>Penghasilan bruto untuk menghitung TER bukan hanya gaji pokok. Premi <b>BPJS Kesehatan, JKK, dan JKM yang dibayar perusahaan</b> ikut dihitung sebagai penghasilan, walaupun tidak Anda terima tunai. Sebaliknya, iuran <b>JHT 2% dan JP 1%</b> yang Anda bayar menjadi pengurang di perhitungan Desember, bersama <b>biaya jabatan</b> 5% (maksimal Rp6 juta setahun).</p>
<p>Inilah sebabnya potongan pajak di slip gaji sering terlihat sedikit lebih besar dari perkiraan bila hanya menghitung dari gaji pokok.</p>"""),
      ("Tips agar tidak kaget dengan potongan pajak", "<ul>"
       "<li><b>Cek status PTKP di HRD.</b> Bila sudah menikah atau punya anak tetapi status di sistem masih TK/0, potongan Anda lebih besar dari seharusnya. Status yang dipakai adalah kondisi awal tahun pajak.</li>"
       "<li><b>Siapkan dana saat bonus atau THR.</b> Potongan di bulan itu bisa beberapa kali lipat bulan biasa. Anggarkan dari THR bersih, bukan THR kotor.</li>"
       "<li><b>Jangan panik melihat slip Desember.</b> Bisa lebih besar (kurang potong) atau justru lebih kecil bahkan ada pengembalian (lebih potong).</li>"
       "<li><b>Simpan bukti potong 1721-A1.</b> Dokumen ini dibutuhkan untuk lapor SPT Tahunan paling lambat 31 Maret tahun berikutnya.</li>"
       "<li><b>Pindah kerja di tengah tahun?</b> Minta bukti potong dari kantor lama dan berikan ke kantor baru atau gabungkan sendiri di SPT, agar pajak setahun dihitung benar.</li></ul>"
       + TIP("gunakan kalkulator PPh 21 untuk melihat potongan setiap bulan, termasuk bulan bonus dan Desember, sebelum menerima slip gaji.")),
  ],
  faq=[("Apakah semua karyawan kena PPh 21?", "Hanya bila penghasilan neto setahunnya melebihi PTKP. Namun perusahaan tetap wajib menghitung dan melaporkannya."),
       ("Apakah TER menambah beban pajak?", "Tidak. TER hanya cara memotong per bulan. Total pajak setahun tetap ditentukan oleh tarif Pasal 17 di masa pajak terakhir.")])

A(slug="cara-membaca-slip-gaji", calc="gaji-bersih", img="gaji-bersih", date="27 November 2026",
  title="Cara Membaca Slip Gaji: Gaji Kotor, Potongan, dan Take Home Pay",
  h1="Cara Membaca Slip Gaji dan Menghitung Take Home Pay",
  desc="Kenali komponen slip gaji: gaji pokok, tunjangan tetap dan tidak tetap, potongan BPJS, PPh 21, serta tips mengatur gaji bersih setiap bulan.",
  lead="Angka yang masuk ke rekening hampir selalu lebih kecil dari gaji di kontrak kerja. Kenali komponen slip gaji supaya Anda tahu ke mana selisihnya pergi.",
  body=[
      ("Gaji kotor dan gaji bersih", """<p><b>Gaji kotor (gross)</b> adalah total penghasilan sebelum potongan: gaji pokok ditambah semua tunjangan. <b>Gaji bersih</b> atau <b>take home pay (THP)</b> adalah uang yang benar-benar Anda terima setelah dikurangi iuran wajib dan pajak. Saat negosiasi gaji atau membandingkan tawaran kerja, pastikan Anda tahu angka yang dibicarakan itu gross atau net.</p>
[[CH_GAJI]]"""),
      ("Komponen penghasilan di slip gaji", """<ul><li><b>Gaji pokok</b>: imbalan dasar sesuai jabatan dan masa kerja.</li>
<li><b>Tunjangan tetap</b>: dibayar rutin dengan jumlah sama setiap bulan, tidak tergantung kehadiran, misalnya tunjangan jabatan atau keluarga. Gaji pokok + tunjangan tetap disebut <b>upah</b> dan menjadi dasar iuran BPJS, THR, dan pesangon.</li>
<li><b>Tunjangan tidak tetap</b>: tergantung kehadiran atau kinerja, misalnya uang makan harian, transport, lembur, dan insentif.</li>
<li><b>Penghasilan tidak rutin</b>: bonus, THR, dan rapel kenaikan gaji.</li></ul>
<p>Menurut aturan pengupahan, gaji pokok sebaiknya paling sedikit 75% dari jumlah gaji pokok dan tunjangan tetap.</p>"""),
      ("Komponen potongan", """<ul><li><b>BPJS Kesehatan 1%</b> dari upah (batas upah Rp12 juta).</li>
<li><b>JHT 2%</b> dari upah, menjadi tabungan hari tua Anda sendiri di BPJS Ketenagakerjaan.</li>
<li><b>JP 1%</b> dari upah (batas upah Rp11.086.300 mulai Maret 2026), untuk manfaat pensiun bulanan.</li>
<li><b>PPh 21</b> dengan metode TER.</li>
<li>Potongan lain sesuai kebijakan kantor: koperasi, pinjaman karyawan, iuran serikat, atau denda keterlambatan.</li></ul>
<p>Iuran JHT dan JP sebenarnya bukan &ldquo;hilang&rdquo;. Keduanya kembali kepada Anda sebagai saldo JHT dan manfaat pensiun.</p>"""),
      ("Tips mengelola gaji bersih", "<ul>"
       "<li><b>Susun anggaran dari THP rata-rata</b>, bukan gaji di kontrak. Potongan pajak Desember bisa berbeda dari bulan lain.</li>"
       "<li><b>Gunakan pola 50/30/20</b> sebagai titik awal: 50% kebutuhan, 30% keinginan, 20% tabungan dan investasi. Sesuaikan dengan kondisi Anda.</li>"
       "<li><b>Sisihkan di awal</b> (pay yourself first): atur transfer otomatis ke rekening tabungan atau investasi pada hari gajian.</li>"
       "<li><b>Bangun dana darurat</b> 3–6 kali pengeluaran bulanan sebelum mulai berinvestasi di instrumen berisiko.</li>"
       "<li><b>Periksa slip setiap bulan.</b> Kesalahan status PTKP, upah BPJS yang dilaporkan terlalu rendah, atau lembur yang belum dibayar lebih mudah diperbaiki bila cepat diketahui.</li>"
       "<li><b>Cek saldo JHT</b> melalui aplikasi resmi BPJS Ketenagakerjaan untuk memastikan iuran benar-benar disetor perusahaan.</li></ul>"
       + TIP("saat membandingkan dua tawaran kerja, hitung gaji bersih masing-masing dengan kalkulator gaji bersih, karena tunjangan tidak tetap dan fasilitas bisa membuat perbedaan besar.")),
  ],
  faq=[("Kenapa gaji bersih Desember berbeda?", "Karena PPh 21 Desember dihitung ulang dengan tarif setahun. Bisa lebih besar atau lebih kecil dari bulan biasa."),
       ("Apakah uang makan termasuk upah untuk BPJS?", "Tidak bila dibayar berdasarkan kehadiran. Uang makan harian termasuk tunjangan tidak tetap, tetapi tetap dihitung sebagai penghasilan untuk pajak.")])

A(slug="aturan-thr-dan-tips-mengelolanya", calc="thr", img="thr", date="27 November 2026",
  title="Aturan THR Terbaru: Siapa yang Berhak, Cara Hitung, dan Tips Mengelolanya",
  h1="Aturan THR: Hak, Cara Hitung, dan Tips Mengelolanya",
  desc="Panduan THR karyawan: dasar hukum, siapa yang berhak, rumus THR proporsional, batas waktu pembayaran, pajak THR, dan tips menggunakan THR dengan bijak.",
  lead="Tunjangan Hari Raya (THR) adalah hak karyawan yang wajib dibayar perusahaan menjelang hari raya keagamaan. Berikut aturan dan cara menghitungnya.",
  body=[
      ("Pengertian dan dasar hukum THR", """<p><b>Tunjangan Hari Raya Keagamaan (THR)</b> adalah pendapatan non-upah yang wajib dibayarkan pengusaha kepada pekerja menjelang hari raya keagamaan, yaitu Idulfitri, Natal, Nyepi, Waisak, atau Imlek sesuai agama pekerja (atau sesuai kesepakatan). Aturan utamanya adalah <b>Permenaker Nomor 6 Tahun 2016</b>, diperkuat oleh peraturan pemerintah tentang pengupahan.</p>
<p>THR wajib dibayar <b>paling lambat 7 hari sebelum hari raya</b>, dan tidak boleh dicicil kecuali ada ketentuan khusus dari pemerintah. Setiap tahun Kementerian Ketenagakerjaan biasanya menerbitkan surat edaran yang menegaskan kewajiban ini.</p>"""),
      ("Siapa yang berhak menerima THR?", """<ul><li>Pekerja dengan masa kerja <b>minimal 1 bulan terus-menerus</b>.</li>
<li>Berlaku untuk karyawan tetap (PKWTT) maupun kontrak (PKWT).</li>
<li>Pekerja harian lepas juga berhak, dengan dasar perhitungan upah rata-rata.</li>
<li>Karyawan tetap yang di-PHK dalam 30 hari sebelum hari raya tetap berhak atas THR.</li></ul>"""),
      ("Cara menghitung THR", """<p>Dasar THR adalah <b>upah satu bulan</b>, yaitu gaji pokok ditambah tunjangan tetap.</p>
<div class="formula">Masa kerja ≥ 12 bulan : THR = 1 × upah
Masa kerja 1–12 bulan : THR = (masa kerja ÷ 12) × upah</div>
<p>Contoh: upah Rp6.000.000 dan masa kerja 8 bulan, maka THR = 8/12 × Rp6.000.000 = Rp4.000.000. Untuk pekerja harian lepas dengan masa kerja 12 bulan atau lebih, upah satu bulan dihitung dari rata-rata upah 12 bulan terakhir; bila kurang dari 12 bulan, dari rata-rata upah per bulan selama masa kerja.</p>
[[CH_THR]]"""),
      ("THR dan pajak", """<p>THR termasuk penghasilan yang dipotong PPh 21. Dengan metode TER, pajak bulan THR dihitung dari gaji ditambah THR, sehingga tarifnya naik ke lapisan lebih tinggi dan potongannya melonjak. Namun di bulan Desember semua penghasilan setahun dihitung ulang dengan tarif Pasal 17, sehingga total pajak setahun tidak bertambah hanya karena cara potong ini.</p>"""),
      ("Tips mengelola THR", "<ul>"
       "<li><b>Hitung THR bersih dulu</b>, setelah dipotong pajak, baru buat rencana belanja.</li>"
       "<li><b>Bagi ke beberapa pos</b>: kebutuhan hari raya, zakat atau sedekah, mudik, dan tabungan. Tentukan persentasenya sebelum uang masuk.</li>"
       "<li><b>Lunasi utang berbunga tinggi</b> seperti kartu kredit atau paylater sebelum belanja konsumtif.</li>"
       "<li><b>Sisakan sebagian untuk setelah lebaran.</b> Pengeluaran sering membengkak, sementara gaji berikutnya baru datang beberapa minggu kemudian.</li>"
       "<li><b>Waspadai diskon.</b> Buat daftar belanja dan patok anggaran agar THR tidak habis untuk barang yang tidak direncanakan.</li></ul>"
       + TIP("bila THR tidak dibayar atau terlambat, pekerja bisa melapor ke posko pengaduan THR Kementerian Ketenagakerjaan atau dinas ketenagakerjaan setempat. Pengusaha yang terlambat dikenai denda 5% dari total THR, dan denda ini tidak menghapus kewajiban membayar THR.")),
  ],
  faq=[("Apakah THR boleh lebih besar dari 1 bulan upah?", "Boleh, bila diatur dalam perjanjian kerja, peraturan perusahaan, perjanjian kerja bersama, atau kebiasaan yang berlaku."),
       ("Apakah karyawan yang resign berhak THR?", "Untuk karyawan tetap, bila hubungan kerja berakhir dalam 30 hari sebelum hari raya, tetap berhak. Di luar itu, umumnya tidak.")])

A(slug="mengenal-bpjs-kesehatan-dan-ketenagakerjaan", calc="bpjs", img="bpjs", date="27 November 2026",
  title="Mengenal BPJS Kesehatan dan Ketenagakerjaan: Program, Manfaat, dan Iurannya",
  h1="Mengenal BPJS Kesehatan dan BPJS Ketenagakerjaan",
  desc="Penjelasan lengkap program BPJS untuk karyawan: Kesehatan, JHT, JP, JKK, JKM, dan JKP, besar iuran, manfaat, serta tips memastikan hak Anda terpenuhi.",
  lead="Setiap karyawan di Indonesia wajib ikut BPJS. Iurannya dipotong dari gaji, tetapi banyak yang belum tahu manfaat apa saja yang sebenarnya didapat.",
  body=[
      ("Dua badan, enam program", """<p>Jaminan sosial di Indonesia dikelola dua badan. <b>BPJS Kesehatan</b> menyelenggarakan Jaminan Kesehatan Nasional (JKN). <b>BPJS Ketenagakerjaan</b> menyelenggarakan lima program: Jaminan Hari Tua (JHT), Jaminan Pensiun (JP), Jaminan Kecelakaan Kerja (JKK), Jaminan Kematian (JKM), dan Jaminan Kehilangan Pekerjaan (JKP).</p>
[[CH_BPJS]]"""),
      ("BPJS Kesehatan", """<p>Memberi layanan kesehatan mulai dari puskesmas atau klinik (fasilitas kesehatan tingkat pertama) sampai rumah sakit dengan sistem rujukan. Iuran pekerja penerima upah adalah <b>5% dari upah</b>: 4% dibayar perusahaan dan 1% dipotong dari gaji, dengan batas upah Rp12 juta. Iuran ini sudah menanggung peserta, pasangan, dan sampai tiga anak.</p>
<p>Pemerintah juga sedang menerapkan <b>Kelas Rawat Inap Standar (KRIS)</b> secara bertahap untuk menyeragamkan standar ruang rawat inap peserta. Ikuti pengumuman resmi BPJS Kesehatan untuk perkembangan terbarunya.</p>"""),
      ("Program BPJS Ketenagakerjaan", """<ul><li><b>JHT</b>: tabungan yang dibayar bersama (3,7% perusahaan, 2% karyawan) dan dikembangkan oleh BPJS. Saldo bisa dicairkan saat berhenti bekerja, pensiun, cacat total tetap, atau meninggal; sebagian juga bisa diklaim lebih awal untuk kepemilikan rumah atau keperluan lain setelah kepesertaan 10 tahun.</li>
<li><b>JP</b>: memberi uang pensiun bulanan setelah mencapai usia pensiun, dengan syarat masa iuran minimal 15 tahun. Iuran 3% (2% perusahaan, 1% karyawan) dengan batas upah yang naik setiap tahun.</li>
<li><b>JKK</b>: menanggung biaya perawatan tanpa batas sesuai kebutuhan medis bila mengalami kecelakaan kerja atau penyakit akibat kerja, termasuk kecelakaan dalam perjalanan berangkat dan pulang kerja. Iuran 0,24%–1,74% ditanggung perusahaan.</li>
<li><b>JKM</b>: santunan kepada ahli waris bila peserta meninggal bukan karena kecelakaan kerja, termasuk beasiswa pendidikan anak sesuai ketentuan. Iuran 0,3% ditanggung perusahaan.</li>
<li><b>JKP</b>: bagi yang terkena PHK, memberi uang tunai untuk beberapa bulan, akses informasi pasar kerja, dan pelatihan kerja. Tidak ada iuran tambahan.</li></ul>"""),
      ("Tips memastikan hak BPJS Anda", "<ul>"
       "<li><b>Unduh aplikasi resmi</b> (Mobile JKN dan JMO) untuk mengecek status kepesertaan dan saldo JHT. Pastikan iuran tercatat setiap bulan.</li>"
       "<li><b>Cocokkan upah yang dilaporkan.</b> Bila perusahaan melaporkan upah lebih rendah dari upah sebenarnya, saldo JHT dan manfaat pensiun Anda ikut kecil.</li>"
       "<li><b>Daftarkan anggota keluarga</b> (pasangan dan anak) di BPJS Kesehatan agar ikut tertanggung tanpa iuran tambahan.</li>"
       "<li><b>Ikuti alur rujukan</b>: mulai dari faskes tingkat pertama, kecuali kondisi gawat darurat.</li>"
       "<li><b>Laporkan kecelakaan kerja</b> ke perusahaan secepatnya agar klaim JKK diproses.</li>"
       "<li><b>Jangan buru-buru mencairkan JHT</b> bila tidak mendesak. Saldo terus dikembangkan dan menjadi bekal hari tua.</li></ul>"
       + TIP("perusahaan yang memotong iuran dari gaji tetapi tidak menyetorkannya melanggar aturan. Laporkan ke BPJS atau dinas ketenagakerjaan setempat.")),
  ],
  faq=[("Apakah iuran BPJS mengurangi pajak?", "Iuran JHT dan JP yang dibayar karyawan menjadi pengurang penghasilan kena pajak. Iuran BPJS Kesehatan karyawan tidak."),
       ("Bisakah punya BPJS Kesehatan dan asuransi swasta sekaligus?", "Bisa. Beberapa asuransi swasta menyediakan skema koordinasi manfaat (COB) dengan BPJS Kesehatan.")])

A(slug="panduan-kpr-rumah-pertama", calc="kpr", img="kpr", date="27 November 2026",
  title="Panduan KPR Rumah Pertama: Syarat, Bunga Fixed vs Floating, dan Tips Lolos",
  h1="Panduan KPR untuk Pembeli Rumah Pertama",
  desc="Pengertian KPR, cara kerja bunga fixed dan floating, syarat pengajuan, biaya yang perlu disiapkan, serta tips agar KPR disetujui dan cicilan tetap aman.",
  lead="KPR (Kredit Pemilikan Rumah) membantu Anda membeli rumah dengan mencicil hingga puluhan tahun. Pahami cara kerjanya sebelum menandatangani akad.",
  body=[
      ("Apa itu KPR?", """<p><b>KPR</b> adalah kredit dari bank untuk membeli rumah, dengan rumah itu sendiri sebagai jaminan. Anda membayar uang muka (DP), sisanya dibiayai bank dan dicicil setiap bulan selama tenor yang disepakati, biasanya 5 sampai 25 tahun. Selama kredit berjalan, sertifikat rumah dipegang bank dan baru diserahkan setelah lunas.</p>
<p>Selain KPR konvensional, ada juga <b>KPR syariah</b> dengan akad seperti murabahah (jual beli dengan margin tetap), dan <b>KPR bersubsidi</b> (FLPP) untuk masyarakat berpenghasilan rendah dengan bunga tetap rendah sepanjang tenor.</p>"""),
      ("Bunga fixed dan floating", """<p>KPR konvensional umumnya memakai <b>bunga fixed</b> di awal, misalnya 3–5 tahun, lalu beralih ke <b>bunga floating</b> yang mengikuti suku bunga pasar. Cicilan dihitung dengan metode anuitas: jumlahnya tetap selama bunga tidak berubah, dan dihitung ulang ketika bunga floating mulai berlaku.</p>
[[CH_KPR]]
<p>Inilah risiko terbesar KPR: cicilan bisa naik signifikan setelah masa promosi berakhir. Selalu simulasikan cicilan dengan bunga floating yang realistis sebelum memilih rumah.</p>"""),
      ("Syarat umum pengajuan", """<ul><li>WNI, usia minimal 21 tahun atau sudah menikah, dan usia saat lunas tidak melebihi batas bank (umumnya 55–65 tahun).</li>
<li>Penghasilan tetap dengan masa kerja minimal 1–2 tahun, atau usaha yang sudah berjalan bagi wiraswasta.</li>
<li>Dokumen: KTP, KK, NPWP, slip gaji atau laporan keuangan, rekening koran beberapa bulan terakhir, dan dokumen rumah (dari developer atau penjual).</li>
<li>Riwayat kredit baik di <b>SLIK OJK</b>. Tunggakan kartu kredit atau pinjaman online bisa membuat pengajuan ditolak.</li></ul>"""),
      ("Biaya di luar DP", """<p>Banyak pembeli rumah pertama hanya menyiapkan DP. Padahal ada biaya lain yang perlu dibayar di awal: provisi dan administrasi bank, biaya appraisal, notaris dan akta (AJB, APHT), asuransi jiwa dan kebakaran, serta <b>BPHTB</b> (pajak pembeli) bila tidak ditanggung developer atau program pemerintah. Totalnya bisa beberapa persen dari harga rumah, jadi tanyakan rinciannya sejak awal.</p>"""),
      ("Tips agar KPR lolos dan cicilan aman", "<ul>"
       "<li><b>Jaga cicilan di bawah 30–35% penghasilan</b>, termasuk cicilan lain yang sudah berjalan.</li>"
       "<li><b>Bersihkan riwayat kredit</b> beberapa bulan sebelum mengajukan: lunasi tunggakan dan kurangi limit kartu kredit yang tidak terpakai.</li>"
       "<li><b>Perbesar DP</b> bila memungkinkan. Pokok yang lebih kecil berarti total bunga jauh lebih rendah.</li>"
       "<li><b>Bandingkan beberapa bank</b>, bukan hanya bunga promosi, tetapi juga bunga floating historis, penalti pelunasan, dan biaya.</li>"
       "<li><b>Siapkan dana cadangan</b> minimal 6 kali cicilan untuk berjaga-jaga bila penghasilan terganggu.</li>"
       "<li><b>Pertimbangkan pelunasan sebagian</b> atau take over ke bank lain saat bunga floating tinggi.</li></ul>"
       + TIP("coba simulasi KPR dengan beberapa skenario bunga floating, misalnya 10%, 12%, dan 13%, untuk memastikan cicilan tetap terjangkau.")),
  ],
  faq=[("Lebih baik KPR atau menabung dulu?", "Tergantung kenaikan harga rumah di lokasi incaran, kestabilan penghasilan, dan kesiapan dana darurat. KPR memberi rumah lebih cepat, tetapi dengan biaya bunga."),
       ("Apa itu take over KPR?", "Memindahkan sisa KPR ke bank lain yang menawarkan bunga lebih rendah. Hitung biayanya (penalti, provisi, notaris) dibanding penghematan bunga.")])

A(slug="bunga-flat-vs-efektif-kredit-kendaraan", calc="kredit-kendaraan", img="kredit-kendaraan", date="27 November 2026",
  title="Bunga Flat vs Bunga Efektif: Panduan Kredit Motor dan Mobil",
  h1="Bunga Flat vs Bunga Efektif pada Kredit Kendaraan",
  desc="Kenali perbedaan bunga flat dan efektif, kenapa bunga flat terlihat murah, biaya tersembunyi kredit kendaraan, dan tips memilih leasing.",
  lead="Brosur kredit motor dan mobil sering menampilkan bunga yang terlihat kecil. Pahami cara membacanya agar Anda tahu biaya sebenarnya.",
  body=[
      ("Apa itu bunga flat?", """<p><b>Bunga flat</b> dihitung dari pokok pinjaman awal selama seluruh tenor, walaupun sisa utang berkurang setiap bulan. Cicilannya mudah dihitung: (pokok + pokok × bunga × tahun) ÷ jumlah bulan. Metode ini lazim dipakai perusahaan pembiayaan (leasing) untuk kredit kendaraan.</p>
<p><b>Bunga efektif</b> dihitung dari sisa pokok. Di awal porsi bunga besar, makin lama makin kecil. Inilah metode yang dipakai KPR dan sebagian besar kredit bank.</p>"""),
      ("Kenapa bunga flat terlihat lebih murah", """<p>Pada bunga flat, Anda membayar bunga atas seluruh pokok awal sampai akhir, padahal rata-rata sisa utang sepanjang tenor hanya sekitar setengahnya. Akibatnya bunga flat setara bunga efektif yang hampir <b>dua kali lipat</b>.</p>
[[CH_FLAT]]
<p>Karena itu, saat membandingkan tawaran leasing dengan kredit bank atau KTA, ubah dulu semua angka ke bunga efektif.</p>"""),
      ("Biaya selain cicilan", """<ul><li><b>Uang muka (DP)</b> dan angsuran pertama yang sering dibayar di depan.</li>
<li><b>Biaya administrasi dan provisi.</b></li><li><b>Asuransi kendaraan</b>, all risk atau total loss only, sering dimasukkan ke cicilan.</li>
<li><b>Biaya fidusia</b>, pendaftaran jaminan kendaraan.</li><li><b>Denda keterlambatan</b> harian dan <b>penalti pelunasan dipercepat</b>.</li></ul>
<p>Mintalah <b>total biaya yang harus dibayar</b> (DP + seluruh cicilan + biaya lain) secara tertulis, lalu bandingkan dengan harga tunai.</p>"""),
      ("Tips memilih kredit kendaraan", "<ul>"
       "<li><b>Pilih leasing yang terdaftar dan diawasi OJK.</b></li>"
       "<li><b>DP besar, tenor pendek.</b> Kombinasi ini paling menghemat total bunga.</li>"
       "<li><b>Batasi cicilan kendaraan</b> sekitar 10–15% penghasilan, agar tidak mengganggu kebutuhan pokok dan tabungan.</li>"
       "<li><b>Hitung biaya kepemilikan</b>: bensin, pajak tahunan, servis, parkir, dan asuransi setelah lunas.</li>"
       "<li><b>Baca perjanjian sebelum tanda tangan</b>, terutama soal denda, penarikan kendaraan, dan pelunasan dipercepat.</li>"
       "<li><b>Jangan oper kredit di bawah tangan.</b> Pengalihan tanpa persetujuan leasing berisiko secara hukum.</li></ul>"
       + TIP("gunakan simulasi kredit kendaraan untuk melihat bunga efektif dari bunga flat yang ditawarkan, lalu bandingkan dengan pinjaman bank.")),
  ],
  faq=[("Apakah boleh melunasi kredit lebih cepat?", "Umumnya boleh, tetapi cek penalti dan cara menghitung sisa bunga. Pada bunga flat, penghematannya sering lebih kecil dari perkiraan."),
       ("Apakah leasing boleh menarik kendaraan sepihak?", "Penarikan harus mengikuti ketentuan hukum yang berlaku dan perjanjian fidusia. Bila ada sengketa, konsultasikan ke OJK atau lembaga penyelesaian sengketa.")])

A(slug="panduan-deposito-untuk-pemula", calc="deposito", img="deposito", date="27 November 2026",
  title="Panduan Deposito untuk Pemula: Cara Kerja, Pajak, Penjaminan LPS, dan Tips",
  h1="Panduan Deposito untuk Pemula",
  desc="Pengertian deposito, jenis-jenisnya, cara menghitung bunga dan pajak 20%, syarat penjaminan LPS, perbandingan dengan tabungan, dan tips memilih deposito.",
  lead="Deposito adalah salah satu cara paling sederhana dan aman untuk mengembangkan uang. Kenali cara kerjanya agar hasilnya maksimal.",
  body=[
      ("Apa itu deposito?", """<p><b>Deposito berjangka</b> adalah simpanan di bank yang hanya bisa diambil setelah jangka waktu tertentu (tenor), misalnya 1, 3, 6, 12, atau 24 bulan. Sebagai imbalan karena dana &ldquo;dikunci&rdquo;, bank memberi bunga yang lebih tinggi dari tabungan biasa, dan besarnya sudah pasti sejak awal.</p>
<p>Selain deposito konvensional, ada <b>deposito syariah</b> dengan sistem bagi hasil (nisbah), serta deposito yang bisa dibuka sepenuhnya secara online melalui aplikasi bank dengan setoran awal lebih kecil.</p>"""),
      ("Bunga dan pajak deposito", """<p>Bunga deposito dikenai <b>pajak final 20%</b> yang langsung dipotong bank. Bunga tidak dipotong pajak bila total simpanan Anda di bank itu tidak lebih dari Rp7,5 juta.</p>
[[CH_DEPO]]
<p>Saat jatuh tempo, Anda bisa memilih <b>ARO</b> (diperpanjang otomatis), dengan bunga ditambahkan ke pokok sehingga ikut berbunga, atau bunga dikirim ke rekening tabungan.</p>"""),
      ("Penjaminan LPS", """<p>Simpanan di bank peserta <b>Lembaga Penjamin Simpanan (LPS)</b> dijamin sampai <b>Rp2 miliar per nasabah per bank</b>. Agar dijamin, ada tiga syarat utama: simpanan tercatat dalam pembukuan bank, bunga yang Anda terima <b>tidak melebihi tingkat bunga penjaminan LPS</b>, dan Anda tidak menyebabkan bank menjadi bermasalah.</p>
<p>Syarat kedua paling sering terlupa. Bila bank menawarkan bunga jauh lebih tinggi dari tingkat penjaminan LPS, simpanan Anda bisa tidak dijamin. Cek tingkat bunga penjaminan terbaru di situs resmi LPS, karena angkanya ditinjau berkala.</p>"""),
      ("Tips memilih dan memakai deposito", "<ul>"
       "<li><b>Gunakan untuk tujuan jelas</b> dengan jangka waktu pasti, misalnya DP rumah dua tahun lagi atau biaya sekolah tahun depan.</li>"
       "<li><b>Jangan simpan dana darurat seluruhnya di deposito.</b> Pencairan sebelum jatuh tempo bisa kena penalti.</li>"
       "<li><b>Pecah ke beberapa deposito</b> dengan tanggal jatuh tempo berbeda (laddering) agar sebagian dana selalu tersedia.</li>"
       "<li><b>Bandingkan imbal hasil bersih</b> dengan alternatif lain seperti reksa dana pasar uang atau surat berharga negara (SBN) ritel, yang pajaknya berbeda.</li>"
       "<li><b>Perhatikan inflasi.</b> Bunga bersih yang lebih rendah dari inflasi berarti daya beli uang Anda tetap tergerus.</li>"
       "<li><b>Pastikan bank terdaftar di OJK dan peserta LPS</b>, terutama untuk bank digital atau BPR yang menawarkan bunga tinggi.</li></ul>"
       + TIP("hitung bunga bersih setelah pajak dengan kalkulator deposito, lalu bandingkan dengan imbal hasil bersih instrumen lain sebelum memutuskan.")),
  ],
  faq=[("Berapa minimal membuka deposito?", "Berbeda tiap bank. Deposito konvensional di kantor cabang umumnya mulai beberapa juta rupiah, sedangkan deposito online di bank digital bisa jauh lebih kecil."),
       ("Apakah deposito termasuk investasi?", "Deposito adalah produk simpanan dengan risiko sangat rendah. Cocok untuk menjaga nilai uang jangka pendek, tetapi imbal hasilnya terbatas.")])

A(slug="bunga-majemuk-dan-investasi-rutin", calc="investasi", img="investasi", date="27 November 2026",
  title="Bunga Majemuk dan Investasi Rutin: Cara Uang Bekerja untuk Anda",
  h1="Bunga Majemuk dan Investasi Rutin untuk Pemula",
  desc="Pengertian bunga majemuk, kenapa waktu adalah kunci, perbandingan instrumen investasi di Indonesia, dan tips memulai investasi rutin bulanan.",
  lead="Bunga majemuk membuat hasil investasi ikut menghasilkan. Semakin awal dan rutin Anda memulai, semakin besar efeknya.",
  body=[
      ("Apa itu bunga majemuk?", """<p><b>Bunga majemuk</b> (compound interest) berarti hasil investasi tidak diambil, tetapi ditambahkan ke modal sehingga periode berikutnya ikut menghasilkan. Hasilnya tumbuh seperti bola salju: pelan di awal, lalu makin cepat seiring waktu.</p>
[[CH_INV]]
<p>Grafik di atas menunjukkan dua hal penting. Pertama, <b>waktu</b> adalah faktor terbesar: selisih antara menabung biasa dan berinvestasi melebar tajam setelah 10 tahun. Kedua, perbedaan imbal hasil beberapa persen per tahun menghasilkan selisih ratusan juta dalam jangka panjang.</p>"""),
      ("Investasi rutin (dollar cost averaging)", """<p>Menyetor jumlah yang sama setiap bulan disebut <b>investasi rutin</b> atau dollar cost averaging. Keuntungannya, Anda tidak perlu menebak waktu terbaik untuk masuk pasar: saat harga turun, setoran yang sama membeli lebih banyak unit; saat harga naik, nilai investasi Anda ikut naik. Kebiasaan ini juga membantu disiplin, terutama bila diatur otomatis setiap hari gajian.</p>"""),
      ("Mengenal pilihan instrumen", """<ul><li><b>Reksa dana pasar uang</b>: risiko rendah, cocok untuk dana darurat dan tujuan di bawah 1 tahun.</li>
<li><b>SBN ritel</b> (ORI, SBR, Sukuk Ritel, Sukuk Tabungan): surat utang negara dengan kupon tetap atau mengambang, dijamin negara. Kupon dikenai pajak final 10%.</li>
<li><b>Reksa dana pendapatan tetap</b>: berisi obligasi, cocok untuk jangka menengah 1–3 tahun.</li>
<li><b>Reksa dana saham dan saham</b>: potensi imbal hasil tertinggi dalam jangka panjang, tetapi nilainya bisa naik-turun tajam. Cocok untuk tujuan di atas 5 tahun.</li>
<li><b>Emas</b>: sering dipakai sebagai lindung nilai, tanpa imbal hasil rutin.</li></ul>
<p>Pastikan produk dan aplikasi yang Anda pakai <b>terdaftar dan diawasi OJK</b>. Waspadai tawaran dengan imbal hasil pasti yang terlalu tinggi; itu ciri khas investasi bodong.</p>"""),
      ("Tips memulai investasi rutin", "<ul>"
       "<li><b>Siapkan dana darurat dulu</b>, minimal 3–6 kali pengeluaran bulanan, di instrumen yang mudah dicairkan.</li>"
       "<li><b>Tentukan tujuan dan jangka waktunya</b>, misalnya dana pendidikan 10 tahun atau dana pensiun 25 tahun. Jangka waktu menentukan instrumen yang cocok.</li>"
       "<li><b>Mulai kecil, tetapi rutin.</b> Banyak reksa dana bisa dimulai dari Rp10.000–Rp100.000.</li>"
       "<li><b>Naikkan setoran setiap kali gaji naik.</b> Kenaikan 5–10% per tahun berdampak besar pada nilai akhir.</li>"
       "<li><b>Diversifikasi</b>, jangan taruh semua uang di satu produk.</li>"
       "<li><b>Hitung inflasi.</b> Untuk melihat nilai riil, kurangi imbal hasil dengan perkiraan inflasi.</li>"
       "<li><b>Jangan panik saat pasar turun.</b> Untuk tujuan jangka panjang, penurunan sementara justru kesempatan membeli lebih murah.</li></ul>"
       + TIP("simulasikan beberapa skenario imbal hasil (pesimis, moderat, optimis) di kalkulator investasi untuk mengetahui berapa setoran bulanan yang dibutuhkan agar target tercapai.")),
  ],
  faq=[("Berapa imbal hasil yang realistis?", "Tergantung instrumen dan kondisi pasar. Tidak ada imbal hasil yang dijamin selain produk simpanan dan SBN dengan kupon tetap. Gunakan beberapa skenario."),
       ("Lebih baik investasi sekaligus atau rutin?", "Investasi sekaligus bisa unggul bila pasar terus naik, tetapi investasi rutin lebih mudah dijalankan dan mengurangi risiko masuk di harga puncak.")])

# ================= artikel tambahan (gelombang 2) =================
_u = 6e6 / 173
CH_LEMBUR = figure(bars(["1 jam", "2 jam", "3 jam", "4 jam"], [("Upah lembur", E, [_u * 1.5 + _u * 2 * (h - 1) for h in range(1, 5)])], rb, "Upah lembur di hari kerja",
                        values_on_top=lambda v: f"Rp{round(v):,}".replace(",", ".")),
                   "Upah lembur di hari kerja untuk upah Rp6 juta per bulan (upah sejam = Rp6.000.000 ÷ 173 ≈ Rp34.682). Jam pertama dibayar 1,5 kali, jam berikutnya 2 kali.")
CH_ANGGARAN = figure(bars(["Kebutuhan (50%)", "Keinginan (30%)", "Tabungan & investasi (20%)"], [("", E, [4e6, 2.4e6, 1.6e6])], jt, "Pembagian anggaran 50/30/20", values_on_top=jt),
                     "Contoh pembagian gaji bersih Rp8 juta per bulan dengan pola 50/30/20.")
CH_PINJAM = figure(bars(["Pinjaman daring (0,2%/hari)", "Kartu kredit (1,75%/bulan)", "KTA bank (contoh 12%/tahun)"], [("Biaya", C, [300000, 87500, 50000])], rb,
                        "Biaya meminjam Rp5 juta selama 30 hari", values_on_top=lambda v: f"Rp{round(v):,}".replace(",", ".")),
                   "Ilustrasi biaya bunga meminjam Rp5 juta selama 30 hari. Angka bunga hanya contoh; tarif sebenarnya berbeda menurut produk dan waktu.")
CH_TAKEOVER = figure(bars(["Bunga 11%", "Bunga 8%"], [("Cicilan per bulan", E, [5014221, 4329810])], jt, "Cicilan sebelum dan sesudah take over",
                          values_on_top=lambda v: f"Rp{round(v):,}".replace(",", ".")),
                     "Sisa pokok Rp400 juta dengan sisa tenor 12 tahun. Turun dari 11% ke 8% menghemat sekitar Rp684 ribu per bulan, atau sekitar Rp98,6 juta selama sisa tenor, sebelum dikurangi biaya take over.")
CH_DARURAT = figure(bars(["Lajang", "Menikah", "Menikah + anak", "Wiraswasta / freelancer"], [("Dana darurat", G, [15e6, 30e6, 45e6, 60e6])], jt, "Target dana darurat", values_on_top=jt),
                    "Contoh target dana darurat untuk pengeluaran Rp5 juta per bulan: 3, 6, 9, dan 12 kali pengeluaran bulanan.")

A(slug="cara-lapor-spt-tahunan-karyawan", calc="pph21", img="pph21", photo="a2-spt", date="27 November 2026",
  title="Cara Lapor SPT Tahunan Karyawan di Coretax: Langkah, Dokumen, dan Tips",
  h1="Cara Lapor SPT Tahunan untuk Karyawan",
  desc="Panduan lapor SPT Tahunan orang pribadi bagi karyawan lewat Coretax DJP: dokumen yang disiapkan, langkah pengisian, batas waktu, sanksi, dan tips agar tidak keliru.",
  lead="Walaupun pajak sudah dipotong kantor setiap bulan, karyawan tetap wajib melaporkan SPT Tahunan. Berikut langkah dan tipsnya.",
  body=[
      ("Kenapa karyawan tetap wajib lapor SPT?", """<p>PPh 21 yang dipotong perusahaan adalah <b>pembayaran</b> pajak. <b>SPT Tahunan</b> adalah <b>laporan</b> dari Anda sendiri kepada negara tentang penghasilan, harta, utang, dan pajak setahun. Keduanya berbeda: pajak bisa sudah lunas, tetapi kewajiban melapor tetap ada bagi setiap wajib pajak yang memiliki NPWP (sekarang NIK berfungsi sebagai NPWP).</p>
<p>Sejak pelaporan tahun pajak 2025, SPT Tahunan dilaporkan melalui sistem <b>Coretax DJP</b>, menggantikan DJP Online dan e-Filing lama.</p>"""),
      ("Dokumen yang perlu disiapkan", """<ul><li><b>Bukti potong PPh 21 (formulir 1721-A1)</b> dari perusahaan, atau A2 bagi ASN. Bila pindah kerja, kumpulkan bukti potong dari setiap pemberi kerja.</li>
<li><b>Akun Coretax</b> yang sudah aktif, beserta kata sandi dan sertifikat elektronik atau kode otorisasi untuk tanda tangan digital.</li>
<li><b>Daftar harta</b> per 31 Desember: tabungan, deposito, kendaraan, rumah, investasi, beserta nilai perolehannya.</li>
<li><b>Daftar utang</b>: sisa KPR, kredit kendaraan, kartu kredit, dan pinjaman lain.</li>
<li><b>Data keluarga</b> yang menjadi tanggungan.</li>
<li>Bukti penghasilan lain bila ada, misalnya bunga deposito (pajak final) atau honor sampingan.</li></ul>"""),
      ("Langkah lapor di Coretax", """<ol><li>Masuk ke Coretax DJP dengan NIK dan kata sandi.</li>
<li>Buka menu <b>Surat Pemberitahuan (SPT)</b>, lalu pilih <b>Buat Konsep SPT</b>.</li>
<li>Pilih jenis <b>PPh Orang Pribadi</b>, SPT Tahunan, periode, dan tahun pajak. Pilih model <b>Normal</b> untuk laporan pertama.</li>
<li>Buka konsep SPT. Sistem otomatis mengisi sejumlah data, termasuk penghasilan dan pajak dari bukti potong yang sudah dilaporkan pemberi kerja.</li>
<li>Periksa dan lengkapi: penghasilan lain, harta, utang, dan tanggungan.</li>
<li>Pastikan status SPT. Bagi karyawan dengan satu pemberi kerja, biasanya <b>nihil</b> karena pajak sudah dipotong pas.</li>
<li>Klik <b>Bayar dan Lapor</b>, lalu tanda tangani secara digital. Simpan bukti penerimaan elektronik (BPE).</li></ol>
<p>Bila hasilnya <b>kurang bayar</b>, sistem membuat kode billing untuk pembayaran. Bila <b>lebih bayar</b>, Anda bisa memilih pengembalian atau kompensasi.</p>"""),
      ("Batas waktu dan sanksi", """<p>SPT Tahunan orang pribadi wajib dilaporkan <b>paling lambat 3 bulan setelah tahun pajak berakhir</b>, yaitu 31 Maret. Keterlambatan dikenai sanksi administrasi berupa denda <b>Rp100.000</b>. Bila ada pengumuman perpanjangan atau penghapusan sanksi karena kendala sistem, ikuti informasi resmi DJP.</p>"""),
      ("Tips agar tidak keliru", "<ul>"
       "<li><b>Minta bukti potong sejak Januari.</b> Perusahaan wajib memberikannya paling lambat sebulan setelah tahun pajak berakhir.</li>"
       "<li><b>Cocokkan angka bukti potong dengan slip gaji.</b> Kesalahan status PTKP atau penghasilan sebaiknya dibetulkan oleh perusahaan.</li>"
       "<li><b>Laporkan harta dengan nilai perolehan</b>, bukan nilai pasar saat ini.</li>"
       "<li><b>Jangan menunggu akhir Maret.</b> Sistem biasanya padat menjelang tenggat.</li>"
       "<li><b>Simpan BPE dan semua dokumen</b> minimal lima tahun.</li>"
       "<li>Bila bingung, hubungi <b>Kring Pajak 1500200</b> atau datangi kantor pajak terdekat.</li></ul>"
       + TIP("sebelum lapor, cek ulang perhitungan pajak setahun Anda dengan kalkulator PPh 21, terutama bila ada bonus atau pindah kerja.")),
  ],
  faq=[("Apakah SPT saya pasti nihil?", "Bila penghasilan hanya dari satu pemberi kerja dan sudah dipotong dengan benar, biasanya nihil. Bila punya dua pemberi kerja dalam setahun atau penghasilan lain, bisa kurang bayar."),
       ("Apakah penghasilan di bawah PTKP wajib lapor?", "Bila sudah terdaftar sebagai wajib pajak, tetap lapor. Penghasilan di bawah PTKP dapat mengajukan status non-efektif sesuai ketentuan.")])

A(slug="cara-menghitung-upah-lembur", calc="gaji-bersih", img="gaji-bersih", photo="a2-lembur", date="27 November 2026",
  title="Cara Menghitung Upah Lembur Sesuai PP 35/2021 (Hari Kerja dan Hari Libur)",
  h1="Cara Menghitung Upah Lembur Karyawan",
  desc="Rumus upah lembur sesuai PP 35/2021: upah sejam 1/173, tarif lembur hari kerja dan hari libur, batas jam lembur, contoh hitung, dan tips memastikan lembur dibayar.",
  lead="Lembur adalah hak yang ada aturannya, termasuk cara menghitung upahnya. Berikut rumus resmi dan contohnya.",
  body=[
      ("Dasar aturan lembur", """<p>Waktu kerja lembur adalah waktu kerja di luar jam kerja normal (7 jam sehari untuk 6 hari kerja, atau 8 jam sehari untuk 5 hari kerja, dengan total 40 jam seminggu), atau bekerja pada hari istirahat mingguan dan hari libur resmi. Aturannya ada di <b>PP 35/2021</b> sebagai turunan UU Cipta Kerja.</p>
<ul><li>Lembur harus atas <b>perintah dan persetujuan</b> pekerja, sebaiknya tertulis.</li>
<li>Paling lama <b>4 jam sehari dan 18 jam seminggu</b> (tidak termasuk lembur di hari libur).</li>
<li>Pekerja lembur berhak atas upah lembur, istirahat yang cukup, dan makanan-minuman minimal 1.400 kalori bila lembur 4 jam atau lebih.</li></ul>"""),
      ("Rumus upah lembur", """<div class="formula">Upah sejam = 1/173 × upah sebulan
(upah = gaji pokok + tunjangan tetap; bila tunjangan tetap
 lebih dari 25%, dasar minimal 75% dari total upah)</div>
<p><b>Lembur di hari kerja:</b> jam pertama 1,5 × upah sejam; jam kedua dan seterusnya 2 × upah sejam.</p>
<p><b>Lembur di hari istirahat atau libur resmi</b> (pola 6 hari kerja): 7 jam pertama 2×, jam ke-8 3×, jam ke-9 sampai ke-10 4×. Untuk pola 5 hari kerja: 8 jam pertama 2×, jam ke-9 3×, jam ke-10 sampai ke-11 4×.</p>
[[CH_LEMBUR]]"""),
      ("Contoh lembur di hari libur", """<p>Upah Rp6.000.000, pola 5 hari kerja, lembur 9 jam pada hari Sabtu. Upah sejam Rp34.682. Upah lembur = 8 × 2 × Rp34.682 + 1 × 3 × Rp34.682 = Rp554.913 + Rp104.046 = sekitar <b>Rp658.960</b>.</p>
<p>Upah lembur termasuk penghasilan yang dikenai PPh 21, sehingga potongan pajak bulan itu bisa sedikit naik.</p>"""),
      ("Tips memastikan lembur dibayar benar", "<ul>"
       "<li><b>Catat jam mulai dan selesai</b> setiap lembur, beserta siapa yang memerintahkan.</li>"
       "<li><b>Minta surat perintah lembur</b> atau persetujuan tertulis, termasuk lewat email atau aplikasi absensi.</li>"
       "<li><b>Cek komponen lembur di slip gaji</b> dan hitung ulang dengan rumus di atas.</li>"
       "<li><b>Pahami pengecualian</b>: untuk jabatan tertentu dengan tanggung jawab tinggi (misalnya manajer), perusahaan dapat mengatur lain asalkan upahnya lebih tinggi; cek perjanjian kerja Anda.</li>"
       "<li>Bila ada sengketa, bicarakan dengan HRD atau serikat pekerja, lalu dinas ketenagakerjaan setempat.</li></ul>"
       + TIP("masukkan rata-rata upah lembur per bulan ke kolom tunjangan tidak tetap di kalkulator gaji bersih untuk melihat dampaknya pada pajak dan gaji yang diterima.")),
  ],
  faq=[("Apakah lembur boleh diganti cuti?", "Aturan mewajibkan upah lembur. Kesepakatan lain sebaiknya tidak merugikan pekerja dan tertulis jelas."),
       ("Apakah lembur dihitung dari gaji pokok saja?", "Dari upah sebulan, yaitu gaji pokok ditambah tunjangan tetap.")])

A(slug="tips-negosiasi-gaji", calc="gaji-bersih", img="gaji-bersih", photo="a2-negosiasi", date="27 November 2026",
  title="Tips Negosiasi Gaji: Gross vs Net, Benefit, dan Cara Menyampaikannya",
  h1="Tips Negosiasi Gaji untuk Pekerjaan Baru",
  desc="Cara menegosiasikan gaji: riset pasar, memahami gross dan net, menghitung nilai benefit, waktu yang tepat, dan contoh kalimat saat negosiasi.",
  lead="Angka yang Anda sepakati di awal menjadi dasar kenaikan gaji bertahun-tahun ke depan. Persiapkan negosiasinya dengan baik.",
  body=[
      ("Lakukan riset sebelum menyebut angka", """<p>Cari tahu kisaran gaji untuk posisi, pengalaman, industri, dan kota yang sama. Sumbernya bisa dari laporan gaji perusahaan rekrutmen, lowongan yang mencantumkan gaji, komunitas profesi, atau teman di industri yang sama. Tentukan tiga angka: <b>angka ideal</b>, <b>angka wajar</b>, dan <b>batas bawah</b> yang masih Anda terima.</p>"""),
      ("Pahami gross dan net", """<p>Pastikan angka yang dibicarakan <b>gross</b> (sebelum potongan) atau <b>net</b> (yang diterima). Selisihnya bisa beberapa ratus ribu sampai jutaan rupiah per bulan karena potongan BPJS dan PPh 21. Tanyakan juga apakah pajak ditanggung perusahaan.</p>
<p>Tanyakan rincian <b>gaji pokok dan tunjangan tetap</b>. Komponen ini menjadi dasar THR, BPJS (termasuk saldo JHT dan pensiun), lembur, dan pesangon. Tawaran dengan gaji pokok besar umumnya lebih menguntungkan dalam jangka panjang dibanding tunjangan tidak tetap yang besar.</p>"""),
      ("Hitung nilai benefit", """<ul><li>Asuransi kesehatan swasta untuk diri dan keluarga.</li><li>Bonus tahunan: apakah pasti atau tergantung kinerja.</li>
<li>Tunjangan transport, makan, komunikasi, atau kerja jarak jauh.</li><li>Fleksibilitas kerja dan waktu tempuh; perjalanan dua jam sehari juga ada biayanya.</li>
<li>Kesempatan belajar, sertifikasi, dan jenjang karier.</li></ul>
<p>Dua tawaran dengan gaji sama bisa sangat berbeda nilainya setelah benefit dihitung.</p>"""),
      ("Cara menyampaikan", "<ul>"
       "<li><b>Biarkan perusahaan menyebut angka lebih dulu</b> bila memungkinkan. Bila diminta, sebutkan rentang, dengan batas bawah sedikit di atas angka wajar Anda.</li>"
       "<li><b>Dasarkan pada nilai</b>, bukan kebutuhan pribadi: pengalaman, hasil kerja, dan keahlian yang relevan.</li>"
       "<li><b>Gunakan kalimat yang sopan dan jelas</b>, misalnya: &ldquo;Berdasarkan pengalaman saya di bidang ini dan kisaran pasar untuk posisi serupa, saya berharap di kisaran Rp… sampai Rp… gross per bulan.&rdquo;</li>"
       "<li><b>Negosiasikan selain gaji</b> bila angka sudah mentok: tanggal mulai, hari kerja jarak jauh, evaluasi gaji setelah masa percobaan, atau tunjangan pelatihan.</li>"
       "<li><b>Minta penawaran tertulis</b> yang mencantumkan gaji pokok, tunjangan, dan benefit sebelum mengundurkan diri dari pekerjaan lama.</li></ul>"
       + TIP("hitung gaji bersih dari setiap tawaran dengan kalkulator gaji bersih agar Anda membandingkan angka yang benar-benar diterima.")),
  ],
  faq=[("Berapa kenaikan yang wajar saat pindah kerja?", "Tidak ada angka baku. Bergantung pada pasar, tingkat jabatan, dan kebutuhan perusahaan. Riset pasar adalah patokan terbaik."),
       ("Apakah boleh menolak menyebut gaji saat ini?", "Boleh. Anda bisa menjawab dengan ekspektasi gaji untuk posisi baru berdasarkan riset pasar.")])

A(slug="cara-membuat-anggaran-50-30-20", calc="gaji-bersih", img="gaji-bersih", photo="a2-anggaran", date="27 November 2026",
  title="Cara Membuat Anggaran Bulanan dengan Metode 50/30/20",
  h1="Cara Membuat Anggaran Bulanan 50/30/20",
  desc="Panduan menyusun anggaran bulanan dengan metode 50/30/20: membagi gaji untuk kebutuhan, keinginan, dan tabungan, beserta contoh dan tips menjalankannya.",
  lead="Metode 50/30/20 adalah cara paling sederhana untuk mulai mengatur gaji tanpa harus mencatat setiap rupiah.",
  body=[
      ("Apa itu metode 50/30/20?", """<p>Metode ini membagi <b>penghasilan bersih</b> menjadi tiga pos:</p>
<ul><li><b>50% kebutuhan</b>: hal yang wajib dibayar, seperti makan, sewa atau cicilan rumah, listrik, air, transportasi, internet, pendidikan anak, dan cicilan utang minimum.</li>
<li><b>30% keinginan</b>: hal yang menyenangkan tetapi bisa dikurangi, seperti makan di luar, hiburan, belanja, liburan, dan langganan.</li>
<li><b>20% tabungan dan investasi</b>: dana darurat, tujuan jangka panjang, dan pelunasan utang lebih cepat.</li></ul>
[[CH_ANGGARAN]]"""),
      ("Langkah menyusun anggaran", """<ol><li><b>Hitung penghasilan bersih</b> rata-rata per bulan, setelah potongan BPJS dan pajak.</li>
<li><b>Catat pengeluaran satu sampai dua bulan</b> terakhir dari mutasi rekening dan dompet digital.</li>
<li><b>Kelompokkan</b> ke kebutuhan, keinginan, dan tabungan.</li>
<li><b>Bandingkan</b> dengan porsi 50/30/20 dan tentukan pos mana yang perlu diubah.</li>
<li><b>Otomatiskan</b>: pindahkan 20% ke rekening terpisah di hari gajian.</li></ol>"""),
      ("Menyesuaikan dengan kondisi Anda", """<p>Angka 50/30/20 adalah titik awal, bukan aturan mati. Di kota besar dengan biaya sewa tinggi, porsi kebutuhan bisa mencapai 60%; kurangi porsi keinginan, bukan tabungan. Bila punya utang berbunga tinggi, gunakan sebagian besar porsi 20% untuk melunasinya lebih dulu. Bila penghasilan naik, usahakan kenaikannya masuk ke tabungan, bukan menambah gaya hidup.</p>"""),
      ("Tips agar anggaran berjalan", "<ul>"
       "<li><b>Pisahkan rekening</b>: satu untuk kebutuhan, satu untuk belanja harian, satu untuk tabungan.</li>"
       "<li><b>Gunakan amplop digital</b> atau kantong tabungan di aplikasi bank.</li>"
       "<li><b>Evaluasi setiap bulan</b> selama 10–15 menit.</li>"
       "<li><b>Siapkan pos tahunan</b> seperti pajak kendaraan, asuransi, dan biaya sekolah dengan menabung sedikit setiap bulan.</li>"
       "<li><b>Beri ruang untuk diri sendiri.</b> Anggaran yang terlalu ketat sering gagal di bulan kedua.</li></ul>"
       + TIP("mulai dari angka gaji bersih yang tepat. Kalkulator gaji bersih menghitungnya setelah BPJS dan PPh 21.")),
  ],
  faq=[("Bagaimana bila penghasilan tidak tetap?", "Gunakan penghasilan bulan terendah sebagai dasar anggaran, lalu tabung kelebihan di bulan yang lebih baik."),
       ("Apakah cicilan termasuk kebutuhan?", "Cicilan minimum termasuk kebutuhan. Pembayaran ekstra untuk melunasi lebih cepat bisa diambil dari porsi 20%.")])

A(slug="cara-cek-saldo-dan-klaim-jht", calc="bpjs", img="bpjs", photo="a2-jht", date="27 November 2026",
  title="Cara Cek Saldo dan Klaim JHT BPJS Ketenagakerjaan: Syarat dan Langkahnya",
  h1="Cara Cek Saldo dan Klaim JHT BPJS Ketenagakerjaan",
  desc="Panduan cek saldo JHT, syarat klaim JHT saat berhenti bekerja atau klaim sebagian, dokumen yang dibutuhkan, cara klaim online, dan pajak atas JHT.",
  lead="Saldo JHT adalah tabungan Anda sendiri. Kenali cara mengecek dan mencairkannya agar hak Anda tidak terlewat.",
  body=[
      ("Cara cek saldo JHT", """<p>Cara termudah adalah lewat aplikasi resmi <b>JMO (Jamsostek Mobile)</b>: daftar dengan NIK dan data diri, lalu lihat saldo dan riwayat iuran per bulan. Saldo juga bisa dicek di kantor cabang BPJS Ketenagakerjaan. Periksa setidaknya beberapa bulan sekali untuk memastikan iuran benar-benar disetor perusahaan dan upah yang dilaporkan sesuai.</p>"""),
      ("Kapan JHT bisa dicairkan?", """<ul><li><b>Berhenti bekerja</b>, baik mengundurkan diri maupun terkena PHK, setelah masa tunggu sesuai ketentuan.</li>
<li><b>Mencapai usia pensiun</b>.</li><li><b>Cacat total tetap</b>.</li><li><b>Meninggal dunia</b>, dibayarkan kepada ahli waris.</li><li><b>Meninggalkan Indonesia</b> untuk selamanya.</li>
<li><b>Klaim sebagian</b> setelah kepesertaan minimal 10 tahun: sampai 10% untuk persiapan pensiun atau sampai 30% untuk kepemilikan rumah, dengan syarat masih aktif bekerja. Klaim sebagian hanya dapat dipilih salah satu.</li></ul>"""),
      ("Dokumen dan cara klaim", """<p>Dokumen yang umumnya diminta: e-KTP, kartu peserta BPJS Ketenagakerjaan (atau nomor peserta), surat keterangan berhenti bekerja atau paklaring dari perusahaan, buku tabungan atas nama sendiri, dan NPWP bila saldo melebihi batas tertentu. Klaim dapat dilakukan lewat aplikasi JMO, layanan online di situs resmi BPJS Ketenagakerjaan, atau datang ke kantor cabang. Ikuti daftar dokumen terbaru di kanal resmi karena persyaratan dapat diperbarui.</p>"""),
      ("Pajak atas JHT", """<p>JHT yang dibayarkan sekaligus dikenai PPh final: tarif <b>0% sampai Rp50 juta</b> dan <b>5% atas bagian di atas Rp50 juta</b>. Pajak ini dipotong langsung saat pencairan.</p>"""),
      ("Tips seputar JHT", "<ul>"
       "<li><b>Gunakan hanya kanal resmi.</b> Waspadai calo atau jasa pencairan yang meminta data pribadi dan biaya.</li>"
       "<li><b>Minta paklaring</b> sebelum hari terakhir bekerja.</li>"
       "<li><b>Pindah kerja? Pertimbangkan tidak mencairkan.</b> Saldo bisa digabung ke kepesertaan di perusahaan baru sehingga terus berkembang.</li>"
       "<li><b>Cocokkan data</b> nama, NIK, dan tanggal lahir di BPJS dengan KTP agar klaim tidak tertunda.</li></ul>"
       + TIP("lihat berapa iuran JHT yang disetor setiap bulan untuk upah Anda dengan kalkulator iuran BPJS.")),
  ],
  faq=[("Berapa lama proses klaim JHT?", "Umumnya beberapa hari kerja setelah dokumen lengkap dan terverifikasi, tergantung kanal dan antrean."),
       ("Apakah JHT berbeda dengan Jaminan Pensiun?", "Ya. JHT dibayar sekaligus dari saldo tabungan, sedangkan JP memberi uang pensiun bulanan setelah syarat masa iuran terpenuhi.")])

A(slug="pinjaman-online-vs-kredit-bank", calc="kredit-kendaraan", img="kredit-kendaraan", photo="a2-pinjam", date="27 November 2026",
  title="Pinjaman Online vs Kredit Bank: Bandingkan Biaya dan Risikonya",
  h1="Pinjaman Online vs Kredit Bank: Mana yang Lebih Aman?",
  desc="Perbandingan pinjaman daring (pindar), paylater, kartu kredit, dan KTA bank: cara membandingkan bunga, ciri pinjol ilegal, dan tips meminjam dengan aman.",
  lead="Pinjaman daring memang cepat, tetapi biayanya bisa jauh lebih mahal. Bandingkan dulu sebelum memilih.",
  body=[
      ("Jenis-jenis pinjaman", """<ul><li><b>Pinjaman daring (pindar)</b>: pinjaman lewat aplikasi platform yang berizin OJK, cair cepat, tenor pendek.</li>
<li><b>Paylater</b>: fasilitas beli sekarang bayar nanti di aplikasi belanja atau dompet digital.</li>
<li><b>Kartu kredit</b>: batas kredit bergulir; bunga dikenakan bila tagihan tidak dibayar penuh.</li>
<li><b>KTA bank</b> (kredit tanpa agunan): tenor 1–5 tahun, proses lebih ketat, bunga umumnya lebih rendah.</li></ul>"""),
      ("Bandingkan dalam satuan yang sama", """<p>Bunga pinjaman daring sering ditulis <b>per hari</b>, kartu kredit <b>per bulan</b>, dan KTA <b>per tahun</b>. Ubah ke satuan yang sama sebelum membandingkan. Bunga 0,2% per hari, misalnya, setara sekitar 6% per bulan atau 73% per tahun.</p>
[[CH_PINJAM]]
<p>OJK membatasi manfaat ekonomi (bunga dan biaya) pindar dan menurunkannya secara bertahap. Walau begitu, untuk pinjaman jangka pendek biayanya tetap jauh lebih tinggi daripada kredit bank.</p>"""),
      ("Ciri pinjol ilegal", """<ul><li>Tidak terdaftar di OJK. Cek daftar resmi di situs OJK atau hubungi kontak OJK 157.</li>
<li>Menawarkan lewat SMS atau WhatsApp tanpa diminta.</li><li>Meminta akses ke seluruh kontak, galeri, atau lokasi.</li>
<li>Bunga dan biaya tidak jelas, potongan di awal sangat besar.</li><li>Penagihan dengan ancaman atau menyebarkan data.</li></ul>"""),
      ("Tips meminjam dengan aman", "<ul>"
       "<li><b>Pinjam untuk kebutuhan, bukan gaya hidup.</b> Hindari meminjam untuk menutup pinjaman lain.</li>"
       "<li><b>Hitung total yang harus dikembalikan</b>, termasuk biaya layanan dan denda.</li>"
       "<li><b>Batasi total cicilan</b> di bawah 30% penghasilan.</li>"
       "<li><b>Utamakan kredit bank</b> bila waktu memungkinkan; biayanya lebih rendah.</li>"
       "<li><b>Bayar tepat waktu.</b> Riwayat pindar dan paylater tercatat di SLIK OJK dan memengaruhi pengajuan KPR atau kredit lain.</li></ul>"
       + TIP("untuk membandingkan bunga flat dan bunga efektif, gunakan simulasi kredit kendaraan; prinsip perhitungannya sama untuk pinjaman lain dengan cicilan tetap.")),
  ],
  faq=[("Apakah paylater memengaruhi KPR?", "Bisa. Paylater dari lembaga berizin tercatat di SLIK OJK. Tunggakan dapat membuat pengajuan kredit lain ditolak."),
       ("Bagaimana bila sudah terjerat pinjol ilegal?", "Jangan menambah pinjaman baru. Laporkan ke OJK dan Satgas PASTI, dan ke polisi bila ada ancaman atau penyebaran data.")])

A(slug="take-over-dan-pelunasan-kpr", calc="kpr", img="kpr", photo="a2-takeover", date="27 November 2026",
  title="Take Over KPR dan Pelunasan Dipercepat: Kapan Menguntungkan?",
  h1="Take Over KPR dan Pelunasan Dipercepat",
  desc="Penjelasan take over KPR ke bank lain dan pelunasan sebagian atau penuh: cara menghitung penghematan, biaya yang perlu diperhitungkan, dan tips memilih waktunya.",
  lead="Saat bunga floating terasa berat, ada dua cara meringankan KPR: pindah ke bank lain atau melunasi sebagian lebih cepat.",
  body=[
      ("Apa itu take over KPR?", """<p><b>Take over</b> berarti sisa KPR Anda dilunasi oleh bank baru, lalu Anda melanjutkan cicilan di bank baru dengan bunga dan tenor yang baru. Tujuannya biasanya mendapatkan bunga lebih rendah, misalnya bunga promosi fixed, atau mengubah tenor agar cicilan lebih ringan.</p>
[[CH_TAKEOVER]]"""),
      ("Biaya yang perlu dihitung", """<ul><li><b>Penalti pelunasan</b> di bank lama, umumnya persentase dari sisa pokok, terutama bila masih dalam masa fixed.</li>
<li><b>Provisi dan administrasi</b> di bank baru.</li><li><b>Appraisal</b> rumah.</li><li><b>Notaris</b> untuk roya (pengangkatan hak tanggungan lama) dan APHT baru.</li>
<li><b>Asuransi jiwa dan kebakaran</b> baru.</li></ul>
<p>Take over menguntungkan bila <b>total penghematan bunga jauh lebih besar dari total biaya</b>. Ingat juga bahwa bunga promosi di bank baru hanya berlaku beberapa tahun.</p>"""),
      ("Pelunasan sebagian atau penuh", """<p>Bila memiliki dana lebih, misalnya dari bonus, Anda bisa melunasi sebagian pokok. Ada dua pilihan setelahnya: <b>cicilan turun</b> dengan tenor tetap, atau <b>tenor dipersingkat</b> dengan cicilan tetap. Memperpendek tenor biasanya menghemat bunga lebih banyak.</p>
<p>Pelunasan paling efektif di <b>tahun-tahun awal</b> dan saat bunga floating tinggi, karena porsi bunga masih besar. Tanyakan penalti dan minimal pelunasan ke bank.</p>"""),
      ("Tips memutuskan", "<ul>"
       "<li><b>Hitung titik impas</b>: berapa bulan penghematan cicilan menutup biaya take over.</li>"
       "<li><b>Jangan habiskan dana darurat</b> untuk pelunasan KPR.</li>"
       "<li><b>Bandingkan dengan investasi</b>: bila bunga KPR lebih tinggi dari imbal hasil bersih investasi yang realistis, pelunasan cenderung lebih menguntungkan.</li>"
       "<li><b>Pastikan riwayat kredit lancar</b>; bank baru akan memeriksa SLIK OJK.</li>"
       "<li><b>Minta simulasi tertulis</b> dari bank lama dan bank baru.</li></ul>"
       + TIP("gunakan simulasi KPR untuk menghitung cicilan baru dengan sisa pokok, bunga, dan sisa tenor setelah take over.")),
  ],
  faq=[("Kapan waktu terbaik take over?", "Umumnya setelah masa fixed berakhir, karena penalti di masa fixed biasanya lebih besar, dan saat selisih bunga cukup lebar."),
       ("Apakah bisa take over KPR syariah?", "Bisa, baik ke bank syariah lain maupun konvensional, dengan perhitungan biaya dan akad yang berbeda.")])

A(slug="mengenal-sbn-ritel", calc="investasi", img="investasi", photo="a2-sbn", date="27 November 2026",
  title="Mengenal SBN Ritel: ORI, Sukuk Ritel, SBR, dan Sukuk Tabungan",
  h1="Mengenal SBN Ritel untuk Investor Pemula",
  desc="Penjelasan Surat Berharga Negara ritel: jenis ORI, SR, SBR, dan ST, perbedaan bisa diperdagangkan atau tidak, pajak kupon, cara membeli, dan tips memilih.",
  lead="SBN ritel adalah surat utang negara yang bisa dibeli perorangan mulai dari nominal kecil, dengan imbal hasil yang dijamin negara.",
  body=[
      ("Apa itu SBN ritel?", """<p><b>Surat Berharga Negara (SBN) ritel</b> diterbitkan pemerintah untuk dibeli masyarakat. Anda meminjamkan uang kepada negara dan menerima <b>kupon</b> (imbalan) secara berkala, lalu pokok dikembalikan saat jatuh tempo. Pembayaran kupon dan pokok dijamin undang-undang, sehingga risiko gagal bayarnya sangat rendah.</p>"""),
      ("Jenis-jenis SBN ritel", """<div class="tscroll"><table class="tbl"><thead><tr><th>Jenis</th><th>Prinsip</th><th>Kupon</th><th>Bisa dijual sebelum jatuh tempo?</th></tr></thead><tbody>
<tr><td>ORI (Obligasi Negara Ritel)</td><td>Konvensional</td><td>Tetap</td><td>Ya, di pasar sekunder</td></tr>
<tr><td>SR (Sukuk Ritel)</td><td>Syariah</td><td>Tetap</td><td>Ya, di pasar sekunder</td></tr>
<tr><td>SBR (Savings Bond Ritel)</td><td>Konvensional</td><td>Mengambang dengan batas bawah</td><td>Tidak; ada fasilitas pencairan awal sebagian</td></tr>
<tr><td>ST (Sukuk Tabungan)</td><td>Syariah</td><td>Mengambang dengan batas bawah</td><td>Tidak; ada fasilitas pencairan awal sebagian</td></tr></tbody></table></div>
<p>Seri yang bisa diperdagangkan harganya dapat naik atau turun di pasar sekunder, sehingga bisa untung atau rugi bila dijual sebelum jatuh tempo. Seri yang tidak bisa diperdagangkan nilainya tetap, tetapi pencairan awal hanya pada jadwal tertentu.</p>"""),
      ("Pajak dan cara membeli", """<p>Kupon SBN dikenai <b>PPh final 10%</b>, lebih rendah dari pajak bunga deposito 20%. SBN ritel dijual pada masa penawaran tertentu beberapa kali setahun melalui <b>mitra distribusi resmi</b> yang ditunjuk Kementerian Keuangan, seperti bank, perusahaan sekuritas, dan platform investasi. Nominal pembelian minimum umumnya mulai Rp1 juta.</p>"""),
      ("Tips berinvestasi di SBN ritel", "<ul>"
       "<li><b>Cocokkan tenor dengan tujuan</b>, umumnya 2–6 tahun.</li>"
       "<li><b>Pilih kupon tetap</b> bila memperkirakan suku bunga turun, dan <b>kupon mengambang</b> bila memperkirakan suku bunga naik.</li>"
       "<li><b>Beli di mitra distribusi resmi</b> dan cek daftarnya di situs Kementerian Keuangan.</li>"
       "<li><b>Catat jadwal masa penawaran</b>; kuota bisa habis lebih cepat.</li>"
       "<li><b>Jadikan bagian dari portofolio</b>, bersama dana darurat dan instrumen jangka panjang lain.</li></ul>"
       + TIP("simulasikan hasil investasi dengan kupon tertentu di kalkulator investasi, lalu bandingkan dengan deposito di kalkulator deposito.")),
  ],
  faq=[("Apakah SBN ritel aman?", "Pembayaran kupon dan pokok dijamin negara. Risiko yang tersisa adalah perubahan harga bila seri yang bisa diperdagangkan dijual sebelum jatuh tempo."),
       ("Apakah SBN ritel cocok untuk dana darurat?", "Kurang cocok, karena pencairan tidak selalu bisa kapan saja. Simpan dana darurat di instrumen yang lebih likuid.")])

A(slug="reksa-dana-vs-deposito", calc="deposito", img="deposito", photo="a2-reksadana", date="27 November 2026",
  title="Reksa Dana vs Deposito: Perbedaan, Risiko, Pajak, dan Mana yang Cocok",
  h1="Reksa Dana vs Deposito: Mana yang Cocok untuk Anda?",
  desc="Perbandingan reksa dana dan deposito dari sisi imbal hasil, risiko, pajak, likuiditas, dan penjaminan, serta panduan memilih sesuai tujuan keuangan.",
  lead="Deposito dan reksa dana sama-sama populer untuk mengembangkan uang, tetapi cara kerja dan risikonya berbeda.",
  body=[
      ("Perbedaan utama", """<div class="tscroll"><table class="tbl"><thead><tr><th>Aspek</th><th>Deposito</th><th>Reksa dana</th></tr></thead><tbody>
<tr><td>Jenis</td><td>Simpanan di bank</td><td>Investasi yang dikelola manajer investasi</td></tr>
<tr><td>Imbal hasil</td><td>Bunga pasti sejak awal</td><td>Tidak pasti, mengikuti nilai aset</td></tr>
<tr><td>Penjaminan</td><td>LPS sampai Rp2 miliar (dengan syarat)</td><td>Tidak dijamin; diawasi OJK, dana disimpan bank kustodian</td></tr>
<tr><td>Pajak untuk Anda</td><td>Bunga dipotong PPh final 20%</td><td>Keuntungan bukan objek pajak bagi investor (pajak di tingkat portofolio)</td></tr>
<tr><td>Pencairan</td><td>Saat jatuh tempo; sebelum itu bisa kena penalti</td><td>Kapan saja di hari bursa; dana masuk beberapa hari kerja</td></tr>
<tr><td>Modal awal</td><td>Umumnya jutaan rupiah</td><td>Bisa mulai puluhan ribu rupiah</td></tr></tbody></table></div>"""),
      ("Mengenal jenis reksa dana", """<ul><li><b>Pasar uang</b>: deposito dan surat utang jangka pendek. Risiko paling rendah, cocok untuk kebutuhan di bawah 1 tahun.</li>
<li><b>Pendapatan tetap</b>: obligasi. Cocok untuk 1–3 tahun.</li><li><b>Campuran</b>: gabungan saham dan obligasi.</li>
<li><b>Saham</b>: potensi tertinggi, fluktuasi terbesar. Cocok untuk 5 tahun ke atas.</li></ul>"""),
      ("Memilih sesuai tujuan", """<ul><li><b>Dana darurat</b>: tabungan dan reksa dana pasar uang, karena mudah dicairkan.</li>
<li><b>Tujuan pasti 1–2 tahun</b> (DP rumah, biaya nikah): deposito, reksa dana pasar uang, atau pendapatan tetap.</li>
<li><b>Tujuan jangka panjang</b> (pensiun, pendidikan anak): reksa dana saham atau campuran secara rutin, bersama SBN.</li></ul>"""),
      ("Tips memilih", "<ul>"
       "<li><b>Bandingkan imbal hasil bersih</b>: bunga deposito setelah pajak 20% dengan kinerja reksa dana setelah biaya.</li>"
       "<li><b>Pastikan produk dan aplikasi terdaftar di OJK.</b></li>"
       "<li><b>Lihat kinerja jangka panjang</b>, bukan hanya satu bulan terakhir, dan baca prospektus atau fund fact sheet.</li>"
       "<li><b>Perhatikan biaya</b> pembelian, penjualan, dan pengelolaan.</li>"
       "<li><b>Tidak harus memilih salah satu.</b> Kombinasi sesuai tujuan sering paling baik.</li></ul>"
       + TIP("hitung bunga bersih deposito dengan kalkulator deposito sebagai pembanding imbal hasil reksa dana.")),
  ],
  faq=[("Bisakah reksa dana rugi?", "Bisa. Nilai unit dapat turun, terutama reksa dana saham. Reksa dana pasar uang paling stabil, tetapi tetap tidak dijamin."),
       ("Apakah keuntungan reksa dana perlu dilaporkan di SPT?", "Keuntungan reksa dana bukan objek pajak bagi investor, tetapi nilai investasinya dilaporkan sebagai harta.")])

A(slug="berapa-dana-darurat-yang-ideal", calc="deposito", img="deposito", photo="a2-darurat", date="27 November 2026",
  title="Berapa Dana Darurat yang Ideal dan Di Mana Menyimpannya?",
  h1="Berapa Dana Darurat yang Ideal?",
  desc="Panduan dana darurat: pengertian, cara menghitung jumlah ideal sesuai status, tempat menyimpan yang tepat, dan langkah mengumpulkannya dari nol.",
  lead="Dana darurat adalah fondasi keuangan. Tanpa dana ini, satu kejadian tak terduga bisa memaksa Anda berutang.",
  body=[
      ("Apa itu dana darurat?", """<p><b>Dana darurat</b> adalah uang yang disisihkan khusus untuk kejadian tak terduga: kehilangan pekerjaan, sakit, kerusakan kendaraan atau rumah, atau kebutuhan mendesak keluarga. Dana ini <b>bukan</b> untuk liburan, belanja diskon, atau investasi.</p>"""),
      ("Berapa jumlah yang ideal?", """<p>Patokan umum dihitung dari <b>pengeluaran bulanan wajib</b>, bukan dari gaji:</p>
<ul><li>Lajang: 3–6 kali pengeluaran bulanan.</li><li>Menikah: 6 kali.</li><li>Menikah dengan anak: 9 kali atau lebih.</li>
<li>Wiraswasta, freelancer, atau penghasilan tidak tetap: 12 kali.</li></ul>
[[CH_DARURAT]]"""),
      ("Di mana menyimpannya?", """<p>Dana darurat harus <b>aman</b> dan <b>mudah dicairkan</b>, bukan untuk mengejar imbal hasil tinggi:</p>
<ul><li><b>Rekening tabungan terpisah</b>, untuk kebutuhan yang bisa muncul hari itu juga.</li>
<li><b>Reksa dana pasar uang</b>, dengan pencairan dalam beberapa hari kerja.</li>
<li><b>Deposito bertenor pendek</b> atau berjenjang (laddering), untuk sebagian dana.</li></ul>
<p>Hindari saham, kripto, atau properti untuk dana darurat karena nilainya bisa turun tepat saat Anda membutuhkannya.</p>"""),
      ("Langkah mengumpulkan dari nol", "<ol>"
       "<li><b>Hitung pengeluaran wajib</b> per bulan dan tentukan targetnya.</li>"
       "<li><b>Mulai dari target kecil</b>, misalnya satu bulan pengeluaran, lalu naikkan bertahap.</li>"
       "<li><b>Sisihkan otomatis</b> di hari gajian, misalnya 10–20% dari gaji bersih.</li>"
       "<li><b>Gunakan penghasilan tambahan</b> seperti THR atau bonus untuk mempercepat.</li>"
       "<li><b>Isi kembali</b> setiap kali dana terpakai.</li></ol>"
       + TIP("simpan sebagian dana darurat di deposito berjenjang dan hitung bunga bersihnya dengan kalkulator deposito.")),
  ],
  faq=[("Apakah perlu dana darurat bila sudah punya asuransi?", "Ya. Asuransi menanggung risiko tertentu, sedangkan dana darurat menutup kebutuhan mendesak lain seperti kehilangan penghasilan."),
       ("Lebih dulu dana darurat atau investasi?", "Umumnya dana darurat dulu, setidaknya sebagian, agar investasi tidak perlu dicairkan saat harga sedang turun.")])

CHARTS = {"CH_LEMBUR": CH_LEMBUR, "CH_ANGGARAN": CH_ANGGARAN, "CH_PINJAM": CH_PINJAM, "CH_TAKEOVER": CH_TAKEOVER, "CH_DARURAT": CH_DARURAT,
          "CH_PPH": CH_PPH, "CH_GAJI": CH_GAJI, "CH_BPJS": CH_BPJS, "CH_THR": CH_THR, "CH_KPR": CH_KPR, "CH_FLAT": CH_FLAT, "CH_DEPO": CH_DEPO, "CH_INV": CH_INV}
