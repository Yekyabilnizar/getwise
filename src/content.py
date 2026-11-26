"""Isi situs GetWise: kategori, kalkulator (formulir + artikel), dan halaman statis."""

STATUS_OPTS = [("TK/0", "TK/0 – lajang, tanpa tanggungan"), ("TK/1", "TK/1 – lajang, 1 tanggungan"), ("TK/2", "TK/2 – lajang, 2 tanggungan"),
               ("TK/3", "TK/3 – lajang, 3 tanggungan"), ("K/0", "K/0 – kawin, tanpa tanggungan"), ("K/1", "K/1 – kawin, 1 tanggungan"),
               ("K/2", "K/2 – kawin, 2 tanggungan"), ("K/3", "K/3 – kawin, 3 tanggungan")]
JKK_OPTS = [("sangat_rendah", "Sangat rendah – 0,24% (kantor, jasa)"), ("rendah", "Rendah – 0,54%"), ("sedang", "Sedang – 0,89%"),
            ("tinggi", "Tinggi – 1,27%"), ("sangat_tinggi", "Sangat tinggi – 1,74% (tambang, konstruksi berat)")]
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]


def money(i, label, v, h=""):
    return (f'<div class="fld"><label for="{i}">{label}</label><div class="in pre" data-pre="Rp"><input id="{i}" inputmode="numeric" data-money value="{v}"></div>'
            + (f'<div class="h">{h}</div>' if h else "") + "</div>")


def num(i, label, v, suf="", h="", step="any"):
    return (f'<div class="fld"><label for="{i}">{label}</label><div class="in{" suf" if suf else ""}" data-suf="{suf}"><input id="{i}" inputmode="decimal" value="{v}"></div>'
            + (f'<div class="h">{h}</div>' if h else "") + "</div>")


def sel(i, label, opts, d, h=""):
    o = "".join(f'<option value="{a}"{" selected" if str(a) == str(d) else ""}>{b}</option>' for a, b in opts)
    return f'<div class="fld"><label for="{i}">{label}</label><select id="{i}">{o}</select>' + (f'<div class="h">{h}</div>' if h else "") + "</div>"


def chk(i, label, on=True):
    return f'<label class="chk"><input type="checkbox" id="{i}"{" checked" if on else ""}> {label}</label>'


BPJS_OPTS = ('<div class="fld"><label>Program BPJS yang diikuti</label>' + chk("kes", "BPJS Kesehatan") + chk("jht", "JHT (Jaminan Hari Tua)")
             + chk("jp", "JP (Jaminan Pensiun)") + chk("jkkjkm", "JKK &amp; JKM (dibayar perusahaan)") + "</div>"
             + sel("jkk", "Tingkat risiko kerja (JKK)", JKK_OPTS, "sangat_rendah"))

CATS = [
    dict(id="pajak-gaji", short="Pajak & Gaji", name="Pajak & Gaji", icon="🧾", desc="PPh 21 metode TER, gaji bersih, dan THR"),
    dict(id="bpjs", short="BPJS", name="BPJS & Jaminan Sosial", icon="🛡️", desc="Iuran BPJS Kesehatan dan Ketenagakerjaan"),
    dict(id="kredit", short="Kredit", name="Kredit & Cicilan", icon="🏠", desc="KPR dan kredit kendaraan"),
    dict(id="investasi", short="Investasi", name="Tabungan & Investasi", icon="📈", desc="Deposito dan investasi rutin"),
]

SRC_TER = ("Direktorat Jenderal Pajak – Serba-serbi TER PPh Pasal 21", "https://pajak.go.id/id/artikel/serba-serbi-ter-pph-pasal-21-pajak-baru-atau-formula-baru")
SRC_TER2 = ("Direktorat Jenderal Pajak – Simpel pakai TER, begini penjelasannya", "https://www.pajak.go.id/id/artikel/simpel-pakai-ter-begini-penjelasannya")
SRC_PP58 = ("PP Nomor 58 Tahun 2023 tentang Tarif Pemotongan PPh Pasal 21 dan PMK Nomor 168 Tahun 2023", "")
SRC_HPP = ("UU Nomor 7 Tahun 2021 tentang Harmonisasi Peraturan Perpajakan (tarif Pasal 17)", "")
SRC_BPJSTK = ("BPJS Ketenagakerjaan – Berapa besaran iuran JHT, JKK, JKM, JP, dan JKP?", "https://www.bpjsketenagakerjaan.go.id/artikel/18913/artikel-berapa-besaran-iuran-jht-jkk-jkm-jp-dan-jkp")
SRC_KES = ("Perpres Nomor 64 Tahun 2020 tentang Jaminan Kesehatan (iuran 5%, batas upah Rp12 juta)", "")
SRC_JP = ("Batas upah Jaminan Pensiun 2026: Rp11.086.300 mulai Maret 2026 (sebelumnya Rp10.547.400)", "https://www.mondaq.com/employee-benefits-compensation/1756368/socialization-of-pension-wage-limit-regulations-for-the-year-2026-indonesia")

CALCS = []


def C(**k):
    CALCS.append(k)


# ============================================================ PPh 21
C(id="pph21", slug="kalkulator-pph-21", cat="pajak-gaji", icon="🧾", short="Kalkulator PPh 21",
  title="Kalkulator PPh 21 TER 2026 – Hitung Pajak Gaji Bulanan & Desember",
  h1="Kalkulator PPh 21 2026 (Metode TER)",
  desc="Hitung PPh 21 karyawan tetap dengan tarif efektif rata-rata (TER) PP 58/2023: pajak Januari–November, perhitungan ulang Desember, PTKP, dan biaya jabatan.",
  card="Pajak gaji bulanan metode TER dan perhitungan ulang Desember.",
  lead="Hitung potongan PPh 21 karyawan tetap per bulan dengan tarif efektif rata-rata (TER), lengkap dengan perhitungan ulang di bulan Desember sesuai tarif Pasal 17.",
  form=money("gaji", "Gaji pokok + tunjangan tetap / bulan", "10000000", "Penghasilan rutin setiap bulan sebelum potongan.")
  + money("tidakTetap", "Tunjangan tidak tetap / bulan", "0", "Lembur, insentif, uang makan harian, rata-rata per bulan.")
  + sel("status", "Status PTKP", STATUS_OPTS, "TK/0", "Status pada awal tahun pajak.")
  + money("bonus", "Bonus / THR setahun", "0", "Penghasilan tidak rutin yang dibayar sekali.")
  + sel("bulanBonus", "Bulan bonus dibayar", [(i + 1, b) for i, b in enumerate(BULAN)], 4),
  opts=BPJS_OPTS,
  sections=[
      ("Cara menghitung PPh 21 dengan TER", """<p>Sejak 1 Januari 2024, pemotongan PPh 21 karyawan tetap memakai <b>tarif efektif rata-rata (TER)</b> sesuai PP 58/2023 dan PMK 168/2023. Perhitungannya dibagi dua:</p>
<ol><li><b>Januari sampai November</b>: PPh 21 = <b>penghasilan bruto bulan itu × tarif TER</b>. Tarif dipilih dari tabel kategori A, B, atau C sesuai status PTKP dan besarnya bruto bulan tersebut.</li>
<li><b>Desember (masa pajak terakhir)</b>: pajak setahun dihitung ulang dengan tarif progresif Pasal 17, lalu dikurangi pajak yang sudah dipotong Januari–November. Selisihnya menjadi potongan Desember; bila negatif, kelebihannya dikembalikan.</li></ol>
<p>Karena itu potongan Desember sering berbeda dari bulan lain, terutama bila ada bonus, THR, atau perubahan gaji di tengah tahun.</p>"""),
      ("Apa saja yang termasuk penghasilan bruto?", """<p>Bruto bukan hanya gaji pokok. Yang dijumlahkan antara lain:</p>
<ul><li>gaji pokok, tunjangan tetap, dan tunjangan tidak tetap (lembur, insentif);</li>
<li>bonus, THR, dan penghasilan tidak rutin lain pada bulan dibayarkan;</li>
<li><b>premi asuransi yang dibayar perusahaan</b>: BPJS Kesehatan bagian perusahaan (4%), JKK, dan JKM. Komponen ini tidak Anda terima tunai, tetapi menambah bruto.</li></ul>
<p>Iuran JHT dan JP bagian perusahaan <b>tidak</b> ditambahkan ke bruto. Kalkulator ini menghitung semuanya otomatis dari pilihan program BPJS di pengaturan lanjutan.</p>"""),
      ("Kategori TER dan PTKP", """<p>Kategori TER ditentukan oleh status PTKP:</p>
<ul><li><b>Kategori A</b>: TK/0, TK/1, K/0 (PTKP Rp54 juta sampai Rp58,5 juta)</li>
<li><b>Kategori B</b>: TK/2, TK/3, K/1, K/2 (PTKP Rp63 juta sampai Rp67,5 juta)</li>
<li><b>Kategori C</b>: K/3 (PTKP Rp72 juta)</li></ul>
<p>PTKP setahun: Rp54.000.000 untuk wajib pajak, ditambah Rp4.500.000 bila kawin, dan Rp4.500.000 untuk setiap tanggungan (paling banyak tiga orang).</p>"""),
      ("Perhitungan Desember (tarif Pasal 17)", """<div class="formula">Penghasilan bruto setahun
− Biaya jabatan (5%, maks. Rp6.000.000 setahun)
− Iuran JHT 2% dan JP 1% yang dibayar karyawan
= Penghasilan neto setahun
− PTKP
= PKP (dibulatkan ke bawah ke ribuan)
PPh 21 setahun = tarif Pasal 17 × PKP
PPh 21 Desember = PPh 21 setahun − PPh 21 Januari–November</div>
<p>Tarif Pasal 17 (UU HPP): 5% sampai Rp60 juta; 15% di atas Rp60 juta sampai Rp250 juta; 25% di atas Rp250 juta sampai Rp500 juta; 30% di atas Rp500 juta sampai Rp5 miliar; 35% di atas Rp5 miliar.</p>"""),
      ("Contoh", """<p>Karyawan berstatus TK/0 dengan gaji Rp10.000.000 per bulan, tanpa BPJS dan tanpa bonus. Bruto Rp10.000.000 berada di lapisan TER kategori A di atas Rp9.650.000 sampai Rp10.050.000, tarifnya 2%. Potongan Januari–November Rp200.000 per bulan, total Rp2.200.000.</p>
<p>Di Desember: bruto setahun Rp120.000.000 − biaya jabatan Rp6.000.000 = neto Rp114.000.000; dikurangi PTKP Rp54.000.000 menjadi PKP Rp60.000.000; pajak setahun 5% × Rp60.000.000 = Rp3.000.000. Potongan Desember = Rp3.000.000 − Rp2.200.000 = <b>Rp800.000</b>.</p>"""),
  ],
  faq=[("Kenapa potongan Desember lebih besar dari bulan biasa?", "TER adalah tarif pendekatan. Di Desember pajak setahun dihitung ulang dengan tarif progresif Pasal 17, sehingga kekurangan pemotongan selama Januari–November ditagih sekaligus. Bonus atau kenaikan gaji di tengah tahun membuat selisihnya makin besar."),
       ("Apakah TER membuat pajak setahun lebih besar?", "Tidak. TER hanya mengubah cara memotong per bulan. Total pajak setahun tetap ditentukan oleh perhitungan Pasal 17 di masa pajak terakhir."),
       ("Bagaimana jika saya keluar kerja di tengah tahun?", "Bulan terakhir bekerja diperlakukan seperti Desember: pajak dihitung ulang dengan Pasal 17 untuk penghasilan yang disetahunkan sesuai ketentuan. Kalkulator ini mengasumsikan bekerja penuh Januari–Desember."),
       ("Apakah iuran BPJS Kesehatan karyawan (1%) mengurangi pajak?", "Tidak. Yang menjadi pengurang adalah iuran JHT dan JP yang dibayar karyawan, serta biaya jabatan."),
       ("Kategori TER berdasarkan status apa?", "Berdasarkan status PTKP pada awal tahun pajak (atau awal bekerja). Perubahan status di tengah tahun, misalnya menikah, baru berlaku untuk tahun pajak berikutnya.")],
  sources=[SRC_TER, SRC_TER2, SRC_PP58, SRC_HPP, SRC_BPJSTK],
  related=["gaji-bersih", "thr", "bpjs", "kpr"])

# ============================================================ gaji bersih
C(id="gaji-bersih", slug="kalkulator-gaji-bersih", cat="pajak-gaji", icon="💵", short="Kalkulator Gaji Bersih",
  title="Kalkulator Gaji Bersih 2026 – Take Home Pay Setelah BPJS & PPh 21",
  h1="Kalkulator Gaji Bersih (Take Home Pay) 2026",
  desc="Hitung gaji bersih yang diterima setelah dipotong BPJS Kesehatan, JHT, JP, dan PPh 21 TER, plus total biaya yang dikeluarkan perusahaan.",
  card="Gaji yang benar-benar diterima setelah BPJS dan PPh 21.",
  lead="Dari gaji kotor ke gaji yang masuk rekening: potongan BPJS Kesehatan, JHT, JP, dan PPh 21 dihitung otomatis, lengkap dengan biaya total yang ditanggung perusahaan.",
  form=money("gaji", "Gaji pokok + tunjangan tetap / bulan", "8000000") + money("tidakTetap", "Tunjangan tidak tetap / bulan", "0", "Lembur, insentif, uang transport harian.")
  + sel("status", "Status PTKP", STATUS_OPTS, "TK/0"),
  opts=BPJS_OPTS,
  sections=[
      ("Komponen potongan gaji", """<p>Gaji yang Anda terima (take home pay) adalah gaji kotor dikurangi tiga kelompok potongan wajib:</p>
<ul><li><b>BPJS Kesehatan 1%</b> dari upah, dengan batas upah Rp12.000.000 (perusahaan menanggung 4%).</li>
<li><b>JHT 2%</b> dari upah tanpa batas atas (perusahaan menanggung 3,7%).</li>
<li><b>JP 1%</b> dari upah dengan batas upah Rp11.086.300 mulai Maret 2026 (perusahaan menanggung 2%).</li>
<li><b>PPh 21</b> metode TER untuk bulan Januari–November.</li></ul>
<p>Potongan lain seperti koperasi, pinjaman, atau iuran serikat tidak dihitung karena berbeda di setiap perusahaan.</p>"""),
      ("Gaji bersih bulan biasa dan rata-rata setahun", """<p>Kalkulator menampilkan dua angka. <b>Gaji bersih bulan biasa</b> memakai pajak TER yang dipotong Januari–November. <b>Rata-rata setahun</b> memakai pajak tahunan yang sebenarnya dibagi 12, karena potongan Desember bisa lebih besar atau lebih kecil. Angka kedua lebih tepat untuk merencanakan anggaran bulanan.</p>"""),
      ("Biaya perusahaan", """<p>Bagi perusahaan, biaya satu karyawan lebih besar dari gaji kotornya karena ada iuran BPJS bagian pemberi kerja: Kesehatan 4%, JHT 3,7%, JP 2%, JKK 0,24% sampai 1,74% sesuai risiko, dan JKM 0,3%. Angka ini berguna bagi pemilik usaha yang sedang menyusun anggaran gaji.</p>"""),
      ("Contoh", """<p>Gaji Rp8.000.000, status TK/0, ikut semua program BPJS dengan risiko sangat rendah. Potongan karyawan: BPJS Kesehatan Rp80.000, JHT Rp160.000, JP Rp80.000. Bruto untuk pajak = Rp8.000.000 + premi yang dibayar perusahaan (Kesehatan Rp320.000, JKK Rp19.200, JKM Rp24.000) = Rp8.363.200, tarif TER kategori A 1,5%, sehingga PPh 21 Rp125.448. Gaji bersih bulan biasa sekitar <b>Rp7.554.552</b>.</p>"""),
  ],
  faq=[("Kenapa premi BPJS dari perusahaan menambah pajak saya?", "Sesuai ketentuan, premi asuransi kesehatan, kecelakaan kerja, dan kematian yang dibayar pemberi kerja termasuk penghasilan bruto karyawan, walaupun tidak diterima tunai."),
       ("Bagaimana jika perusahaan menanggung pajak saya (gross-up atau ditanggung)?", "Bila pajak ditanggung perusahaan, gaji bersih Anda sama dengan gaji kotor dikurangi BPJS. Kalkulator ini memakai skema umum: pajak dipotong dari gaji."),
       ("Apakah uang makan dan transport kena pajak?", "Bila diberikan dalam bentuk uang, ya, termasuk penghasilan bruto. Masukkan rata-ratanya di kolom tunjangan tidak tetap."),
       ("Upah untuk BPJS itu gaji pokok saja?", "Upah untuk iuran BPJS adalah gaji pokok ditambah tunjangan tetap. Kalkulator ini memakai kolom gaji pokok + tunjangan tetap sebagai dasar iuran.")],
  sources=[SRC_BPJSTK, SRC_KES, SRC_JP, SRC_TER, SRC_PP58],
  related=["pph21", "bpjs", "thr", "investasi"])

# ============================================================ THR
C(id="thr", slug="kalkulator-thr", cat="pajak-gaji", icon="🎁", short="Kalkulator THR",
  title="Kalkulator THR 2026 – Besaran THR Proporsional & Potongan Pajaknya",
  h1="Kalkulator THR Karyawan 2026",
  desc="Hitung besaran THR sesuai masa kerja (penuh atau proporsional) dan perkiraan potongan PPh 21 TER di bulan THR dibayarkan.",
  card="THR penuh atau proporsional, plus potongan pajaknya.",
  lead="Hitung hak THR sesuai masa kerja, lalu lihat berapa PPh 21 tambahan yang dipotong di bulan THR dibayarkan dan berapa THR bersih yang Anda terima.",
  form=money("gaji", "Gaji pokok + tunjangan tetap / bulan", "8000000", "Dasar THR adalah upah: gaji pokok ditambah tunjangan tetap.")
  + num("masaKerja", "Masa kerja (bulan)", "12", "bulan", "Dihitung sampai hari raya keagamaan.") + sel("status", "Status PTKP", STATUS_OPTS, "TK/0"),
  opts=money("tidakTetap", "Tunjangan tidak tetap / bulan", "0") + BPJS_OPTS,
  sections=[
      ("Siapa yang berhak dan berapa besarnya", """<p>Menurut Permenaker 6/2016, karyawan dengan masa kerja <b>minimal 1 bulan terus-menerus</b> berhak atas Tunjangan Hari Raya (THR), baik karyawan tetap (PKWTT) maupun kontrak (PKWT).</p>
<ul><li>Masa kerja <b>12 bulan atau lebih</b>: THR = 1 bulan upah.</li>
<li>Masa kerja <b>1 sampai kurang dari 12 bulan</b>: THR = masa kerja ÷ 12 × 1 bulan upah.</li></ul>
<p>Upah yang dimaksud adalah gaji pokok ditambah tunjangan tetap. THR wajib dibayar paling lambat 7 hari sebelum hari raya, dan perusahaan boleh memberi lebih besar bila diatur dalam perjanjian kerja atau kebiasaan.</p>"""),
      ("Kenapa potongan pajak di bulan THR besar?", """<p>Dengan metode TER, pajak bulan itu dihitung dari <b>bruto bulan tersebut</b> yang sudah termasuk THR. Bruto yang lebih besar jatuh ke lapisan tarif TER yang lebih tinggi, sehingga potongannya melonjak.</p>
<p>Lonjakan ini bukan pajak tambahan permanen. Di bulan Desember, pajak setahun dihitung ulang dengan tarif Pasal 17, sehingga potongan Desember menyesuaikan. Total pajak setahun pada umumnya sama apa pun bulan THR dibayar.</p>"""),
      ("Contoh", """<p>Gaji Rp8.000.000, masa kerja 6 bulan, status K/1, tanpa BPJS. THR = 6/12 × Rp8.000.000 = Rp4.000.000. Bulan biasa: bruto Rp8.000.000 kena TER kategori B 1% = Rp80.000. Bulan THR: bruto Rp12.000.000 kena 3% = Rp360.000. Tambahan potongan karena THR Rp280.000, sehingga THR bersih sekitar <b>Rp3.720.000</b>.</p>"""),
  ],
  faq=[("Apakah karyawan kontrak berhak THR?", "Ya. Karyawan PKWT dengan masa kerja minimal 1 bulan terus-menerus berhak atas THR."),
       ("Bagaimana jika berhenti sebelum hari raya?", "Karyawan tetap yang hubungan kerjanya berakhir dalam 30 hari sebelum hari raya tetap berhak atas THR. Untuk karyawan kontrak yang kontraknya berakhir sebelum hari raya, ketentuannya berbeda; cek perjanjian kerja Anda."),
       ("Apakah THR selalu kena pajak?", "THR termasuk penghasilan bruto dan dipotong PPh 21. Bila penghasilan setahun Anda di bawah PTKP, potongan akan dikembalikan atau tidak ada di perhitungan Desember."),
       ("Apakah THR dihitung dari gaji pokok saja?", "Dari upah, yaitu gaji pokok ditambah tunjangan tetap. Tunjangan tidak tetap seperti lembur tidak termasuk dasar THR.")],
  sources=[("Permenaker Nomor 6 Tahun 2016 tentang Tunjangan Hari Raya Keagamaan", ""), SRC_TER, SRC_PP58],
  related=["pph21", "gaji-bersih", "bpjs", "deposito"])

# ============================================================ BPJS
C(id="bpjs", slug="kalkulator-bpjs", cat="bpjs", icon="🛡️", short="Kalkulator Iuran BPJS",
  title="Kalkulator Iuran BPJS Kesehatan & Ketenagakerjaan 2026 (JHT, JP, JKK, JKM)",
  h1="Kalkulator Iuran BPJS 2026",
  desc="Hitung iuran BPJS Kesehatan dan BPJS Ketenagakerjaan (JHT, JP, JKK, JKM) bagian karyawan dan perusahaan, lengkap dengan batas upah terbaru.",
  card="Iuran Kesehatan, JHT, JP, JKK, JKM bagian karyawan & perusahaan.",
  lead="Hitung iuran BPJS Kesehatan dan BPJS Ketenagakerjaan per bulan, terpisah antara bagian yang dipotong dari gaji karyawan dan bagian yang ditanggung perusahaan.",
  form=money("gaji", "Upah per bulan", "8000000", "Gaji pokok + tunjangan tetap.") + BPJS_OPTS,
  sections=[
      ("Tarif iuran BPJS pekerja penerima upah", """<div class="tscroll"><table class="tbl"><thead><tr><th>Program</th><th>Perusahaan</th><th>Karyawan</th><th>Batas upah</th></tr></thead><tbody>
<tr><td>BPJS Kesehatan</td><td>4%</td><td>1%</td><td>Rp12.000.000</td></tr>
<tr><td>JHT (Jaminan Hari Tua)</td><td>3,7%</td><td>2%</td><td>tidak ada</td></tr>
<tr><td>JP (Jaminan Pensiun)</td><td>2%</td><td>1%</td><td>Rp11.086.300 (mulai Maret 2026)</td></tr>
<tr><td>JKK (Kecelakaan Kerja)</td><td>0,24%–1,74%</td><td>–</td><td>tidak ada</td></tr>
<tr><td>JKM (Kematian)</td><td>0,3%</td><td>–</td><td>tidak ada</td></tr></tbody></table></div>
<p>Jaminan Kehilangan Pekerjaan (JKP) tidak menambah iuran karena dibiayai pemerintah dan rekomposisi iuran yang sudah ada.</p>"""),
      ("Batas upah dan batas bawah", """<p>Untuk BPJS Kesehatan, upah di atas Rp12.000.000 tetap dihitung Rp12.000.000, dan upah yang dilaporkan tidak boleh di bawah upah minimum setempat. Untuk JP, batas upah diperbarui setiap Maret mengikuti pertumbuhan ekonomi; mulai Maret 2026 batasnya Rp11.086.300, sehingga iuran JP karyawan paling besar sekitar Rp110.863 per bulan.</p>
<p>Iuran BPJS Kesehatan 1% karyawan mencakup peserta, pasangan, dan sampai tiga anak. Anggota keluarga tambahan (misalnya anak keempat atau orang tua) dikenai tambahan 1% per orang.</p>"""),
      ("Contoh", """<p>Upah Rp8.000.000 dengan risiko kerja sangat rendah. Bagian karyawan: Kesehatan Rp80.000, JHT Rp160.000, JP Rp80.000, total Rp320.000. Bagian perusahaan: Kesehatan Rp320.000, JHT Rp296.000, JP Rp160.000, JKK Rp19.200, JKM Rp24.000, total Rp819.200.</p>"""),
  ],
  faq=[("Apakah iuran BPJS mengurangi pajak?", "Iuran JHT 2% dan JP 1% yang dibayar karyawan mengurangi penghasilan kena pajak. Iuran BPJS Kesehatan karyawan tidak. Sebaliknya, premi Kesehatan, JKK, dan JKM yang dibayar perusahaan menambah penghasilan bruto untuk PPh 21."),
       ("Bagaimana jika gaji saya di atas Rp12 juta?", "Iuran BPJS Kesehatan dihitung dari Rp12.000.000, jadi potongan karyawan paling besar Rp120.000 per bulan. JHT tetap dihitung dari seluruh upah."),
       ("Bagaimana dengan pekerja mandiri (bukan penerima upah)?", "Pekerja mandiri membayar iuran dengan skema berbeda (nominal tetap per kelas untuk Kesehatan dan berdasarkan penghasilan yang dilaporkan untuk Ketenagakerjaan). Kalkulator ini khusus pekerja penerima upah."),
       ("Kapan JHT bisa dicairkan?", "JHT dapat dicairkan saat usia pensiun 56 tahun, cacat total tetap, meninggal dunia, atau berhenti bekerja sesuai ketentuan. Sebagian saldo juga dapat diklaim lebih awal untuk keperluan tertentu.")],
  sources=[SRC_BPJSTK, SRC_KES, SRC_JP, ("PP 44/2015 (JKK & JKM), PP 45/2015 (JP), PP 46/2015 (JHT), PP 37/2021 jo. PP 6/2025 (JKP)", "")],
  related=["gaji-bersih", "pph21", "thr", "investasi"])

# ============================================================ KPR
C(id="kpr", slug="simulasi-kpr", cat="kredit", icon="🏠", short="Simulasi KPR",
  title="Simulasi KPR 2026 – Hitung Cicilan Rumah Bunga Fixed & Floating",
  h1="Simulasi KPR: Cicilan Rumah Fixed dan Floating",
  desc="Hitung cicilan KPR dengan bunga fixed lalu floating (metode anuitas), total bunga, sisa pokok per tahun, dan penghasilan minimal yang disarankan.",
  card="Cicilan rumah dengan bunga fixed lalu floating, plus jadwal per tahun.",
  lead="Simulasikan cicilan KPR dengan masa bunga fixed lalu floating. Lihat cicilan per bulan, total bunga, sisa pokok tiap tahun, dan penghasilan minimal yang biasanya disyaratkan bank.",
  form=money("harga", "Harga rumah", "600000000") + num("dpPersen", "Uang muka (DP)", "20", "%") + num("tenorTahun", "Tenor", "15", "tahun")
  + num("fixTahun", "Masa bunga fixed", "3", "tahun") + num("bungaFix", "Bunga fixed per tahun", "4,5", "%") + num("bungaFloat", "Perkiraan bunga floating per tahun", "11", "%", "Bunga setelah masa fixed berakhir."),
  sections=[
      ("Cara bank menghitung cicilan KPR", """<p>Hampir semua KPR di Indonesia memakai <b>metode anuitas</b>: cicilan per bulan sama selama suku bunga tidak berubah, tetapi porsi bunga besar di awal dan porsi pokok besar di akhir.</p>
<div class="formula">Cicilan = P × r ÷ (1 − (1 + r)^−n)
P = pokok pinjaman (harga − DP)
r = bunga per tahun ÷ 12
n = sisa tenor dalam bulan</div>
<p>Saat masa fixed berakhir, bank menghitung ulang cicilan dengan rumus yang sama memakai <b>sisa pokok</b>, <b>bunga floating</b>, dan <b>sisa tenor</b>. Karena bunga floating biasanya jauh lebih tinggi, cicilan bisa naik tajam.</p>"""),
      ("Fixed, floating, dan risiko lonjakan cicilan", """<p>Bunga promosi fixed (misalnya 3–5% untuk 1–5 tahun) membuat cicilan awal ringan. Setelah itu bunga mengikuti suku bunga acuan bank (floating) yang bisa naik atau turun. Simulasikan beberapa skenario bunga floating, misalnya 10%, 12%, dan 13%, untuk memastikan Anda tetap sanggup membayar bila bunga naik.</p>"""),
      ("Penghasilan minimal dan biaya lain", """<p>Bank umumnya mensyaratkan cicilan tidak lebih dari sekitar <b>30–35% penghasilan</b> bulanan (bisa gabungan suami-istri). Kalkulator ini menampilkan penghasilan minimal dengan patokan 30% dari cicilan tertinggi.</p>
<p>Selain DP, siapkan biaya awal seperti provisi dan administrasi bank, biaya notaris dan akta, asuransi jiwa dan kebakaran, serta pajak pembeli (BPHTB). Besarnya berbeda antarbank dan daerah; secara kasar bisa beberapa persen dari harga rumah.</p>"""),
      ("Tips menghemat bunga", """<ul><li>Perbesar DP untuk mengurangi pokok pinjaman.</li><li>Pilih tenor sependek yang masih nyaman; total bunga turun drastis.</li>
<li>Manfaatkan pelunasan sebagian saat bunga floating tinggi, dengan memperhatikan penalti pelunasan dipercepat.</li><li>Pertimbangkan take over KPR ke bank lain bila selisih bunga cukup besar.</li></ul>"""),
  ],
  faq=[("Berapa DP minimum KPR?", "Ditentukan bank sesuai ketentuan loan-to-value (LTV) Bank Indonesia dan program yang sedang berlaku; beberapa program rumah pertama bahkan membolehkan DP sangat kecil. Tanyakan langsung ke bank."),
       ("Kenapa sisa pokok berkurang lambat di tahun-tahun awal?", "Karena pada metode anuitas porsi bunga dihitung dari sisa pokok yang masih besar, sehingga sebagian besar cicilan awal habis untuk bunga."),
       ("Apakah hasil simulasi sama persis dengan bank?", "Mendekati. Bank bisa memakai pembulatan, hitungan hari, atau biaya asuransi yang dimasukkan ke cicilan, sehingga angkanya sedikit berbeda."),
       ("Lebih baik tenor pendek atau panjang?", "Tenor pendek: cicilan lebih besar tetapi total bunga jauh lebih kecil. Tenor panjang: cicilan ringan tetapi total bunga membengkak. Pilih tenor terpendek yang cicilannya tetap di bawah sekitar 30% penghasilan.")],
  sources=[("Rumus anuitas standar perbankan; ketentuan LTV/FTV Bank Indonesia", "")],
  related=["kredit-kendaraan", "investasi", "gaji-bersih", "deposito"])

# ============================================================ kredit kendaraan
C(id="kredit-kendaraan", slug="simulasi-kredit-kendaraan", cat="kredit", icon="🏍️", short="Simulasi Kredit Motor/Mobil",
  title="Simulasi Kredit Motor & Mobil – Bunga Flat ke Bunga Efektif",
  h1="Simulasi Kredit Motor dan Mobil",
  desc="Hitung cicilan kredit kendaraan dengan bunga flat, total bunga, dan bunga efektif tahunan yang sebenarnya untuk membandingkan penawaran leasing.",
  card="Cicilan bunga flat dan bunga efektif yang sebenarnya.",
  lead="Hitung cicilan kredit motor atau mobil dengan bunga flat, lalu lihat bunga efektif tahunan yang sebenarnya supaya Anda bisa membandingkan penawaran secara adil.",
  form=money("harga", "Harga kendaraan (OTR)", "30000000") + num("dpPersen", "Uang muka (DP)", "20", "%") + num("tenorBulan", "Tenor", "36", "bulan")
  + num("bungaFlat", "Bunga flat per tahun", "6", "%"),
  sections=[
      ("Bunga flat itu apa?", """<p>Kredit kendaraan di leasing umumnya memakai <b>bunga flat</b>: bunga dihitung dari pokok awal selama seluruh tenor, walaupun pokok terus berkurang setiap bulan.</p>
<div class="formula">Total bunga = Pokok × bunga flat per tahun × tenor (tahun)
Cicilan = (Pokok + Total bunga) ÷ tenor (bulan)</div>"""),
      ("Kenapa perlu melihat bunga efektif?", """<p>Karena bunga flat dihitung dari pokok awal, beban sebenarnya jauh lebih tinggi dari angka flat yang tertulis. <b>Bunga efektif</b> adalah suku bunga yang menghasilkan cicilan yang sama bila dihitung dari sisa pokok (seperti KPR). Sebagai gambaran, bunga flat 6% untuk 3 tahun setara bunga efektif sekitar 11% per tahun.</p>
<p>Gunakan bunga efektif untuk membandingkan penawaran leasing dengan kredit tanpa agunan (KTA) bank atau pinjaman lain.</p>"""),
      ("Biaya lain yang perlu diperhitungkan", """<ul><li>Biaya administrasi dan provisi di awal.</li><li>Asuransi kendaraan (all risk atau total loss only) yang sering dimasukkan ke cicilan.</li>
<li>Denda keterlambatan dan penalti pelunasan dipercepat.</li><li>Biaya fidusia.</li></ul>
<p>Mintalah rincian total pembayaran (total DP + seluruh cicilan + biaya) sebelum menandatangani perjanjian.</p>"""),
  ],
  faq=[("Mana yang lebih murah, DP besar atau tenor panjang?", "DP besar dan tenor pendek hampir selalu lebih murah karena total bunga dihitung dari pokok dan lamanya pinjaman."),
       ("Apakah boleh melunasi lebih cepat?", "Biasanya boleh, tetapi beberapa leasing mengenakan penalti. Karena bunga flat sudah dihitung di depan, pastikan cara perhitungan sisa bunga saat pelunasan."),
       ("Kenapa bunga efektif hampir dua kali bunga flat?", "Karena pada bunga flat Anda membayar bunga atas seluruh pokok awal sampai akhir tenor, padahal rata-rata pokok yang benar-benar Anda pinjam hanya sekitar setengahnya.")],
  sources=[("Perhitungan bunga flat dan bunga efektif (metode anuitas) yang lazim dipakai lembaga pembiayaan", "")],
  related=["kpr", "gaji-bersih", "investasi", "deposito"])

# ============================================================ deposito
C(id="deposito", slug="kalkulator-deposito", cat="investasi", icon="🏦", short="Kalkulator Deposito",
  title="Kalkulator Bunga Deposito 2026 – Bunga Bersih Setelah Pajak 20%",
  h1="Kalkulator Bunga Deposito",
  desc="Hitung bunga deposito bersih setelah PPh final 20%, hasil per periode, dan saldo akhir bila diperpanjang otomatis (ARO).",
  card="Bunga bersih setelah pajak 20% dan simulasi ARO.",
  lead="Hitung bunga deposito yang benar-benar Anda terima setelah pajak, lalu simulasikan saldo bila deposito diperpanjang otomatis (ARO) beberapa kali.",
  form=money("nominal", "Nominal deposito", "100000000") + num("bunga", "Bunga per tahun", "4", "%")
  + sel("tenorBulan", "Tenor", [(1, "1 bulan"), (3, "3 bulan"), (6, "6 bulan"), (12, "12 bulan"), (24, "24 bulan")], 12)
  + num("perpanjang", "Jumlah periode", "1", "kali", "Berapa kali deposito diperpanjang (termasuk periode pertama).")
  + '<div class="fld"><label>Perpanjangan</label>' + chk("aro", "ARO + bunga (bunga ikut didepositokan)", True) + "</div>",
  sections=[
      ("Cara menghitung bunga deposito", """<div class="formula">Bunga kotor = Nominal × bunga per tahun × tenor (bulan) ÷ 12
Pajak = 20% × bunga kotor (bila saldo di atas Rp7.500.000)
Bunga bersih = Bunga kotor − Pajak</div>
<p>Bank sebenarnya menghitung bunga berdasarkan jumlah hari, sehingga hasil di bank bisa berbeda sedikit.</p>"""),
      ("Pajak bunga deposito", """<p>Bunga deposito dikenai <b>PPh final 20%</b> yang dipotong langsung oleh bank. Bunga tidak dipotong pajak bila jumlah deposito dan tabungan Anda di bank tersebut tidak lebih dari Rp7.500.000.</p>"""),
      ("Aman tidaknya deposito: penjaminan LPS", """<p>Simpanan di bank peserta Lembaga Penjamin Simpanan (LPS) dijamin sampai <b>Rp2 miliar per nasabah per bank</b>, dengan syarat suku bunga yang Anda terima tidak melebihi <b>tingkat bunga penjaminan LPS</b> yang berlaku. Bila bunga yang ditawarkan di atas batas itu, simpanan Anda bisa tidak dijamin. Cek tingkat bunga penjaminan terbaru di situs LPS sebelum menempatkan dana.</p>"""),
      ("ARO, ARO + bunga, dan non-ARO", """<ul><li><b>ARO + bunga</b>: pokok dan bunga diperpanjang otomatis, sehingga bunga ikut berbunga (majemuk).</li>
<li><b>ARO pokok saja</b>: pokok diperpanjang, bunga dibayarkan ke rekening tabungan.</li><li><b>Non-ARO</b>: dana kembali ke tabungan saat jatuh tempo.</li></ul>
<p>Hilangkan centang ARO + bunga untuk melihat hasil bila bunga diambil setiap jatuh tempo.</p>"""),
  ],
  faq=[("Apakah bunga deposito lebih baik dari reksa dana pasar uang?", "Deposito memberi bunga pasti dan dijamin LPS (dengan syarat), tetapi dananya terkunci sampai jatuh tempo. Reksa dana pasar uang lebih fleksibel dan pajaknya berbeda, tetapi hasilnya tidak dijamin. Bandingkan hasil bersih setelah pajak."),
       ("Bagaimana jika dicairkan sebelum jatuh tempo?", "Bank biasanya mengenakan penalti atau tidak memberikan bunga untuk periode berjalan. Cek ketentuan bank Anda."),
       ("Apakah bunga deposito perlu dilaporkan di SPT?", "Ya, bunga deposito dilaporkan sebagai penghasilan yang dikenai PPh final, dan saldo deposito dilaporkan sebagai harta.")],
  sources=[("PPh final atas bunga deposito dan tabungan (PP 131/2000 dan perubahannya)", ""), ("Lembaga Penjamin Simpanan – ketentuan penjaminan simpanan", "")],
  related=["investasi", "kpr", "gaji-bersih", "thr"])

# ============================================================ investasi
C(id="investasi", slug="kalkulator-investasi", cat="investasi", icon="📈", short="Kalkulator Investasi",
  title="Kalkulator Investasi & Bunga Majemuk – Simulasi Investasi Rutin Bulanan",
  h1="Kalkulator Investasi Rutin dan Bunga Majemuk",
  desc="Simulasikan nilai investasi dari modal awal dan setoran rutin bulanan dengan imbal hasil majemuk, lengkap dengan tabel pertumbuhan per tahun.",
  card="Nilai investasi rutin bulanan dengan bunga majemuk.",
  lead="Lihat bagaimana modal awal dan setoran rutin tumbuh dengan bunga majemuk. Cocok untuk merencanakan dana pendidikan, dana pensiun, atau target rumah.",
  form=money("awal", "Modal awal", "10000000") + money("bulanan", "Setoran per bulan", "1000000") + num("imbal", "Perkiraan imbal hasil per tahun", "8", "%")
  + num("tahun", "Jangka waktu", "10", "tahun") + num("kenaikan", "Kenaikan setoran per tahun", "0", "%", "Misalnya naik 5% setiap tahun mengikuti kenaikan gaji."),
  sections=[
      ("Apa itu bunga majemuk?", """<p>Bunga majemuk berarti hasil investasi ikut diinvestasikan kembali sehingga ikut menghasilkan. Dalam jangka panjang, efeknya sangat besar: semakin lama dana diinvestasikan, semakin besar porsi hasil dibanding setoran.</p>
<div class="formula">Saldo bulan berikutnya = Saldo × (1 + i) + setoran bulanan
i = (1 + imbal hasil per tahun)^(1/12) − 1</div>"""),
      ("Memilih angka imbal hasil yang realistis", """<p>Imbal hasil tidak dijamin dan berbeda menurut jenis instrumen. Sebagai gambaran kasar (bukan janji): deposito dan reksa dana pasar uang berkisar beberapa persen per tahun, obligasi sedikit lebih tinggi, sedangkan saham dan reksa dana saham berpotensi lebih tinggi dalam jangka panjang tetapi naik-turun tajam. Gunakan beberapa skenario, misalnya pesimis, moderat, dan optimis.</p>"""),
      ("Jangan lupa inflasi", """<p>Nilai Rp100 juta 15 tahun lagi tidak setara Rp100 juta hari ini. Untuk melihat nilai riil, kurangi imbal hasil dengan perkiraan inflasi (misalnya imbal 8% dan inflasi 3% berarti sekitar 5% riil), lalu hitung ulang.</p>"""),
      ("Contoh", """<p>Modal awal Rp10.000.000 dan setoran Rp1.000.000 per bulan selama 10 tahun dengan imbal 8% per tahun. Total setoran Rp130.000.000; nilai akhir sekitar <b>Rp201,7 juta</b>, artinya sekitar Rp71,7 juta berasal dari hasil investasi.</p>"""),
  ],
  faq=[("Apakah hasil kalkulator ini dijamin?", "Tidak. Ini simulasi matematis dengan imbal hasil tetap; investasi nyata naik-turun dan bisa merugi. Gunakan sebagai alat perencanaan."),
       ("Apakah sudah termasuk pajak dan biaya?", "Belum. Masukkan imbal hasil bersih setelah biaya pengelolaan dan pajak bila ingin hasil yang lebih realistis."),
       ("Setoran di awal atau akhir bulan?", "Kalkulator ini mengasumsikan setoran di akhir setiap bulan, sehingga hasilnya sedikit konservatif.")],
  sources=[("Rumus nilai masa depan (future value) anuitas dengan bunga majemuk bulanan", "")],
  related=["deposito", "kpr", "gaji-bersih", "bpjs"])


PAGES = {
    "tentang": ("Tentang Kami", """<p><b>{name}</b> adalah kumpulan kalkulator keuangan untuk orang Indonesia: pajak gaji (PPh 21), gaji bersih, THR, iuran BPJS, KPR, kredit kendaraan, deposito, dan investasi.</p>
<p>Setiap kalkulator dibuat mengikuti aturan resmi yang berlaku, seperti PP 58/2023 dan PMK 168/2023 untuk PPh 21, UU HPP untuk tarif Pasal 17, serta ketentuan BPJS terbaru. Setiap halaman menampilkan rumus, contoh hitung, dan sumber aturannya, sehingga Anda bisa memeriksa sendiri hasilnya.</p>
<h2>Prinsip kami</h2><ul><li><b>Transparan</b>: langkah hitung selalu ditampilkan.</li><li><b>Privat</b>: semua hitungan berjalan di perangkat Anda; angka yang Anda isi tidak dikirim ke server.</li>
<li><b>Mutakhir</b>: aturan diperbarui saat ada perubahan resmi, dan tanggal pembaruan tertulis di setiap halaman.</li></ul>
<h2>Pengelola</h2><p>{name} dikembangkan oleh tim pengembang yang juga membuat <a href="https://getcomput.com" target="_blank" rel="noopener">GetComput</a>, platform belajar statistika berbahasa Indonesia.</p>
<p>Ada saran kalkulator baru atau menemukan kesalahan? <a href="/kontak/">Hubungi kami</a>.</p>"""),
    "kontak": ("Kontak", """<p>Kami senang menerima saran, laporan kesalahan, atau usulan kalkulator baru.</p>
<p>📧 Email: <a href="mailto:{email}">{email}</a></p>
<p>Agar kami bisa membantu dengan cepat, sertakan nama kalkulator, angka yang Anda masukkan, dan hasil yang menurut Anda keliru. Kami tidak dapat memberikan konsultasi pajak atau keuangan pribadi.</p>"""),
    "privasi": ("Kebijakan Privasi", """<p>Terakhir diperbarui: {updated}.</p>
<h2>Data yang Anda masukkan</h2><p>Semua kalkulator berjalan di peramban Anda. Angka yang Anda isi (gaji, harga rumah, dan lainnya) tidak dikirim ke server kami dan tidak kami simpan. Bila Anda memakai fitur “salin tautan hasil”, angka tersebut menjadi bagian dari alamat tautan yang Anda bagikan sendiri.</p>
<h2>Cookie, analitik, dan iklan</h2><p>Situs ini dapat memakai Google Analytics untuk memahami pemakaian situs secara agregat, serta menayangkan iklan pihak ketiga melalui Google AdSense. Google dan mitranya dapat menggunakan cookie atau pengenal serupa untuk menayangkan dan mengukur iklan, termasuk iklan yang dipersonalisasi berdasarkan kunjungan Anda ke situs ini dan situs lain.</p>
<p>Anda dapat mengatur personalisasi iklan di <a href="https://adssettings.google.com" target="_blank" rel="noopener">adssettings.google.com</a> dan mempelajari cara Google memakai data di <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>. Pengunjung dari wilayah yang mewajibkan persetujuan akan melihat pesan persetujuan dari Google.</p>
<h2>Kontak</h2><p>Pertanyaan tentang privasi dapat dikirim ke <a href="mailto:{email}">{email}</a>.</p>"""),
    "syarat": ("Syarat Penggunaan & Penafian", """<p>Terakhir diperbarui: {updated}.</p>
<h2>Penafian</h2><p>Semua hasil di {name} adalah <b>simulasi dan informasi umum</b>, bukan nasihat keuangan, pajak, investasi, atau hukum. Hasil dapat berbeda dari perhitungan bank, perusahaan, atau kantor pajak karena perbedaan komponen, pembulatan, kebijakan internal, atau perubahan aturan.</p>
<p>Sebelum mengambil keputusan penting, konfirmasikan kepada pihak yang berwenang, misalnya HRD, bank, konsultan pajak, atau perencana keuangan.</p>
<h2>Penggunaan</h2><p>Anda boleh memakai kalkulator ini secara gratis untuk keperluan pribadi maupun pekerjaan. Dilarang menyalin isi situs secara massal atau menggunakannya untuk menyesatkan pihak lain.</p>
<h2>Iklan dan tautan</h2><p>Situs ini dibiayai iklan. Iklan yang tampil berasal dari pihak ketiga dan bukan rekomendasi kami.</p>"""),
}
