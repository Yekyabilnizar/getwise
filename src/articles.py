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

CHARTS = {"CH_PPH": CH_PPH, "CH_GAJI": CH_GAJI, "CH_BPJS": CH_BPJS, "CH_THR": CH_THR, "CH_KPR": CH_KPR, "CH_FLAT": CH_FLAT, "CH_DEPO": CH_DEPO, "CH_INV": CH_INV}
