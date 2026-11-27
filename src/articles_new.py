"""Artikel panduan baru (gelombang 3), Bahasa Indonesia. Digabung ke daftar artikel oleh build.py."""
from articles_more import T
from photos import PHOTOS

PHOTOS.update({
    "a3-pesangon": ("photo-1764231467852-b609a742e082", "Jakub Żerdzicki", "https://unsplash.com/photos/hands-signing-a-document-on-a-desk-WTgGFO_gGW8"),
    "a3-zakat": ("photo-1783227610917-4b075d028693", "Defrino Maasy", "https://unsplash.com/photos/a-hand-gives-an-indonesian-100000-rupiah-note-N9Cjgpc1PDk"),
    "a3-kta": ("photo-1633158829585-23ba8f7c8caf", "Towfiqu barbhuiya", "https://unsplash.com/photos/a-person-stacking-coins-on-top-of-a-table-jpqyfK7GB4w"),
    "a3-asuransi": ("photo-1538108149393-fbbd81895907", "Adhy Savala", "https://unsplash.com/photos/empty-hospital-bed-inside-room-zbpgmGe27p8"),
    "a3-pensiun": ("photo-1579621970795-87facc2f976d", "micheile henderson", "https://unsplash.com/photos/green-plant-in-clear-glass-vase-ZVprbBmT8QA"),
    "a3-pendidikan": ("photo-1604156425963-9be03f86a428", "Mufid Majnun", "https://unsplash.com/photos/stack-of-books-on-table-LVcjYwuHQlg"),
    "a3-sewa": ("photo-1480074568708-e7b720bb3f09", "Scott Webb", "https://unsplash.com/photos/white-house-under-maple-trees-1ddol8rgUH8"),
    "a3-freelance": ("photo-1551836022-d5d88e9218df", "Amy Hirschi", "https://unsplash.com/photos/woman-in-teal-t-shirt-sitting-beside-woman-in-suit-jacket-JaoVGh5aJ3E"),
})

TIP = lambda t: f'<div class="note info"><b>Tips:</b> {t}</div>'
NEW = []


def A(**k):
    k.setdefault("date", "27 November 2026")
    NEW.append(k)


A(slug="cara-menghitung-pesangon", calc="gaji-bersih", img="gaji-bersih", photo="a3-pesangon",
  title="Cara Menghitung Pesangon Sesuai PP 35/2021: Rumus, Tabel, dan Pajaknya",
  h1="Cara Menghitung Pesangon Karyawan",
  desc="Panduan menghitung pesangon, uang penghargaan masa kerja, dan uang penggantian hak sesuai PP 35/2021, lengkap dengan tabel, contoh, faktor pengali menurut alasan PHK, dan pajak pesangon.",
  lead="Pemutusan hubungan kerja (PHK) bisa terjadi pada siapa saja. Pahami hak Anda agar tidak dirugikan saat menerima pesangon.",
  body=[
      ("Tiga komponen hak saat PHK", """<p>Menurut UU Ketenagakerjaan sebagaimana diubah UU Cipta Kerja, serta aturan pelaksananya <b>PP 35/2021</b>, pekerja yang terkena PHK dapat berhak atas tiga komponen:</p>
<ul><li><b>Uang pesangon (UP)</b>, besarnya tergantung masa kerja.</li>
<li><b>Uang penghargaan masa kerja (UPMK)</b>, untuk masa kerja minimal 3 tahun.</li>
<li><b>Uang penggantian hak (UPH)</b>, misalnya cuti tahunan yang belum diambil dan belum gugur, serta biaya pulang ke tempat asal bagi pekerja dan keluarganya.</li></ul>
<p>Dasar perhitungannya adalah <b>upah sebulan</b>, yaitu gaji pokok ditambah tunjangan tetap, bukan termasuk lembur atau tunjangan tidak tetap.</p>"""),
      ("Tabel uang pesangon dan UPMK", T(["Masa kerja", "Uang pesangon"], [
          ["Kurang dari 1 tahun", "1 bulan upah"], ["1 sampai kurang dari 2 tahun", "2 bulan upah"], ["2 sampai kurang dari 3 tahun", "3 bulan upah"],
          ["3 sampai kurang dari 4 tahun", "4 bulan upah"], ["4 sampai kurang dari 5 tahun", "5 bulan upah"], ["5 sampai kurang dari 6 tahun", "6 bulan upah"],
          ["6 sampai kurang dari 7 tahun", "7 bulan upah"], ["7 sampai kurang dari 8 tahun", "8 bulan upah"], ["8 tahun atau lebih", "9 bulan upah"]])
       + T(["Masa kerja", "UPMK"], [
          ["3 sampai kurang dari 6 tahun", "2 bulan upah"], ["6 sampai kurang dari 9 tahun", "3 bulan upah"], ["9 sampai kurang dari 12 tahun", "4 bulan upah"],
          ["12 sampai kurang dari 15 tahun", "5 bulan upah"], ["15 sampai kurang dari 18 tahun", "6 bulan upah"], ["18 sampai kurang dari 21 tahun", "7 bulan upah"],
          ["21 sampai kurang dari 24 tahun", "8 bulan upah"], ["24 tahun atau lebih", "10 bulan upah"]])),
      ("Faktor pengali menurut alasan PHK", """<p>Besar pesangon akhir tidak selalu sama dengan tabel di atas. PP 35/2021 menetapkan <b>pengali</b> berbeda menurut alasan PHK. Beberapa contoh:</p>
<ul><li><b>Efisiensi untuk mencegah kerugian</b>: 1 kali uang pesangon, ditambah UPMK dan UPH.</li>
<li><b>Efisiensi karena perusahaan mengalami kerugian</b>: 0,5 kali uang pesangon, ditambah UPMK dan UPH.</li>
<li><b>Pekerja memasuki usia pensiun</b>: 1,75 kali uang pesangon, ditambah UPMK dan UPH.</li>
<li><b>Pekerja meninggal dunia</b>: 2 kali uang pesangon kepada ahli waris, ditambah UPMK dan UPH.</li>
<li><b>Mengundurkan diri atas kemauan sendiri</b>: tidak mendapat pesangon dan UPMK, tetapi berhak atas UPH dan uang pisah yang besarnya diatur dalam perjanjian kerja atau peraturan perusahaan.</li></ul>
<p>Masih ada alasan lain, seperti perusahaan tutup, pailit, merger, atau pelanggaran berat, masing-masing dengan ketentuan sendiri. Perjanjian kerja bersama juga boleh mengatur nilai yang lebih menguntungkan pekerja. Bila ragu, konsultasikan ke dinas ketenagakerjaan setempat atau serikat pekerja.</p>"""),
      ("Contoh perhitungan", """<p>Karyawan tetap dengan upah <b>Rp8.000.000</b> dan masa kerja <b>7 tahun 4 bulan</b> terkena PHK karena efisiensi untuk mencegah kerugian. Sisa cuti tahunan 6 hari.</p>""" + T(["Komponen", "Perhitungan", "Jumlah"], [
          ["Uang pesangon (masa kerja 7–8 tahun)", "1 × 8 × Rp8.000.000", "Rp64.000.000"], ["UPMK (masa kerja 6–9 tahun)", "3 × Rp8.000.000", "Rp24.000.000"],
          ["UPH cuti (6 hari)", "6/25 × Rp8.000.000 (asumsi pembagi 25 hari kerja)", "Rp1.920.000"], ["=Total sebelum pajak", "", "Rp89.920.000"]]) + """
<p>Pembagi untuk menghitung upah harian bisa berbeda tergantung pola kerja dan kebijakan perusahaan, jadi angka UPH dapat sedikit berbeda.</p>"""),
      ("Pajak atas pesangon", """<p>Pesangon, UPMK, dan UPH yang dibayar sekaligus dikenai <b>PPh 21 final</b> dengan tarif berlapis atas jumlah bruto:</p>""" + T(["Lapisan penghasilan", "Tarif"], [
          ["Sampai Rp50 juta", "0%"], ["Di atas Rp50 juta sampai Rp100 juta", "5%"], ["Di atas Rp100 juta sampai Rp500 juta", "15%"], ["Di atas Rp500 juta", "25%"]]) + """
<p>Pada contoh di atas, total Rp89.920.000 dikenai pajak: Rp50 juta pertama 0%, dan Rp39.920.000 berikutnya 5% atau Rp1.996.000. Pesangon bersih yang diterima sekitar <b>Rp87.924.000</b>. Karena final, pesangon tidak digabung dengan gaji saat menghitung pajak setahun.</p>"""),
      ("Tips menghadapi PHK", "<ul>"
       "<li><b>Minta perhitungan tertulis</b> dari perusahaan dan cocokkan dengan tabel serta alasan PHK.</li>"
       "<li><b>Pastikan dasar upah benar</b>: gaji pokok ditambah tunjangan tetap.</li>"
       "<li><b>Jangan buru-buru menandatangani</b> kesepakatan bila ada yang belum jelas. Anda berhak berunding (bipartit).</li>"
       "<li><b>Urus JKP dan JHT</b> di BPJS Ketenagakerjaan. JKP hanya untuk korban PHK dan ada batas waktu pengajuannya.</li>"
       "<li><b>Kelola pesangon dengan bijak</b>: sisihkan untuk dana darurat beberapa bulan, lunasi utang berbunga tinggi, baru pertimbangkan investasi atau usaha.</li>"
       "<li><b>Minta surat keterangan kerja (paklaring)</b> dan bukti potong pajak untuk keperluan pekerjaan berikutnya dan SPT.</li></ul>"
       + TIP("hitung juga gaji bersih di pekerjaan berikutnya dengan kalkulator gaji bersih, agar rencana keuangan setelah PHK lebih realistis.")),
      ("Kesimpulan", """<p>Pesangon terdiri dari uang pesangon, UPMK, dan UPH, dengan besaran yang ditentukan masa kerja dan alasan PHK. Hitung dengan upah yang benar, periksa faktor pengalinya, dan perhitungkan pajak final agar Anda tahu angka bersih yang akan diterima. Dengan persiapan yang baik, pesangon bisa menjadi jembatan menuju pekerjaan atau usaha berikutnya.</p>"""),
  ],
  faq=[("Apakah karyawan kontrak mendapat pesangon?", "Karyawan PKWT tidak mendapat pesangon, tetapi berhak atas uang kompensasi saat kontrak berakhir bila masa kerja minimal 1 bulan, sebesar masa kerja dibagi 12 dikali upah sebulan."),
       ("Apakah pesangon bisa dicicil?", "Pembayaran pesangon idealnya sekaligus. Bila ada kesepakatan lain, pastikan tertulis dan tidak merugikan pekerja."),
       ("Apakah pesangon memengaruhi klaim JHT?", "Tidak. Pesangon dibayar perusahaan, sedangkan JHT adalah saldo Anda di BPJS Ketenagakerjaan. Keduanya hak yang terpisah.")])

A(slug="cara-menghitung-zakat-penghasilan", calc="gaji-bersih", img="gaji-bersih", photo="a3-zakat",
  title="Cara Menghitung Zakat Penghasilan (Zakat Profesi): Nisab, Kadar, dan Contohnya",
  h1="Cara Menghitung Zakat Penghasilan",
  desc="Panduan zakat penghasilan atau zakat profesi: pengertian, nisab setara 85 gram emas, kadar 2,5%, cara menghitung bulanan dan tahunan, serta zakat sebagai pengurang pajak.",
  lead="Bagi umat Islam, zakat penghasilan adalah kewajiban atas gaji dan pendapatan lain yang telah mencapai nisab. Berikut cara menghitungnya.",
  body=[
      ("Apa itu zakat penghasilan?", """<p><b>Zakat penghasilan</b>, sering disebut zakat profesi, adalah zakat yang dikeluarkan dari penghasilan seperti gaji, honor, upah, dan pendapatan jasa lainnya. Di Indonesia, panduan perhitungannya mengacu pada fatwa MUI dan ketentuan BAZNAS sebagai badan resmi pengelola zakat.</p>
<p>Zakat ini wajib bila penghasilan telah mencapai <b>nisab</b>, yaitu batas minimal tertentu, dengan <b>kadar 2,5%</b>. Banyak orang membayarnya setiap bulan saat menerima gaji agar lebih ringan dan teratur.</p>"""),
      ("Nisab dan kadar zakat", """<p>Nisab zakat penghasilan setara dengan nilai <b>85 gram emas per tahun</b>. Karena harga emas berubah, nilai nisab dalam rupiah juga berubah. BAZNAS biasanya mengumumkan nilai nisab yang dipakai sebagai acuan.</p>
<div class="formula">Nisab per tahun  = 85 gram × harga emas per gram
Nisab per bulan  = nisab per tahun ÷ 12
Zakat            = 2,5% × penghasilan (bila ≥ nisab)</div>
<p>Contoh dengan asumsi harga emas Rp2.000.000 per gram (hanya ilustrasi): nisab per tahun Rp170.000.000, atau sekitar <b>Rp14.166.667 per bulan</b>.</p>"""),
      ("Contoh perhitungan", T(["Kondisi", "Penghasilan per bulan", "Mencapai nisab?", "Zakat per bulan"], [
          ["Karyawan A", "Rp10.000.000", "Tidak (di bawah Rp14,17 juta)", "Tidak wajib, dianjurkan berinfak"],
          ["Karyawan B", "Rp15.000.000", "Ya", "2,5% × Rp15.000.000 = Rp375.000"],
          ["Karyawan C", "Rp25.000.000", "Ya", "2,5% × Rp25.000.000 = Rp625.000"]]) + """
<p>Ada perbedaan pandangan apakah zakat dihitung dari penghasilan kotor atau setelah dikurangi kebutuhan pokok. Panduan BAZNAS umumnya menggunakan penghasilan bruto. Bila ragu, ikuti panduan lembaga amil zakat tempat Anda membayar atau konsultasikan dengan ahlinya.</p>"""),
      ("Zakat sebagai pengurang pajak", """<p>Zakat yang dibayarkan melalui <b>badan atau lembaga amil zakat resmi</b> yang disahkan pemerintah dapat menjadi pengurang penghasilan bruto dalam perhitungan pajak, sesuai ketentuan perpajakan. Syaratnya, ada bukti setor yang sah, misalnya Bukti Setor Zakat (BSZ) dengan identitas pembayar.</p>
<p>Bila zakat dipotong langsung oleh perusahaan dari gaji dan disetorkan ke lembaga resmi, pengurangan ini dapat diperhitungkan dalam PPh 21. Bila dibayar sendiri, simpan buktinya untuk dilaporkan dalam SPT Tahunan. Zakat yang diberikan langsung kepada penerima tanpa melalui lembaga resmi tidak dapat menjadi pengurang pajak, walaupun tetap sah secara agama.</p>"""),
      ("Tips menunaikan zakat penghasilan", "<ul>"
       "<li><b>Hitung saat gajian</b> dan langsung sisihkan sebelum dipakai untuk kebutuhan lain.</li>"
       "<li><b>Gunakan lembaga resmi</b> agar penyaluran tepat sasaran dan buktinya dapat dipakai untuk pajak.</li>"
       "<li><b>Masukkan zakat ke anggaran</b> sebagai pos tersendiri di awal, sebelum membagi sisa penghasilan.</li>"
       "<li><b>Perhatikan penghasilan tidak rutin</b> seperti bonus, THR, dan honor; zakat juga dihitung atas penghasilan tersebut bila mencapai nisab.</li>"
       "<li><b>Simpan bukti setor</b> untuk keperluan SPT Tahunan.</li></ul>"
       + TIP("cek gaji bersih Anda dengan kalkulator gaji bersih untuk menyusun anggaran yang sudah memasukkan zakat.")),
      ("Kesimpulan", """<p>Zakat penghasilan dihitung 2,5% dari penghasilan yang mencapai nisab setara 85 gram emas per tahun. Menunaikannya setiap bulan melalui lembaga resmi membuatnya lebih ringan, tertib, dan dapat menjadi pengurang penghasilan dalam perhitungan pajak. Jadikan zakat pos pertama dalam anggaran agar tidak terlewat.</p>"""),
  ],
  faq=[("Apakah zakat penghasilan sama dengan zakat fitrah?", "Berbeda. Zakat fitrah dibayar setahun sekali menjelang Idulfitri per jiwa, sedangkan zakat penghasilan dihitung dari pendapatan."),
       ("Bagaimana bila penghasilan berubah-ubah?", "Anda bisa menjumlahkan penghasilan setahun dan membandingkannya dengan nisab tahunan, lalu membayar 2,5% dari totalnya."),
       ("Apakah zakat boleh dibayar lewat aplikasi?", "Boleh, selama melalui kanal resmi lembaga amil zakat yang berizin, sehingga bukti setornya sah.")])

A(slug="panduan-kta-kredit-tanpa-agunan", calc="kredit-kendaraan", img="kredit-kendaraan", photo="a3-kta",
  title="Panduan KTA (Kredit Tanpa Agunan): Cara Kerja, Bunga, Syarat, dan Tips Memilih",
  h1="Panduan KTA: Kredit Tanpa Agunan dari Bank",
  desc="Pengertian KTA, cara menghitung bunga flat dan efektif, syarat pengajuan, biaya provisi dan asuransi, perbandingan dengan pinjaman lain, serta tips memakai KTA dengan aman.",
  lead="KTA bisa menjadi solusi dana cepat tanpa jaminan, tetapi bunganya tidak kecil. Pahami cara kerjanya sebelum mengajukan.",
  body=[
      ("Apa itu KTA?", """<p><b>Kredit Tanpa Agunan (KTA)</b> adalah pinjaman dari bank yang tidak memerlukan jaminan seperti rumah atau kendaraan. Persetujuannya didasarkan pada penghasilan, riwayat kredit, dan kemampuan bayar. Plafonnya biasanya beberapa kali gaji bulanan, dengan tenor 1 sampai 5 tahun dan cicilan tetap setiap bulan.</p>
<p>Karena tanpa jaminan, risiko bagi bank lebih besar, sehingga bunga KTA lebih tinggi daripada KPR atau kredit dengan agunan, tetapi umumnya lebih rendah daripada kartu kredit yang tidak dilunasi atau pinjaman daring jangka pendek.</p>"""),
      ("Bunga flat per bulan dan bunga efektif", """<p>Bunga KTA sering ditawarkan dalam bentuk <b>flat per bulan</b>, misalnya 1% per bulan. Angka ini terlihat kecil, padahal setara bunga efektif yang jauh lebih tinggi.</p>""" + T(["Rincian", "Jumlah"], [
          ["Pinjaman", "Rp50.000.000"], ["Tenor", "36 bulan"], ["Bunga flat 1% per bulan (12% per tahun)", "Rp500.000 × 36 = Rp18.000.000"],
          ["Cicilan per bulan", "Rp1.888.889"], ["=Bunga efektif setara", "sekitar 21,2% per tahun"]]) + """
<p>Selalu ubah penawaran ke bunga efektif sebelum membandingkan dengan pinjaman lain. Prinsip perhitungannya sama dengan kredit kendaraan bunga flat.</p>"""),
      ("Syarat dan biaya", """<ul><li><b>Syarat umum</b>: WNI, usia minimal 21 tahun, penghasilan minimal sesuai ketentuan bank, masa kerja tertentu, KTP, NPWP, slip gaji atau rekening koran.</li>
<li><b>Riwayat kredit</b> di SLIK OJK harus baik.</li>
<li><b>Biaya provisi</b>, biasanya persentase dari plafon dan dipotong saat pencairan.</li>
<li><b>Biaya administrasi</b> dan kadang <b>asuransi jiwa kredit</b>.</li>
<li><b>Denda keterlambatan</b> dan <b>penalti pelunasan dipercepat</b>.</li></ul>
<p>Perhatikan bahwa dana yang Anda terima bisa lebih kecil dari plafon karena biaya provisi dan administrasi dipotong di awal.</p>"""),
      ("Kapan KTA masuk akal?", """<ul><li><b>Melunasi utang yang lebih mahal</b>, misalnya tagihan kartu kredit yang menumpuk atau pinjaman daring, sehingga total bunga turun (konsolidasi utang).</li>
<li><b>Kebutuhan penting dan terencana</b> seperti biaya pendidikan atau renovasi mendesak, bila tidak ada sumber dana yang lebih murah.</li>
<li><b>Modal usaha</b> yang perhitungan arus kasnya jelas dan mampu menutup cicilan.</li></ul>
<p>KTA kurang tepat untuk gaya hidup, liburan, atau barang konsumtif yang nilainya cepat turun.</p>"""),
      ("Tips memakai KTA dengan aman", "<ul>"
       "<li><b>Pinjam secukupnya</b>, bukan sebesar plafon yang ditawarkan.</li>"
       "<li><b>Pastikan total cicilan</b> semua utang tidak melebihi 30% penghasilan.</li>"
       "<li><b>Bandingkan beberapa bank</b> dari bunga efektif, provisi, dan penalti.</li>"
       "<li><b>Pilih tenor pendek</b> bila cicilan masih nyaman, agar total bunga lebih kecil.</li>"
       "<li><b>Waspadai penawaran lewat telepon atau pesan</b> yang meminta data pribadi atau biaya di muka. Ajukan langsung melalui kanal resmi bank.</li></ul>"
       + TIP("hitung bunga efektif dari penawaran bunga flat menggunakan simulasi kredit kendaraan; masukkan DP 0% dan bunga flat per tahun.")),
      ("Kesimpulan", """<p>KTA memberi akses dana tanpa jaminan dengan cicilan tetap, tetapi bunganya relatif tinggi dan sering ditulis sebagai bunga flat per bulan. Hitung bunga efektif, perhitungkan semua biaya, dan gunakan KTA untuk kebutuhan penting atau untuk mengganti utang yang lebih mahal, bukan untuk konsumsi.</p>"""),
  ],
  faq=[("Berapa lama proses KTA?", "Bervariasi, dari beberapa hari sampai dua minggu, tergantung kelengkapan dokumen dan bank. Beberapa bank menawarkan proses digital yang lebih cepat."),
       ("Apakah KTA bisa dilunasi lebih cepat?", "Bisa, umumnya dengan penalti tertentu. Tanyakan cara perhitungan sisa bunga saat pelunasan."),
       ("Apakah wiraswasta bisa mengajukan KTA?", "Bisa, dengan dokumen usaha dan rekening koran sebagai bukti penghasilan. Syaratnya biasanya lebih ketat.")])

A(slug="asuransi-kesehatan-swasta-vs-bpjs", calc="bpjs", img="bpjs", photo="a3-asuransi",
  title="Asuransi Kesehatan Swasta vs BPJS Kesehatan: Perbedaan dan Cara Memilih",
  h1="Asuransi Kesehatan Swasta atau BPJS Kesehatan?",
  desc="Perbandingan BPJS Kesehatan dan asuransi kesehatan swasta: cakupan, premi, sistem rujukan, jenis plan, istilah penting seperti masa tunggu dan limit, serta cara memilih yang tepat.",
  lead="BPJS Kesehatan wajib dimiliki, sedangkan asuransi swasta bersifat tambahan. Kapan Anda butuh keduanya, dan bagaimana memilihnya?",
  body=[
      ("Peran BPJS Kesehatan", """<p>BPJS Kesehatan adalah program jaminan kesehatan nasional yang wajib bagi seluruh penduduk. Kelebihannya: iuran relatif terjangkau, cakupan layanan luas termasuk penyakit kronis dan berbiaya besar, serta tidak ada pengecualian kondisi yang sudah ada sebelumnya. Layanannya mengikuti <b>sistem rujukan berjenjang</b>, dimulai dari fasilitas kesehatan tingkat pertama.</p>
<p>Keterbatasannya biasanya terkait antrean, pilihan rumah sakit dan dokter, serta kenyamanan ruang rawat. Di sinilah asuransi swasta sering dipertimbangkan sebagai pelengkap.</p>"""),
      ("Perbandingan singkat", T(["Aspek", "BPJS Kesehatan", "Asuransi swasta"], [
          ["Sifat", "Wajib", "Sukarela"], ["Biaya", "Iuran tetap atau persentase upah", "Premi tergantung usia, plan, dan kondisi kesehatan"],
          ["Akses layanan", "Rujukan berjenjang", "Umumnya langsung ke rumah sakit rekanan"], ["Kondisi yang sudah ada", "Ditanggung", "Sering dikecualikan atau ada masa tunggu"],
          ["Batas manfaat", "Sesuai paket layanan", "Ada limit tahunan atau per jenis biaya"], ["Kenyamanan", "Sesuai kelas atau standar ruang", "Bisa memilih kamar dan rumah sakit"]])),
      ("Istilah penting di polis asuransi kesehatan", """<ul><li><b>Masa tunggu</b>: periode awal ketika penyakit tertentu belum ditanggung, misalnya 30 hari untuk penyakit umum dan 12 bulan untuk penyakit tertentu.</li>
<li><b>Pre-existing condition</b>: penyakit yang sudah ada sebelum polis dimulai; sering dikecualikan.</li>
<li><b>Limit tahunan</b> dan <b>inner limit</b>: batas total per tahun dan batas per jenis biaya (kamar, operasi, obat).</li>
<li><b>As charged</b>: biaya ditanggung sesuai tagihan sampai batas tahunan, tanpa batas per jenis biaya.</li>
<li><b>Cashless</b> dan <b>reimbursement</b>: dibayar langsung oleh asuransi di rumah sakit rekanan, atau Anda bayar dulu lalu mengajukan penggantian.</li>
<li><b>Koordinasi manfaat (COB)</b>: kerja sama dengan BPJS Kesehatan, sehingga sebagian biaya ditanggung BPJS dan selisihnya oleh asuransi swasta.</li></ul>"""),
      ("Cara memilih", """<ol><li><b>Pastikan BPJS Kesehatan aktif lebih dulu</b>, sebagai perlindungan dasar.</li>
<li><b>Cek asuransi dari kantor</b>. Banyak perusahaan sudah memberikan asuransi kesehatan; pelajari cakupannya sebelum membeli sendiri.</li>
<li><b>Tentukan kebutuhan</b>: rawat inap saja, atau juga rawat jalan, gigi, dan melahirkan.</li>
<li><b>Bandingkan manfaat, bukan hanya premi</b>: limit, daftar rumah sakit, pengecualian, dan masa tunggu.</li>
<li><b>Hindari mencampur proteksi dan investasi</b> bila tujuan utama Anda perlindungan; asuransi murni biasanya memberi manfaat lebih besar untuk premi yang sama.</li>
<li><b>Pilih perusahaan yang diawasi OJK</b> dan memiliki reputasi klaim yang baik.</li></ol>"""),
      ("Tips agar klaim lancar", "<ul>"
       "<li><b>Isi formulir kesehatan dengan jujur</b>. Informasi yang tidak benar bisa membuat klaim ditolak.</li>"
       "<li><b>Simpan polis dan kartu peserta</b> di tempat yang mudah dijangkau keluarga.</li>"
       "<li><b>Pahami prosedur rawat inap</b>: kapan harus menghubungi asuransi dan dokumen apa yang dibutuhkan.</li>"
       "<li><b>Bayar premi tepat waktu</b> agar polis tidak lapse.</li>"
       "<li><b>Tinjau ulang polis</b> setiap beberapa tahun karena kebutuhan dan biaya kesehatan berubah.</li></ul>"
       + TIP("hitung iuran BPJS Kesehatan yang sudah Anda bayar lewat kalkulator iuran BPJS sebelum memutuskan berapa anggaran untuk asuransi tambahan.")),
      ("Kesimpulan", """<p>BPJS Kesehatan adalah fondasi perlindungan kesehatan yang wajib dan relatif terjangkau. Asuransi swasta bisa menjadi pelengkap untuk akses dan kenyamanan yang lebih baik, asalkan Anda memahami limit, masa tunggu, dan pengecualiannya. Pilih berdasarkan kebutuhan keluarga dan kemampuan membayar premi dalam jangka panjang.</p>"""),
  ],
  faq=[("Apakah perlu asuransi swasta bila sudah ada BPJS?", "Tidak wajib. Asuransi swasta berguna bila Anda menginginkan akses lebih cepat, pilihan rumah sakit lebih luas, atau kenyamanan tambahan, dan premi tidak membebani anggaran."),
       ("Apakah premi akan naik?", "Premi umumnya naik seiring bertambahnya usia dan biaya kesehatan. Periksa ketentuan perpanjangan di polis."),
       ("Apa itu asuransi unit link?", "Produk yang menggabungkan proteksi dan investasi. Pahami biaya dan risikonya; bagi banyak orang, memisahkan asuransi murni dan investasi lebih transparan.")])

A(slug="merencanakan-dana-pensiun", calc="investasi", img="investasi", photo="a3-pensiun",
  title="Merencanakan Dana Pensiun: Berapa yang Dibutuhkan dan Cara Mengumpulkannya",
  h1="Merencanakan Dana Pensiun Sejak Dini",
  desc="Cara menghitung kebutuhan dana pensiun, peran JHT dan JP BPJS, pilihan DPLK dan investasi, contoh hitungan setoran bulanan, dan tips agar masa pensiun lebih tenang.",
  lead="Pensiun mungkin terasa masih jauh, tetapi justru itulah alasan terbaik untuk mulai sekarang. Waktu adalah modal terbesar dana pensiun.",
  body=[
      ("Kenapa dana pensiun perlu direncanakan", """<p>Saat pensiun, gaji berhenti tetapi kebutuhan hidup tetap berjalan, bahkan biaya kesehatan cenderung naik. Harapan hidup juga semakin panjang, sehingga masa pensiun bisa berlangsung 20 tahun atau lebih. Mengandalkan anak atau hanya mengandalkan program wajib sering tidak cukup.</p>
<p>Patokan umum, kebutuhan biaya hidup saat pensiun sekitar <b>70–80% dari pengeluaran</b> menjelang pensiun, karena beberapa biaya seperti transportasi kerja dan cicilan rumah biasanya sudah berkurang.</p>"""),
      ("Sumber dana pensiun di Indonesia", """<ul><li><b>JHT BPJS Ketenagakerjaan</b>: saldo tabungan yang dicairkan saat pensiun.</li>
<li><b>JP BPJS Ketenagakerjaan</b>: pensiun bulanan bila masa iuran minimal 15 tahun.</li>
<li><b>Program pensiun dari perusahaan</b>, bila ada, seperti DPPK atau pesangon karena pensiun.</li>
<li><b>DPLK (Dana Pensiun Lembaga Keuangan)</b>: program pensiun sukarela yang bisa diikuti perorangan, dengan manfaat pajak tertentu.</li>
<li><b>Investasi pribadi</b>: reksa dana, SBN, saham, dan properti.</li></ul>
<p>Program wajib umumnya hanya menutup sebagian kebutuhan. Sisanya perlu dikumpulkan sendiri.</p>"""),
      ("Contoh menghitung kebutuhan", """<p>Misalkan Anda berusia 25 tahun dan ingin pensiun di usia 55 dengan biaya hidup setara <b>Rp7 juta per bulan dalam nilai uang sekarang</b>, selama sekitar 25 tahun masa pensiun.</p>""" + T(["Langkah", "Perhitungan", "Hasil"], [
          ["Kebutuhan setahun (nilai sekarang)", "12 × Rp7 juta", "Rp84 juta"], ["Dana yang dibutuhkan saat pensiun (nilai sekarang)", "Rp84 juta × 25 tahun", "sekitar Rp2,1 miliar"],
          ["Setara nilai uang 30 tahun lagi (inflasi 4%)", "Rp7 juta × 1,04³⁰ per bulan", "sekitar Rp22,7 juta per bulan"],
          ["=Setoran bulanan bila imbal riil 4%", "dihitung dengan rumus nilai masa depan", "sekitar Rp3,06 juta (nilai sekarang, naik mengikuti inflasi)"]]) + """
<p>Angka ini terlihat besar, tetapi sebagian akan ditutup oleh JHT, JP, dan program kantor. Hitungan ini juga sangat bergantung pada asumsi, jadi gunakan sebagai gambaran, lalu tinjau ulang setiap beberapa tahun.</p>"""),
      ("Strategi mengumpulkan dana pensiun", """<ul><li><b>Mulai sedini mungkin</b>, walaupun kecil. Setiap 10 tahun penundaan bisa melipatgandakan setoran yang dibutuhkan.</li>
<li><b>Naikkan setoran setiap tahun</b> mengikuti kenaikan gaji.</li>
<li><b>Gunakan instrumen pertumbuhan</b> seperti reksa dana saham untuk jangka panjang, lalu geser bertahap ke instrumen yang lebih stabil menjelang pensiun.</li>
<li><b>Jangan mencairkan JHT</b> setiap pindah kerja bila tidak mendesak.</li>
<li><b>Lunasi utang</b> sebelum pensiun, terutama KPR.</li>
<li><b>Siapkan perlindungan kesehatan</b> agar tabungan pensiun tidak habis untuk biaya berobat.</li></ul>"""),
      ("Tips agar masa pensiun lebih tenang", "<ul>"
       "<li><b>Tentukan gaya hidup pensiun</b> yang realistis sejak sekarang.</li>"
       "<li><b>Pisahkan rekening dana pensiun</b> dari tabungan lain agar tidak terpakai.</li>"
       "<li><b>Tinjau rencana setiap 2–3 tahun</b> dan sesuaikan dengan perubahan penghasilan dan kebutuhan.</li>"
       "<li><b>Pertimbangkan penghasilan pasif</b> atau keahlian yang bisa tetap menghasilkan setelah pensiun.</li>"
       "<li><b>Waspadai investasi bodong</b> yang menyasar pensiunan dengan janji hasil tinggi.</li></ul>"
       + TIP("simulasikan setoran bulanan dan kenaikan setoran tahunan di kalkulator investasi untuk melihat perkiraan dana di usia pensiun.")),
      ("Kesimpulan", """<p>Dana pensiun yang cukup dibangun dari kombinasi program wajib, program kantor, dan investasi pribadi yang dimulai sejak dini. Hitung kebutuhan dengan memperhitungkan inflasi, mulai menyetor secara rutin, naikkan setoran seiring penghasilan, dan tinjau rencana secara berkala. Semakin awal dimulai, semakin ringan bebannya.</p>"""),
  ],
  faq=[("Apakah JHT dan JP cukup untuk pensiun?", "Untuk kebanyakan orang tidak cukup. Keduanya adalah fondasi, sedangkan sisanya perlu disiapkan lewat investasi pribadi atau program pensiun sukarela."),
       ("Kapan sebaiknya mulai menyiapkan dana pensiun?", "Sejak mulai bekerja. Bahkan setoran kecil di usia 20-an bisa tumbuh besar berkat bunga majemuk."),
       ("Apa itu DPLK?", "Dana Pensiun Lembaga Keuangan, program pensiun sukarela yang dikelola bank atau perusahaan asuransi dan diawasi OJK.")])

A(slug="menyiapkan-dana-pendidikan-anak", calc="investasi", img="investasi", photo="a3-pendidikan",
  title="Cara Menyiapkan Dana Pendidikan Anak: Hitung Kebutuhan dan Pilih Instrumennya",
  h1="Cara Menyiapkan Dana Pendidikan Anak",
  desc="Panduan menyiapkan dana pendidikan anak: menghitung biaya masa depan dengan inflasi pendidikan, contoh setoran bulanan, memilih instrumen sesuai jangka waktu, dan tips agar target tercapai.",
  lead="Biaya pendidikan terus naik dari tahun ke tahun. Dengan perencanaan sejak dini, beban biaya sekolah dan kuliah anak bisa jauh lebih ringan.",
  body=[
      ("Kenapa harus disiapkan sejak dini", """<p>Biaya pendidikan, terutama uang pangkal dan biaya kuliah, cenderung naik lebih cepat daripada inflasi umum. Kebutuhan dana pendidikan juga datang pada waktu yang sudah bisa diperkirakan, sehingga sangat cocok direncanakan dengan investasi rutin.</p>
<p>Semakin panjang jangka waktunya, semakin besar peran bunga majemuk, dan semakin kecil setoran bulanan yang dibutuhkan.</p>"""),
      ("Contoh menghitung kebutuhan", """<p>Misalkan biaya kuliah empat tahun di perguruan tinggi incaran saat ini sekitar <b>Rp100 juta</b>, anak berusia 0 tahun dan akan kuliah 18 tahun lagi. Dengan asumsi kenaikan biaya pendidikan 8% per tahun:</p>""" + T(["Langkah", "Perhitungan", "Hasil"], [
          ["Biaya saat ini", "", "Rp100 juta"], ["Biaya 18 tahun lagi", "Rp100 juta × 1,08¹⁸", "sekitar Rp400 juta"],
          ["=Setoran bulanan bila imbal 8% per tahun", "rumus nilai masa depan", "sekitar Rp858 ribu per bulan"]]) + """
<p>Bila baru mulai saat anak berusia 8 tahun (10 tahun sebelum kuliah), setoran yang dibutuhkan bisa beberapa kali lipat lebih besar. Asumsi kenaikan biaya dan imbal hasil hanyalah contoh; cari informasi biaya terbaru dari sekolah atau kampus yang dituju.</p>"""),
      ("Memilih instrumen sesuai jangka waktu", T(["Jarak ke kebutuhan", "Instrumen yang umum dipilih", "Alasan"], [
          ["Lebih dari 10 tahun", "Reksa dana saham, saham, sebagian reksa dana campuran", "Potensi pertumbuhan tinggi, ada waktu untuk pulih dari penurunan"],
          ["5–10 tahun", "Reksa dana campuran, pendapatan tetap, SBN", "Keseimbangan pertumbuhan dan stabilitas"],
          ["Kurang dari 5 tahun", "SBN, reksa dana pendapatan tetap atau pasar uang, deposito", "Menjaga nilai dana menjelang dipakai"],
          ["Kurang dari 1 tahun", "Reksa dana pasar uang, deposito, tabungan", "Dana harus aman dan siap dicairkan"]]) + """
<p>Prinsipnya, makin dekat waktu kebutuhan, makin besar porsi instrumen yang stabil. Pindahkan dana secara bertahap, bukan sekaligus di menit terakhir.</p>"""),
      ("Strategi agar target tercapai", """<ul><li><b>Pisahkan dana per jenjang</b>: SD, SMP, SMA, dan kuliah memiliki waktu kebutuhan berbeda.</li>
<li><b>Otomatiskan setoran</b> setiap gajian agar konsisten.</li>
<li><b>Manfaatkan penghasilan tambahan</b> seperti bonus dan THR untuk mempercepat.</li>
<li><b>Lindungi pencari nafkah</b> dengan asuransi jiwa murni agar rencana tetap berjalan bila terjadi risiko.</li>
<li><b>Evaluasi setiap tahun</b>: sesuaikan target bila biaya sekolah naik lebih cepat dari perkiraan.</li></ul>"""),
      ("Tips menyiapkan dana pendidikan", "<ul>"
       "<li><b>Riset biaya nyata</b> sekolah atau kampus incaran, termasuk uang pangkal dan biaya hidup bila di luar kota.</li>"
       "<li><b>Jangan memakai dana pendidikan</b> untuk keperluan lain.</li>"
       "<li><b>Hati-hati dengan produk yang menjanjikan hasil pasti tinggi.</b></li>"
       "<li><b>Libatkan pasangan</b> dalam menentukan target dan pilihan sekolah.</li>"
       "<li><b>Siapkan rencana cadangan</b> seperti beasiswa atau pilihan kampus alternatif.</li></ul>"
       + TIP("gunakan kalkulator investasi untuk mencoba beberapa skenario imbal hasil dan menemukan setoran bulanan yang realistis.")),
      ("Kesimpulan", """<p>Dana pendidikan anak bisa disiapkan dengan tenang bila dihitung sejak awal: perkirakan biaya masa depan dengan inflasi pendidikan, tentukan setoran bulanan, pilih instrumen sesuai jangka waktu, dan pindahkan secara bertahap ke instrumen yang lebih aman menjelang dipakai. Konsistensi lebih penting daripada besarnya setoran di awal.</p>"""),
  ],
  faq=[("Apakah tabungan pendidikan di bank cukup?", "Tabungan pendidikan memberi disiplin, tetapi imbal hasilnya biasanya rendah. Untuk jangka panjang, kombinasikan dengan instrumen investasi."),
       ("Bagaimana bila anak lebih dari satu?", "Buat target dan rekening terpisah untuk setiap anak sesuai usianya, lalu jumlahkan setoran bulanannya."),
       ("Apakah asuransi pendidikan diperlukan?", "Yang paling penting adalah perlindungan jiwa untuk pencari nafkah. Bandingkan asuransi pendidikan dengan kombinasi asuransi jiwa murni dan investasi terpisah.")])

A(slug="beli-rumah-atau-sewa", calc="kpr", img="kpr", photo="a3-sewa",
  title="Beli Rumah atau Sewa? Cara Membandingkan Biaya dan Menentukan Pilihan",
  h1="Beli Rumah atau Sewa: Mana yang Lebih Menguntungkan?",
  desc="Panduan membandingkan membeli rumah dengan KPR dan menyewa: biaya yang tidak kembali, rasio harga terhadap sewa, contoh hitungan 10 tahun, serta faktor non-finansial yang perlu dipertimbangkan.",
  lead="Membeli rumah tidak selalu lebih menguntungkan daripada menyewa, dan sebaliknya. Jawabannya tergantung angka dan rencana hidup Anda.",
  body=[
      ("Bukan sekadar cicilan vs sewa", """<p>Banyak orang membandingkan cicilan KPR dengan biaya sewa, lalu menyimpulkan &ldquo;lebih baik mencicil karena rumahnya jadi milik sendiri&rdquo;. Perbandingan yang lebih adil melihat <b>biaya yang tidak kembali</b> dari masing-masing pilihan:</p>
<ul><li><b>Menyewa</b>: biaya sewa.</li>
<li><b>Membeli</b>: bunga KPR, biaya awal (provisi, notaris, BPHTB), pajak bumi dan bangunan, perawatan, asuransi, serta hilangnya potensi hasil investasi dari uang DP.</li></ul>
<p>Cicilan pokok KPR bukan biaya, karena menjadi ekuitas Anda di rumah tersebut. Di sisi lain, nilai rumah bisa naik seiring waktu, yang menjadi keuntungan bagi pembeli.</p>"""),
      ("Contoh perbandingan 10 tahun", """<p>Rumah seharga <b>Rp600 juta</b>, atau disewa <b>Rp30 juta per tahun</b> dengan kenaikan sewa 5% per tahun. Bila membeli: DP 20%, KPR Rp480 juta tenor 20 tahun dengan bunga rata-rata 9%.</p>""" + T(["Komponen 10 tahun pertama", "Sewa", "Beli dengan KPR"], [
          ["Total sewa", "sekitar Rp377 juta", "–"], ["Total bunga KPR", "–", "sekitar Rp379 juta"],
          ["Biaya awal, PBB, perawatan (perkiraan)", "–", "puluhan juta rupiah"], ["Uang DP yang tidak diinvestasikan", "bisa diinvestasikan", "Rp120 juta tertanam di rumah"],
          ["Sisa utang setelah 10 tahun", "–", "sekitar Rp341 juta"], ["Kenaikan nilai rumah", "–", "tergantung lokasi, bisa signifikan"]]) + """
<p>Dalam contoh ini, biaya yang tidak kembali dari menyewa dan membeli dalam 10 tahun ternyata mirip. Yang menentukan adalah <b>kenaikan nilai rumah</b> dan <b>hasil investasi dari uang DP</b> bila Anda memilih menyewa. Di lokasi dengan kenaikan harga tinggi, membeli cenderung unggul; di lokasi yang stagnan, menyewa sambil berinvestasi bisa lebih menguntungkan.</p>"""),
      ("Rasio harga terhadap sewa", """<p>Cara cepat menilai: bagi harga rumah dengan sewa setahun. Contoh di atas: Rp600 juta ÷ Rp30 juta = <b>20</b>.</p>
<ul><li><b>Rasio rendah</b> (misalnya di bawah 15): harga relatif murah dibanding sewa, membeli cenderung menarik.</li>
<li><b>Rasio tinggi</b> (misalnya di atas 20–25): harga relatif mahal dibanding sewa, menyewa sambil berinvestasi bisa lebih efisien.</li></ul>
<p>Rasio ini hanya alat bantu awal. Kondisi suku bunga, rencana tinggal, dan kenaikan harga di lokasi tersebut tetap perlu diperhitungkan.</p>"""),
      ("Faktor non-finansial", """<ul><li><b>Rencana tinggal</b>: bila kemungkinan pindah kota dalam 3–5 tahun, menyewa memberi fleksibilitas.</li>
<li><b>Stabilitas penghasilan</b>: KPR adalah komitmen panjang; penghasilan yang tidak stabil membuatnya lebih berisiko.</li>
<li><b>Rasa aman dan kebebasan</b>: rumah sendiri bisa direnovasi sesuai keinginan dan memberi rasa memiliki.</li>
<li><b>Ukuran keluarga</b>: kebutuhan ruang bisa berubah dalam beberapa tahun.</li></ul>"""),
      ("Tips memutuskan", "<ul>"
       "<li><b>Hitung dengan angka nyata</b> di lokasi yang Anda incar, bukan perkiraan umum.</li>"
       "<li><b>Bila menyewa, investasikan selisihnya</b>; tanpa itu, keunggulan menyewa hilang.</li>"
       "<li><b>Bila membeli, pastikan dana darurat tetap ada</b> setelah DP dan biaya awal.</li>"
       "<li><b>Jangan memaksakan</b> cicilan di atas 30–35% penghasilan.</li>"
       "<li><b>Pertimbangkan rumah sebagai tempat tinggal</b>, bukan semata investasi.</li></ul>"
       + TIP("simulasikan cicilan dan total bunga dengan simulasi KPR, lalu bandingkan dengan total sewa di lokasi yang sama.")),
      ("Kesimpulan", """<p>Beli atau sewa bukan soal benar atau salah, melainkan soal angka dan rencana hidup. Bandingkan biaya yang tidak kembali dari masing-masing pilihan, perhitungkan kenaikan nilai rumah dan potensi investasi dari uang DP, lalu pertimbangkan fleksibilitas dan kestabilan penghasilan. Keputusan yang baik adalah yang tetap membuat keuangan Anda sehat.</p>"""),
  ],
  faq=[("Apakah menyewa berarti membuang uang?", "Tidak. Pemilik rumah juga mengeluarkan biaya yang tidak kembali seperti bunga, pajak, dan perawatan. Yang penting adalah membandingkan total biaya dan hasilnya."),
       ("Lebih baik beli rumah atau apartemen?", "Tergantung lokasi, kebutuhan ruang, dan biaya pengelolaan. Apartemen memiliki biaya layanan rutin dan status kepemilikan yang perlu diperhatikan."),
       ("Kapan waktu terbaik membeli rumah?", "Saat dana DP, biaya awal, dan dana darurat sudah siap, penghasilan stabil, dan Anda berencana tinggal cukup lama.")])

A(slug="mengatur-keuangan-freelancer", calc="deposito", img="deposito", photo="a3-freelance",
  title="Mengatur Keuangan Freelancer dan Penghasilan Tidak Tetap",
  h1="Cara Mengatur Keuangan untuk Freelancer",
  desc="Panduan keuangan untuk freelancer dan pekerja dengan penghasilan tidak tetap: menggaji diri sendiri, dana penyangga, pajak, BPJS mandiri, rekening terpisah, dan tips menjaga arus kas.",
  lead="Penghasilan yang naik-turun menuntut cara mengatur uang yang berbeda dari karyawan bergaji tetap. Berikut sistem sederhana yang bisa Anda terapkan.",
  body=[
      ("Tantangan keuangan freelancer", """<p>Freelancer, kreator, konsultan, dan pekerja lepas sering menghadapi bulan &ldquo;panen&rdquo; dan bulan &ldquo;paceklik&rdquo;. Tidak ada THR, BPJS dari kantor, atau potongan pajak otomatis. Semua tanggung jawab itu berpindah ke diri sendiri. Kuncinya adalah membuat <b>sistem</b> yang membuat penghasilan tidak tetap terasa seperti gaji tetap.</p>"""),
      ("Sistem tiga rekening dan gaji untuk diri sendiri", """<ol><li><b>Rekening penampung</b>: semua pembayaran klien masuk ke sini.</li>
<li><b>Rekening gaji</b>: setiap bulan, transfer jumlah tetap dari penampung ke rekening ini, seolah Anda menggaji diri sendiri. Jumlahnya berdasarkan rata-rata penghasilan, misalnya rata-rata 12 bulan terakhir dikurangi cadangan.</li>
<li><b>Rekening pajak dan kewajiban</b>: sisihkan persentase tertentu dari setiap pembayaran untuk pajak, BPJS, dan zakat.</li></ol>
<p>Kelebihan penghasilan di bulan panen tetap tinggal di penampung sebagai <b>dana penyangga</b> untuk bulan sepi.</p>"""),
      ("Dana penyangga dan dana darurat", """<p>Karena penghasilan tidak pasti, freelancer membutuhkan cadangan lebih besar daripada karyawan. Patokan umum adalah <b>6–12 kali pengeluaran bulanan</b>. Dana ini bisa dibagi:</p>""" + T(["Lapisan", "Fungsi", "Tempat"], [
          ["Penyangga arus kas (2–3 bulan)", "Menutup bulan sepi", "Tabungan di rekening penampung"],
          ["Dana darurat (3–6 bulan)", "Sakit, alat kerja rusak, kehilangan klien besar", "Reksa dana pasar uang atau tabungan terpisah"],
          ["Cadangan tambahan", "Masa transisi panjang", "Deposito berjenjang"]])),
      ("Pajak dan jaminan sosial", """<ul><li><b>Pajak penghasilan</b>: honor dari pemberi kerja bisa dipotong PPh 21 atau PPh 23. Bila Anda menjalankan usaha atau pekerjaan bebas, pelajari pilihan pencatatan dan tarif yang berlaku, termasuk tarif final 0,5% dari omzet bagi pelaku usaha tertentu sesuai PP 55/2022. Simpan bukti potong dan catatan penghasilan untuk SPT Tahunan.</li>
<li><b>BPJS Kesehatan mandiri</b>: daftarkan diri dan keluarga, bayar tepat waktu agar tidak nonaktif.</li>
<li><b>BPJS Ketenagakerjaan BPU</b>: JKK dan JKM dengan iuran terjangkau, ditambah JHT sebagai tabungan hari tua.</li>
<li><b>Dana pensiun pribadi</b>: karena tidak ada program kantor, siapkan sendiri lewat investasi rutin atau DPLK.</li></ul>"""),
      ("Tips menjaga arus kas", "<ul>"
       "<li><b>Minta uang muka</b> untuk proyek besar, misalnya 30–50% di awal.</li>"
       "<li><b>Buat kontrak tertulis</b> berisi lingkup kerja, tenggat, dan jadwal pembayaran.</li>"
       "<li><b>Kirim invoice tepat waktu</b> dan tindak lanjuti pembayaran yang terlambat.</li>"
       "<li><b>Diversifikasi klien</b> agar tidak bergantung pada satu sumber penghasilan.</li>"
       "<li><b>Catat semua pemasukan dan pengeluaran usaha</b>, minimal di spreadsheet sederhana.</li>"
       "<li><b>Naikkan tarif secara berkala</b> sesuai pengalaman dan inflasi.</li></ul>"
       + TIP("simpan lapisan dana penyangga di deposito berjenjang dan hitung bunga bersihnya dengan kalkulator deposito.")),
      ("Kesimpulan", """<p>Mengatur keuangan freelancer berarti mengganti struktur yang biasanya disediakan kantor dengan sistem sendiri: menggaji diri sendiri, membangun dana penyangga yang lebih besar, menyisihkan pajak dan iuran BPJS, serta menyiapkan dana pensiun pribadi. Dengan sistem yang konsisten, penghasilan yang naik-turun tidak lagi membuat keuangan ikut goyah.</p>"""),
  ],
  faq=[("Berapa persen penghasilan yang perlu disisihkan untuk pajak?", "Tergantung jenis penghasilan dan skema pajak yang Anda pakai. Hitung berdasarkan ketentuan yang berlaku, lalu sisihkan persentase yang sedikit lebih besar sebagai cadangan."),
       ("Apakah freelancer bisa mengajukan KPR?", "Bisa, dengan rekening koran, kontrak kerja, dan bukti pajak sebagai bukti penghasilan. Riwayat penghasilan yang tercatat rapi sangat membantu."),
       ("Bagaimana menentukan gaji untuk diri sendiri?", "Hitung rata-rata penghasilan bersih 6–12 bulan terakhir, kurangi sebagian untuk cadangan, lalu tetapkan sebagai jumlah tetap bulanan.")])
