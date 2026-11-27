"""Bagian tambahan artikel panduan (Bahasa Indonesia).
Setiap entri disisipkan sebelum bagian terakhir (tips) artikel dengan slug yang sama."""

T = lambda head, rows: ('<div class="tscroll"><table class="tbl"><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
                        + "".join("<tr" + (' class="tot"' if r[0].startswith("=") else "") + ">" + "".join(f"<td>{c.lstrip('=')}</td>" for c in r) + "</tr>" for r in rows)
                        + "</tbody></table></div>")

EXTRA = {}

EXTRA["apa-itu-pph-21-ter"] = [
    ("Contoh lengkap: gaji Rp15 juta, status K/1", """<p>Agar lebih konkret, mari hitung PPh 21 karyawan berstatus <b>K/1</b> (menikah, satu anak) dengan gaji pokok dan tunjangan tetap <b>Rp15.000.000</b> per bulan, ikut semua program BPJS dengan risiko kerja sangat rendah, tanpa bonus.</p>
<p><b>Langkah 1 – bruto bulanan.</b> Selain gaji, perusahaan membayar premi BPJS Kesehatan 4% (Rp480.000, karena batas upah Rp12 juta), JKK 0,24% (Rp36.000), dan JKM 0,3% (Rp45.000). Ketiganya menambah bruto, sehingga bruto bulanan menjadi <b>Rp15.561.000</b>.</p>
<p><b>Langkah 2 – TER Januari–November.</b> Status K/1 masuk kategori B. Untuk bruto Rp15.561.000, tarif TER-nya 6%, sehingga potongan setiap bulan <b>Rp933.660</b>. Selama 11 bulan totalnya Rp10.270.260.</p>
<p><b>Langkah 3 – perhitungan Desember.</b></p>""" + T(["Komponen", "Setahun"], [
        ["Penghasilan bruto (12 × Rp15.561.000)", "Rp186.732.000"], ["− Biaya jabatan (dibatasi)", "Rp6.000.000"], ["− Iuran JHT 2% dan JP 1% karyawan", "Rp4.930.356"],
        ["=Penghasilan neto", "Rp175.801.644"], ["− PTKP K/1", "Rp63.000.000"], ["=PKP (dibulatkan ke ribuan)", "Rp112.801.000"],
        ["5% × Rp60.000.000", "Rp3.000.000"], ["15% × Rp52.801.000", "Rp7.920.150"], ["=PPh 21 setahun", "Rp10.920.150"],
        ["− Sudah dipotong Januari–November", "Rp10.270.260"], ["=PPh 21 Desember", "Rp649.890"]]) + """
<p>Hasilnya, potongan Desember (Rp649.890) justru lebih kecil dari bulan biasa. Ini wajar: TER untuk bruto di kisaran itu sedikit lebih tinggi dari tarif efektif setahun yang sebenarnya, sehingga Desember menjadi bulan penyesuaian. Total pajak setahun tetap <b>Rp10.920.150</b>, atau sekitar 5,8% dari bruto.</p>"""),
    ("Salah kaprah yang sering terjadi", """<ul><li><b>&ldquo;TER adalah pajak final.&rdquo;</b> Tidak. TER hanya cara memotong per bulan. Pajak yang sebenarnya tetap dihitung ulang setahun dengan tarif Pasal 17.</li>
<li><b>&ldquo;Bonus kena pajak lebih tinggi.&rdquo;</b> Bonus memang membuat potongan bulan itu melonjak, tetapi di akhir tahun semua penghasilan dijumlahkan dan dihitung dengan tarif yang sama. Bonus tidak dikenai &ldquo;tarif khusus&rdquo;.</li>
<li><b>&ldquo;Status berubah, pajak langsung berubah.&rdquo;</b> Status PTKP mengikuti keadaan awal tahun pajak. Menikah atau punya anak di tengah tahun baru berpengaruh pada tahun pajak berikutnya.</li>
<li><b>&ldquo;Kalau gaji di bawah PTKP, tidak ada potongan sama sekali.&rdquo;</b> Pada bulan biasa, TER untuk bruto rendah memang 0%. Tetapi bila ada bonus besar di satu bulan, bisa ada potongan sementara yang kemudian dikembalikan di Desember.</li>
<li><b>&ldquo;Pindah kerja tidak perlu mengurus apa-apa.&rdquo;</b> Justru penting meminta bukti potong dari kantor lama. Tanpa itu, kantor baru menghitung seolah Anda baru mulai bekerja, dan pajak setahun bisa kurang bayar saat lapor SPT.</li></ul>"""),
    ("Istilah penting yang perlu Anda pahami", """<ul><li><b>Penghasilan bruto</b>: seluruh penghasilan sebelum dikurangi apa pun, termasuk premi asuransi yang dibayar perusahaan.</li>
<li><b>Biaya jabatan</b>: pengurang otomatis sebesar 5% dari bruto, maksimal Rp500.000 per bulan atau Rp6.000.000 per tahun, sebagai pengganti biaya untuk mendapatkan penghasilan.</li>
<li><b>Penghasilan neto</b>: bruto dikurangi biaya jabatan dan iuran pensiun/JHT yang dibayar karyawan.</li>
<li><b>PTKP</b>: batas penghasilan tidak kena pajak yang ditentukan status kawin dan jumlah tanggungan.</li>
<li><b>PKP</b>: penghasilan kena pajak, yaitu neto dikurangi PTKP, dibulatkan ke bawah ke ribuan rupiah.</li>
<li><b>Bukti potong 1721-A1</b>: dokumen dari pemberi kerja yang merangkum penghasilan dan pajak setahun.</li>
<li><b>Kurang bayar / lebih bayar</b>: selisih antara pajak terutang setahun dan pajak yang sudah dipotong.</li></ul>"""),
]

EXTRA["cara-membaca-slip-gaji"] = [
    ("Contoh slip gaji dan cara membacanya", """<p>Berikut contoh slip gaji bulan biasa untuk karyawan berstatus TK/0 dengan gaji Rp10.000.000, ikut semua program BPJS (risiko kerja sangat rendah):</p>""" + T(["Komponen", "Jumlah"], [
        ["Gaji pokok", "Rp8.000.000"], ["Tunjangan jabatan (tetap)", "Rp2.000.000"], ["=Total penghasilan", "Rp10.000.000"],
        ["BPJS Kesehatan 1%", "−Rp100.000"], ["JHT 2%", "−Rp200.000"], ["JP 1%", "−Rp100.000"], ["PPh 21 (TER kategori A 2,5% × Rp10.454.000)", "−Rp261.350"],
        ["=Gaji bersih ditransfer", "Rp9.338.650"]]) + """
<p>Beberapa hal yang perlu diperhatikan dari contoh ini:</p>
<ul><li>PPh 21 dihitung dari <b>Rp10.454.000</b>, bukan Rp10.000.000, karena premi BPJS Kesehatan (Rp400.000), JKK (Rp24.000), dan JKM (Rp30.000) yang dibayar perusahaan ikut dihitung sebagai penghasilan.</li>
<li>Iuran perusahaan biasanya <b>tidak</b> tercantum sebagai potongan, karena memang tidak diambil dari gaji Anda. Beberapa perusahaan mencantumkannya sebagai informasi.</li>
<li>Bila ada lembur, bonus, atau potongan absensi, angka bulan itu akan berbeda.</li></ul>"""),
    ("Hak Anda atas slip gaji", """<p>Menurut peraturan pengupahan (PP 36/2021 beserta perubahannya), pengusaha wajib memberikan <b>bukti pembayaran upah</b> yang memuat rincian upah setiap kali upah dibayarkan. Bentuknya boleh kertas atau elektronik, misalnya lewat email atau aplikasi HR.</p>
<p>Slip gaji bukan sekadar formalitas. Dokumen ini dibutuhkan untuk mengajukan KPR, kredit kendaraan, kartu kredit, visa, atau beasiswa, dan menjadi bukti bila terjadi perselisihan upah. Simpan slip gaji setidaknya selama Anda bekerja di perusahaan tersebut dan beberapa tahun setelahnya.</p>"""),
    ("Kesalahan yang sering ditemukan di slip gaji", """<ul><li><b>Status PTKP keliru</b>, misalnya sudah menikah tetapi masih tercatat TK/0, sehingga pajak lebih besar.</li>
<li><b>Dasar iuran BPJS terlalu rendah</b>, misalnya hanya dari gaji pokok padahal ada tunjangan tetap. Akibatnya saldo JHT dan manfaat pensiun lebih kecil.</li>
<li><b>Lembur tidak dihitung sesuai aturan</b>, misalnya dibayar flat per jam tanpa kelipatan 1,5 dan 2 kali.</li>
<li><b>Potongan tanpa penjelasan</b>, seperti &ldquo;potongan lain-lain&rdquo; yang tidak jelas dasarnya.</li>
<li><b>Rapel kenaikan gaji terlewat</b> setelah ada penyesuaian upah minimum atau promosi.</li></ul>
<p>Bila menemukan kejanggalan, tanyakan baik-baik ke HRD dengan membawa hitungan Anda. Sebagian besar kesalahan terjadi karena data yang belum diperbarui, bukan kesengajaan.</p>"""),
]

EXTRA["aturan-thr-dan-tips-mengelolanya"] = [
    ("Contoh perhitungan untuk berbagai kondisi", """<p>Berikut beberapa contoh agar aturan proporsional lebih mudah dipahami:</p>""" + T(["Kondisi", "Perhitungan", "THR"], [
        ["Karyawan tetap, kerja 3 tahun, upah Rp7.000.000", "1 × Rp7.000.000", "Rp7.000.000"],
        ["Karyawan kontrak, kerja 4 bulan, upah Rp6.000.000", "4/12 × Rp6.000.000", "Rp2.000.000"],
        ["Karyawan baru, kerja 1 bulan, upah Rp9.000.000", "1/12 × Rp9.000.000", "Rp750.000"],
        ["Harian lepas, kerja 8 bulan, rata-rata upah Rp3.600.000", "rata-rata upah per bulan selama masa kerja", "Rp3.600.000 × 8/12 = Rp2.400.000"],
        ["Karyawan baru, kerja 3 minggu", "belum memenuhi 1 bulan", "belum berhak"]]) + """
<p>Masa kerja dihitung sampai hari raya keagamaan pekerja yang bersangkutan, bukan sampai tanggal pembayaran THR. Bila perusahaan memiliki kebijakan THR yang lebih besar dari aturan, yang berlaku adalah kebijakan yang lebih menguntungkan pekerja.</p>"""),
    ("Bagaimana dengan freelancer dan mitra aplikasi?", """<p>Permenaker 6/2016 mengatur hubungan kerja antara <b>pengusaha dan pekerja</b>. Freelancer yang bekerja per proyek tanpa hubungan kerja, serta mitra pengemudi aplikasi yang berstatus kemitraan, umumnya tidak termasuk dalam aturan THR tersebut. Pemerintah pernah mengimbau perusahaan aplikasi memberikan bonus hari raya kepada mitranya, tetapi bentuk dan besarnya mengikuti kebijakan perusahaan masing-masing.</p>
<p>Bila Anda bekerja dengan status kemitraan atau lepas, sebaiknya siapkan &ldquo;THR sendiri&rdquo; dengan menyisihkan sebagian penghasilan setiap bulan, misalnya 8–10%, ke rekening terpisah. Dalam setahun, jumlahnya kira-kira setara satu bulan penghasilan.</p>"""),
    ("Kesalahan umum saat menerima THR", """<ul><li><b>Menghabiskan THR sebelum diterima</b>, misalnya dengan belanja memakai kartu kredit atau paylater sejak awal Ramadan.</li>
<li><b>Lupa memperhitungkan pajak</b>, sehingga anggaran disusun dari THR kotor.</li>
<li><b>Semua untuk konsumsi</b>, tanpa menyisakan untuk tabungan atau kebutuhan setelah hari raya.</li>
<li><b>Gengsi dan tekanan sosial</b>, misalnya memaksakan barang baru atau pemberian yang melebihi kemampuan.</li>
<li><b>Meminjam untuk mudik</b>, lalu cicilannya membebani beberapa bulan berikutnya.</li></ul>
<p>Salah satu cara sederhana adalah membagi THR bersih menjadi pos tetap, misalnya 40% kebutuhan hari raya, 20% berbagi, 20% mudik atau silaturahmi, dan 20% tabungan. Sesuaikan persentasenya dengan kondisi keluarga Anda.</p>"""),
]

EXTRA["mengenal-bpjs-kesehatan-dan-ketenagakerjaan"] = [
    ("Ilustrasi: berapa yang terkumpul di JHT?", """<p>Karyawan dengan upah <b>Rp8.000.000</b> menyetor JHT sebesar 5,7% setiap bulan (3,7% dari perusahaan dan 2% dari karyawan), yaitu <b>Rp456.000</b>. Dalam setahun terkumpul Rp5.472.000, dan dalam 10 tahun sekitar <b>Rp54,7 juta</b> dari iuran saja, belum termasuk hasil pengembangan dana oleh BPJS Ketenagakerjaan dan kenaikan gaji.</p>
<p>Angka ini menunjukkan mengapa JHT sebaiknya tidak buru-buru dicairkan setiap kali pindah kerja. Bila saldo terus dibiarkan berkembang dan digabung ke kepesertaan di perusahaan berikutnya, JHT bisa menjadi salah satu bekal hari tua yang cukup berarti, selain Jaminan Pensiun.</p>"""),
    ("Peserta mandiri dan pekerja bukan penerima upah", """<p>Tidak semua orang bekerja sebagai karyawan. Untuk mereka, ada skema berbeda:</p>
<ul><li><b>BPJS Kesehatan mandiri</b>: iuran dibayar sendiri dengan nominal tetap per orang per bulan sesuai kelas, untuk setiap anggota keluarga yang didaftarkan. Besaran iuran mengikuti peraturan presiden yang berlaku.</li>
<li><b>BPJS Ketenagakerjaan untuk Bukan Penerima Upah (BPU)</b>: cocok untuk pedagang, freelancer, pengemudi daring, petani, dan pekerja mandiri lain. Program dasarnya JKK dan JKM dengan iuran yang ditetapkan berdasarkan penghasilan yang dilaporkan, mulai dari belasan ribu rupiah per bulan. JHT dapat ditambahkan secara opsional.</li></ul>
<p>Bagi pekerja mandiri, perlindungan JKK sangat berharga: biaya perawatan akibat kecelakaan kerja bisa sangat besar, sementara iurannya relatif kecil.</p>"""),
    ("Kesalahan umum seputar BPJS", """<ul><li><b>Menunggak iuran BPJS Kesehatan mandiri.</b> Kepesertaan bisa nonaktif, dan saat diaktifkan kembali ada ketentuan denda untuk layanan rawat inap tertentu.</li>
<li><b>Tidak memperbarui data keluarga</b> setelah menikah atau punya anak, sehingga anggota keluarga belum tertanggung.</li>
<li><b>Mengira BPJS Ketenagakerjaan otomatis pindah</b> saat ganti pekerjaan. Pastikan perusahaan baru melanjutkan kepesertaan dengan nomor yang sama.</li>
<li><b>Tidak melapor kecelakaan kerja</b> dalam batas waktu, sehingga klaim JKK terhambat.</li>
<li><b>Mengabaikan JP</b> karena manfaatnya baru terasa saat pensiun. Padahal masa iuran minimal 15 tahun menentukan apakah Anda menerima pensiun bulanan.</li></ul>"""),
]

EXTRA["panduan-kpr-rumah-pertama"] = [
    ("Contoh perhitungan KPR", """<p>Rumah seharga <b>Rp600 juta</b> dengan DP 20% (Rp120 juta) berarti pokok pinjaman <b>Rp480 juta</b>. Tenor 15 tahun, bunga fixed 4,5% selama 3 tahun, lalu floating 11%.</p>""" + T(["Periode", "Cicilan per bulan", "Catatan"], [
        ["Tahun 1–3 (fixed 4,5%)", "Rp3.671.968", "Tahun pertama: bunga Rp21,1 juta, pokok Rp22,9 juta"],
        ["Tahun 4–15 (floating 11%)", "Rp5.114.414", "Dihitung ulang dari sisa pokok sekitar Rp408 juta"],
        ["=Total bunga 15 tahun", "sekitar Rp388,7 juta", "Hampir 81% dari pokok pinjaman"]]) + """
<p>Perhatikan dua hal. Pertama, di tahun pertama hampir separuh cicilan habis untuk bunga. Kedua, setelah 3 tahun sisa pokok masih sekitar Rp408 juta, artinya baru sekitar 15% pokok yang terbayar, sementara cicilan naik sekitar Rp1,44 juta per bulan. Untuk cicilan Rp5,1 juta, bank biasanya mensyaratkan penghasilan sekitar Rp17 juta per bulan.</p>"""),
    ("KPR konvensional dan KPR syariah", T(["Aspek", "Konvensional", "Syariah (murabahah)"], [
        ["Dasar", "Pinjaman dengan bunga", "Jual beli dengan margin keuntungan"],
        ["Cicilan", "Fixed beberapa tahun, lalu floating", "Umumnya tetap sampai lunas"],
        ["Risiko kenaikan cicilan", "Ada, saat bunga floating naik", "Tidak ada untuk akad margin tetap"],
        ["Total biaya", "Bisa lebih rendah bila bunga turun", "Pasti sejak awal, kadang lebih tinggi"],
        ["Pelunasan dipercepat", "Ada penalti sesuai ketentuan bank", "Mengikuti ketentuan akad dan bank"]]) + """
<p>KPR syariah dengan margin tetap memberi kepastian cicilan, cocok bagi yang tidak ingin menghadapi risiko kenaikan bunga. KPR konvensional menarik bila Anda memperkirakan suku bunga akan turun atau berencana melunasi lebih cepat. Bandingkan total pembayaran keduanya, bukan hanya angka cicilan bulan pertama.</p>"""),
    ("Tahapan proses KPR dari awal sampai akad", """<ol><li><b>Hitung kemampuan</b>: tentukan cicilan maksimal (30–35% penghasilan) dan dana awal yang tersedia.</li>
<li><b>Cari rumah</b> dan pastikan legalitasnya: sertifikat, IMB/PBG, dan reputasi developer.</li>
<li><b>Ajukan ke beberapa bank</b> dengan dokumen lengkap. Bank akan memeriksa SLIK OJK dan kemampuan bayar.</li>
<li><b>Appraisal</b>: bank menilai rumah. Plafon kredit bisa lebih kecil dari harga bila nilai taksiran lebih rendah.</li>
<li><b>Surat persetujuan kredit (SP3K)</b>: berisi plafon, bunga, tenor, dan biaya. Baca dengan teliti.</li>
<li><b>Akad kredit</b> di hadapan notaris: penandatanganan perjanjian kredit, AJB, dan APHT, sekaligus pembayaran biaya-biaya.</li>
<li><b>Pencairan dan serah terima</b>: dana dibayarkan ke penjual atau developer, lalu kunci diserahkan.</li></ol>
<p>Prosesnya bisa memakan beberapa minggu sampai beberapa bulan, tergantung kelengkapan dokumen dan status rumah (siap huni atau inden).</p>"""),
]

EXTRA["bunga-flat-vs-efektif-kredit-kendaraan"] = [
    ("Contoh: membandingkan dua penawaran", """<p>Anda ingin membeli motor seharga <b>Rp25 juta</b> dengan DP 20%, sehingga pokok pinjaman Rp20 juta dengan tenor 36 bulan. Ada dua penawaran:</p>""" + T(["", "Penawaran A", "Penawaran B"], [
        ["Bunga tertulis", "5% flat per tahun", "9% efektif per tahun"], ["Cicilan per bulan", "Rp638.889", "Rp635.995"],
        ["Total bunga 36 bulan", "Rp3.000.000", "Rp2.895.808"], ["=Bunga efektif setara", "sekitar 9,3%", "9%"]]) + """
<p>Sekilas penawaran A tampak jauh lebih murah karena angkanya &ldquo;5%&rdquo;. Setelah diubah ke satuan yang sama, penawaran B justru sedikit lebih murah. Inilah alasan kenapa membandingkan bunga flat dengan bunga efektif secara langsung bisa menyesatkan.</p>"""),
    ("Cara membaca brosur dan simulasi leasing", """<ul><li><b>Cari total pembayaran</b>, bukan hanya cicilan. Kalikan cicilan dengan jumlah bulan, lalu tambahkan DP dan biaya awal.</li>
<li><b>Perhatikan &ldquo;DP ringan&rdquo;</b>. DP kecil membuat pokok pinjaman besar, sehingga total bunga juga besar.</li>
<li><b>Cek apakah asuransi sudah termasuk</b> dalam cicilan, dan jenisnya (all risk atau total loss only).</li>
<li><b>Tanyakan angsuran pertama</b>: dibayar di depan bersama DP atau bulan berikutnya.</li>
<li><b>Waspadai promo &ldquo;bunga 0%&rdquo;</b>. Kadang biayanya dipindahkan ke harga kendaraan, biaya administrasi, atau asuransi. Bandingkan dengan harga tunai.</li></ul>"""),
    ("Kredit atau menabung dulu lalu beli tunai?", """<p>Kredit memungkinkan Anda memakai kendaraan sekarang, tetapi ada biaya bunga. Menabung dulu lebih murah, tetapi butuh waktu dan disiplin. Pertimbangkan:</p>
<ul><li><b>Bila kendaraan menghasilkan uang</b> (untuk usaha, ojek, atau perjalanan kerja yang menggantikan biaya transportasi besar), kredit bisa masuk akal selama cicilan aman.</li>
<li><b>Bila kendaraan untuk gaya hidup</b>, menabung lalu membeli tunai atau dengan DP besar biasanya lebih bijak.</li>
<li><b>Kendaraan adalah aset yang nilainya turun.</b> Setelah 3 tahun, nilai jual kembali bisa jauh di bawah total yang Anda bayarkan.</li></ul>
<p>Jalan tengahnya: kumpulkan DP sebesar mungkin, pilih tenor sependek yang masih nyaman, dan pastikan dana darurat tetap aman.</p>"""),
]

EXTRA["panduan-deposito-untuk-pemula"] = [
    ("Contoh perhitungan deposito ARO", """<p>Deposito <b>Rp100 juta</b> dengan bunga 4% per tahun, tenor 12 bulan, diperpanjang otomatis beserta bunganya (ARO + bunga) selama tiga periode:</p>""" + T(["Periode", "Bunga bersih (setelah pajak 20%)", "Saldo akhir periode"], [
        ["1", "Rp3.200.000", "Rp103.200.000"], ["2", "Rp3.302.400", "Rp106.502.400"], ["3", "Rp3.408.077", "Rp109.910.477"]]) + """
<p>Bunga bersih bertambah setiap periode karena bunga sebelumnya ikut didepositokan. Imbal bersihnya sekitar 3,2% per tahun. Dengan asumsi suku bunga tetap, saldo bertambah hampir Rp10 juta dalam tiga tahun tanpa tambahan setoran.</p>
<p>Dalam kenyataan, suku bunga saat perpanjangan mengikuti suku bunga yang berlaku saat itu, sehingga bisa naik atau turun.</p>"""),
    ("Deposito, tabungan biasa, dan tabungan berjangka", T(["", "Tabungan biasa", "Tabungan berjangka", "Deposito"], [
        ["Tujuan", "Transaksi harian", "Menabung rutin untuk target", "Menyimpan dana yang belum dipakai"],
        ["Setoran", "Bebas", "Rutin bulanan, autodebet", "Sekali di awal"],
        ["Penarikan", "Kapan saja", "Saat jatuh tempo", "Saat jatuh tempo"],
        ["Bunga", "Paling rendah", "Lebih tinggi dari tabungan biasa", "Umumnya paling tinggi di antara ketiganya"],
        ["Cocok untuk", "Dana harian dan sebagian dana darurat", "Membangun kebiasaan menabung", "Dana yang sudah terkumpul"]]) + """
<p>Ketiganya bisa saling melengkapi: tabungan biasa untuk kebutuhan sehari-hari, tabungan berjangka untuk mengumpulkan dana sedikit demi sedikit, dan deposito untuk menyimpan dana yang sudah terkumpul agar menghasilkan bunga lebih tinggi.</p>"""),
    ("Strategi tangga deposito (laddering)", """<p>Laddering berarti membagi dana ke beberapa deposito dengan jatuh tempo berbeda. Contohnya, dana Rp60 juta dibagi menjadi:</p>
<ul><li>Rp20 juta tenor 3 bulan,</li><li>Rp20 juta tenor 6 bulan,</li><li>Rp20 juta tenor 12 bulan.</li></ul>
<p>Setiap kali satu deposito jatuh tempo, Anda bisa memakainya bila perlu, atau memperpanjangnya ke tenor terpanjang. Hasilnya, sebagian dana selalu tersedia dalam waktu dekat, sementara sebagian lain mendapat bunga tenor yang lebih panjang. Strategi ini juga mengurangi risiko &ldquo;salah waktu&rdquo; saat suku bunga berubah.</p>"""),
]

EXTRA["bunga-majemuk-dan-investasi-rutin"] = [
    ("Kekuatan memulai lebih awal", """<p>Bandingkan dua orang yang sama-sama ingin punya dana di usia 55 tahun, dengan asumsi imbal hasil 8% per tahun:</p>""" + T(["", "Rina", "Budi"], [
        ["Mulai berinvestasi", "Usia 25", "Usia 35"], ["Setoran per bulan", "Rp1.000.000", "Rp2.000.000"],
        ["Lama berinvestasi", "30 tahun", "20 tahun"], ["Total setoran", "Rp360 juta", "Rp480 juta"], ["=Nilai di usia 55", "sekitar Rp1,41 miliar", "sekitar Rp1,14 miliar"]]) + """
<p>Budi menyetor dua kali lipat per bulan dan total setorannya lebih besar Rp120 juta, tetapi hasil akhirnya tetap kalah dari Rina. Sepuluh tahun tambahan memberi waktu bagi bunga majemuk untuk bekerja. Pesannya sederhana: mulai sekarang, walaupun nominalnya kecil.</p>"""),
    ("Kenali profil risiko Anda", """<p>Sebelum memilih instrumen, kenali seberapa besar penurunan nilai yang sanggup Anda hadapi tanpa panik:</p>
<ul><li><b>Konservatif</b>: tidak nyaman melihat nilai turun. Utamakan reksa dana pasar uang, deposito, dan SBN.</li>
<li><b>Moderat</b>: bisa menerima naik-turun sedang demi hasil lebih baik. Kombinasi obligasi, reksa dana campuran, dan sebagian saham.</li>
<li><b>Agresif</b>: siap menghadapi penurunan besar dalam jangka pendek demi potensi hasil jangka panjang. Porsi saham lebih besar.</li></ul>
<p>Profil risiko juga dipengaruhi jangka waktu. Dana yang dibutuhkan tahun depan sebaiknya tidak ditaruh di saham, walaupun Anda berprofil agresif. Platform investasi resmi biasanya meminta Anda mengisi kuesioner profil risiko sebelum membeli produk.</p>"""),
    ("Kesalahan umum investor pemula", """<ul><li><b>Ikut-ikutan</b> membeli produk yang sedang ramai tanpa memahami isinya.</li>
<li><b>Berharap cepat kaya</b> dan berpindah-pindah produk setiap kali ada penurunan.</li>
<li><b>Tidak punya dana darurat</b>, sehingga investasi terpaksa dicairkan saat harga turun.</li>
<li><b>Menaruh semua dana di satu produk</b> atau satu saham.</li>
<li><b>Mengabaikan biaya</b> pembelian, penjualan, dan pengelolaan yang menggerus hasil.</li>
<li><b>Tergiur janji imbal hasil pasti tinggi</b> dari pihak yang tidak terdaftar di OJK.</li></ul>"""),
]

EXTRA["cara-lapor-spt-tahunan-karyawan"] = [
    ("Mengisi daftar harta dan utang", """<p>Bagian harta dan utang sering membuat bingung. Beberapa pedoman sederhana:</p>
<ul><li><b>Kas dan setara kas</b>: saldo tabungan, giro, dan deposito per 31 Desember.</li>
<li><b>Kendaraan dan properti</b>: dicatat sebesar <b>harga perolehan</b> (harga beli), tidak perlu dinilai ulang setiap tahun.</li>
<li><b>Investasi</b>: reksa dana, saham, obligasi, dan emas dicatat sebesar nilai perolehan atau sesuai petunjuk pengisian yang berlaku.</li>
<li><b>Utang</b>: sisa pokok KPR, kredit kendaraan, kartu kredit, dan pinjaman lain per 31 Desember.</li></ul>
<p>Harta yang dibeli dengan kredit tetap dicatat sebesar harga perolehannya, sedangkan sisa kreditnya dicatat di bagian utang. Pastikan perubahan harta dari tahun ke tahun masuk akal dibandingkan penghasilan Anda.</p>"""),
    ("Bila Anda punya penghasilan lain", """<ul><li><b>Bunga deposito, kupon SBN, dan hadiah tertentu</b> sudah dikenai pajak final. Cukup dilaporkan, tidak dihitung ulang.</li>
<li><b>Usaha sampingan</b> dengan omzet sampai Rp4,8 miliar setahun dapat memakai tarif final 0,5% dari omzet sesuai PP 55/2022 (dalam jangka waktu tertentu). Wajib pajak orang pribadi dengan omzet sampai Rp500 juta setahun tidak dikenai pajak atas bagian omzet tersebut.</li>
<li><b>Honor freelance atau pekerjaan bebas</b> yang tidak dipotong pajak oleh pemberi honor perlu dihitung bersama gaji dan dapat menimbulkan kurang bayar.</li>
<li><b>Penghasilan dari dua pemberi kerja</b> dalam setahun hampir selalu menyebabkan kurang bayar, karena PTKP dan tarif rendah dipakai dua kali oleh masing-masing pemberi kerja.</li></ul>"""),
    ("Bila ada kesalahan setelah lapor", """<p>Kesalahan dalam SPT bisa diperbaiki dengan <b>SPT pembetulan</b>. Di Coretax, pilih model SPT <b>Pembetulan</b> saat membuat konsep, lalu ubah bagian yang keliru. Pembetulan dapat dilakukan selama Direktorat Jenderal Pajak belum melakukan pemeriksaan.</p>
<p>Bila pembetulan menyebabkan pajak kurang bayar, setor kekurangannya. Mungkin ada sanksi bunga sesuai ketentuan. Bila menyebabkan lebih bayar, Anda bisa mengajukan pengembalian. Lebih baik membetulkan sendiri daripada menunggu ditegur.</p>"""),
]

EXTRA["cara-menghitung-upah-lembur"] = [
    ("Contoh lembur di hari kerja", """<p>Upah Rp6.000.000 per bulan, upah sejam Rp34.682. Dalam satu bulan, karyawan lembur di hari kerja sebanyak 5 kali, masing-masing 3 jam.</p>""" + T(["Rincian", "Perhitungan", "Jumlah"], [
        ["Jam pertama", "1,5 × Rp34.682", "Rp52.023"], ["Jam kedua dan ketiga", "2 × 2 × Rp34.682", "Rp138.728"],
        ["=Upah lembur per hari", "", "Rp190.751"], ["=Upah lembur sebulan", "5 × Rp190.751", "Rp953.757"]]) + """
<p>Total lembur sebulan hampir Rp1 juta, atau sekitar 16% dari upah. Angka ini cukup besar untuk diperiksa setiap bulan di slip gaji.</p>"""),
    ("Lembur, pajak, dan BPJS", """<ul><li><b>Pajak</b>: upah lembur adalah penghasilan tidak tetap yang dijumlahkan dengan gaji bulan itu untuk menghitung PPh 21 metode TER. Bila lembur besar, tarif TER bulan itu bisa naik satu lapis.</li>
<li><b>BPJS</b>: iuran BPJS dihitung dari upah tetap (gaji pokok dan tunjangan tetap). Upah lembur tidak menambah iuran BPJS.</li>
<li><b>THR dan pesangon</b>: dihitung dari upah tetap, sehingga upah lembur juga tidak ikut menjadi dasar perhitungan.</li></ul>"""),
    ("Hak lain saat lembur", """<p>Selain upah, pekerja yang lembur berhak atas waktu istirahat yang cukup. Untuk lembur 4 jam atau lebih, pengusaha wajib menyediakan makanan dan minuman minimal 1.400 kalori, dan kewajiban ini tidak boleh diganti dengan uang. Perusahaan juga wajib mencatat daftar pekerja yang lembur beserta lamanya.</p>
<p>Bila Anda sering lembur jauh melebihi batas 4 jam sehari atau 18 jam seminggu, itu tanda beban kerja perlu dibicarakan. Selain menyangkut hak upah, kelelahan berkepanjangan berisiko bagi kesehatan dan keselamatan kerja.</p>"""),
]

EXTRA["tips-negosiasi-gaji"] = [
    ("Menentukan angka yang akan diajukan", """<p>Misalkan gaji Anda sekarang Rp8.000.000 gross dan riset pasar menunjukkan posisi baru berada di kisaran Rp9–12 juta. Cara menyusun angka:</p>
<ol><li><b>Batas bawah</b>: berapa gaji yang membuat pindah kerja tetap menguntungkan setelah memperhitungkan transportasi, waktu tempuh, dan benefit yang hilang. Misalnya Rp9,5 juta.</li>
<li><b>Angka wajar</b>: titik tengah pasar yang sesuai pengalaman Anda, misalnya Rp10,5 juta.</li>
<li><b>Angka pembuka</b>: sedikit di atas angka wajar agar ada ruang tawar, misalnya kisaran Rp11–12 juta.</li></ol>
<p>Kenaikan saat pindah kerja sering lebih besar daripada kenaikan tahunan di perusahaan yang sama, tetapi tetap harus didukung alasan yang kuat: keahlian, pencapaian, dan tanggung jawab yang lebih besar.</p>"""),
    ("Kesalahan saat negosiasi", """<ul><li><b>Menyebut angka terlalu cepat</b> sebelum memahami lingkup pekerjaan dan benefit.</li>
<li><b>Tidak membedakan gross dan net</b>, sehingga setuju pada angka yang ternyata lebih kecil dari harapan.</li>
<li><b>Berbohong tentang gaji sekarang</b>. Bisa ketahuan dari slip gaji atau bukti potong pajak.</li>
<li><b>Bersikap ultimatum</b> atau membandingkan dengan tawaran lain secara agresif.</li>
<li><b>Langsung menerima</b> tanpa meminta waktu untuk mempertimbangkan. Meminta satu atau dua hari adalah hal yang wajar.</li></ul>"""),
    ("Negosiasi kenaikan gaji di perusahaan sekarang", """<p>Negosiasi tidak hanya terjadi saat pindah kerja. Untuk meminta kenaikan di perusahaan sekarang:</p>
<ul><li><b>Pilih waktu yang tepat</b>, misalnya menjelang penilaian kinerja atau setelah menyelesaikan proyek penting.</li>
<li><b>Siapkan bukti</b>: pencapaian terukur, tanggung jawab tambahan, dan data pasar.</li>
<li><b>Ajukan secara profesional</b> dalam pertemuan khusus, bukan sambil lalu.</li>
<li><b>Siapkan alternatif</b>: bila anggaran belum ada, minta jadwal evaluasi ulang, pelatihan, atau jalur promosi yang jelas.</li></ul>"""),
]

EXTRA["cara-membuat-anggaran-50-30-20"] = [
    ("Contoh anggaran untuk dua kondisi", """<p><b>Lajang di kota besar, gaji bersih Rp6.000.000:</b></p>""" + T(["Pos", "Porsi", "Jumlah", "Contoh isi"], [
        ["Kebutuhan", "55%", "Rp3.300.000", "Kos Rp1,8 juta, makan Rp1 juta, transportasi dan pulsa Rp500 ribu"],
        ["Keinginan", "25%", "Rp1.500.000", "Nongkrong, hiburan, belanja"],
        ["Tabungan & investasi", "20%", "Rp1.200.000", "Dana darurat dulu, lalu reksa dana"]]) + """
<p><b>Keluarga dengan satu anak, gaji bersih gabungan Rp12.000.000:</b></p>""" + T(["Pos", "Porsi", "Jumlah", "Contoh isi"], [
        ["Kebutuhan", "55%", "Rp6.600.000", "Cicilan rumah, belanja dapur, sekolah, listrik, transportasi"],
        ["Keinginan", "20%", "Rp2.400.000", "Makan di luar, liburan, hobi"],
        ["Tabungan & investasi", "25%", "Rp3.000.000", "Dana darurat, dana pendidikan, dana pensiun"]]) + """
<p>Kedua contoh tidak persis 50/30/20. Tidak apa-apa: yang penting tabungan dialokasikan lebih dulu dan pengeluaran tidak melebihi penghasilan.</p>"""),
    ("Metode lain yang bisa dicoba", """<ul><li><b>Anggaran berbasis nol (zero-based)</b>: setiap rupiah penghasilan diberi tugas sampai sisanya nol. Lebih detail, cocok bagi yang suka mencatat.</li>
<li><b>Metode amplop</b>: uang dibagi ke &ldquo;amplop&rdquo; per pos, baik fisik maupun digital. Bila amplop habis, pos itu berhenti untuk bulan tersebut.</li>
<li><b>Bayar diri sendiri dulu</b>: hanya menetapkan persentase tabungan di awal, sisanya bebas dipakai. Paling sederhana untuk pemula.</li></ul>
<p>Pilih metode yang paling mungkin Anda jalankan secara konsisten. Anggaran yang sederhana tetapi dijalankan lebih baik daripada anggaran sempurna yang ditinggalkan.</p>"""),
    ("Menutup kebocoran anggaran", """<p>Kebocoran biasanya berasal dari pengeluaran kecil yang sering: kopi, ongkos kirim, langganan aplikasi yang lupa dihentikan, biaya admin, atau belanja impulsif lewat paylater. Cara mengatasinya:</p>
<ul><li>Periksa mutasi rekening dan e-wallet sebulan terakhir, lalu tandai pengeluaran yang tidak direncanakan.</li>
<li>Hentikan langganan yang jarang dipakai.</li><li>Terapkan aturan tunggu 24 jam sebelum membeli barang yang tidak direncanakan.</li>
<li>Matikan fitur paylater bila sering membuat belanja berlebihan.</li></ul>"""),
]

EXTRA["cara-cek-saldo-dan-klaim-jht"] = [
    ("Ilustrasi pertumbuhan saldo JHT", """<p>Iuran JHT sebesar 5,7% dari upah setiap bulan. Untuk beberapa tingkat upah, iuran yang terkumpul (belum termasuk hasil pengembangan) adalah:</p>""" + T(["Upah per bulan", "Iuran JHT per bulan", "5 tahun", "10 tahun"], [
        ["Rp5.000.000", "Rp285.000", "Rp17,1 juta", "Rp34,2 juta"], ["Rp8.000.000", "Rp456.000", "Rp27,4 juta", "Rp54,7 juta"],
        ["Rp12.000.000", "Rp684.000", "Rp41,0 juta", "Rp82,1 juta"]]) + """
<p>Saldo sebenarnya biasanya lebih besar karena ada hasil pengembangan yang dibukukan setiap tahun dan kenaikan upah dari waktu ke waktu. Riwayat lengkapnya dapat dilihat di aplikasi JMO.</p>"""),
    ("JHT, JP, dan JKP saat berhenti bekerja", T(["Program", "Saat berhenti bekerja", "Bentuk manfaat"], [
        ["JHT", "Saldo dapat dicairkan setelah masa tunggu", "Uang tunai sekaligus"],
        ["JP", "Bila masa iuran belum 15 tahun, iuran beserta hasil pengembangan dapat dibayarkan sekaligus saat usia pensiun; bila sudah, menerima pensiun bulanan", "Pensiun bulanan atau sekaligus sesuai syarat"],
        ["JKP", "Bila terkena PHK dan memenuhi syarat kepesertaan", "Uang tunai beberapa bulan, informasi pasar kerja, pelatihan"]]) + """
<p>JKP hanya untuk pekerja yang terkena PHK, bukan yang mengundurkan diri, dan mensyaratkan masa iuran tertentu. Bila Anda terkena PHK, ajukan JKP terlebih dahulu sesuai batas waktu, karena manfaatnya berbeda dari JHT.</p>"""),
    ("Masalah yang sering menghambat klaim", """<ul><li><b>Data tidak cocok</b> antara KTP, data BPJS, dan rekening bank, misalnya ejaan nama atau tanggal lahir.</li>
<li><b>Kepesertaan ganda</b>: punya lebih dari satu nomor dari beberapa perusahaan. Gabungkan saldo lebih dulu.</li>
<li><b>Perusahaan belum melaporkan</b> bahwa Anda sudah berhenti, sehingga status masih aktif.</li>
<li><b>Iuran menunggak</b> di perusahaan lama, sehingga saldo tidak sesuai harapan.</li>
<li><b>Dokumen tidak jelas</b> saat diunggah, misalnya foto buram.</li></ul>
<p>Sebagian besar masalah ini bisa diselesaikan dengan menghubungi kantor cabang atau layanan pelanggan resmi BPJS Ketenagakerjaan.</p>"""),
]

EXTRA["pinjaman-online-vs-kredit-bank"] = [
    ("Menghitung biaya pinjaman yang sebenarnya", """<p>Contoh pinjaman daring Rp2.000.000 untuk 30 hari dengan biaya 0,2% per hari dan biaya layanan Rp100.000 yang dipotong di awal:</p>""" + T(["Rincian", "Jumlah"], [
        ["Dana yang Anda terima", "Rp1.900.000"], ["Bunga 0,2% × 30 hari × Rp2.000.000", "Rp120.000"], ["Yang harus dikembalikan", "Rp2.120.000"],
        ["=Biaya total untuk menerima Rp1,9 juta", "Rp220.000 (sekitar 11,6% dalam sebulan)"]]) + """
<p>Biaya layanan yang dipotong di awal membuat biaya sebenarnya jauh lebih tinggi dari bunga yang tertulis. Bila terlambat, denda harian menambah beban. Inilah sebabnya pinjaman daring sebaiknya hanya dipakai untuk kebutuhan mendesak dengan kepastian bisa dilunasi tepat waktu.</p>"""),
    ("Alternatif sebelum meminjam", """<ul><li><b>Dana darurat</b>, inilah fungsinya.</li><li><b>Menjual barang yang tidak terpakai.</b></li>
<li><b>Kasbon ke kantor</b> atau koperasi karyawan, yang biasanya tanpa atau dengan bunga rendah.</li>
<li><b>Bernegosiasi jadwal pembayaran</b> dengan pihak yang ditagih, misalnya sekolah atau rumah sakit.</li>
<li><b>Pinjaman dari keluarga</b> dengan kesepakatan tertulis yang jelas.</li>
<li><b>KTA bank atau kartu kredit</b> bila memiliki akses dan mampu membayar sesuai jadwal.</li></ul>"""),
    ("Bila utang sudah menumpuk", """<p>Bila Anda memiliki beberapa utang sekaligus, susun strategi pelunasan:</p>
<ol><li><b>Catat semua utang</b>: sisa pokok, bunga, cicilan, dan tanggal jatuh tempo.</li>
<li><b>Hentikan utang baru</b>, termasuk gali lubang tutup lubang.</li>
<li><b>Pilih urutan pelunasan</b>: metode <i>avalanche</i> (bunga tertinggi dulu) paling hemat biaya; metode <i>snowball</i> (saldo terkecil dulu) memberi semangat karena cepat terlihat hasilnya.</li>
<li><b>Bayar minimum di semua utang</b> agar tidak kena denda, lalu alokasikan sisa dana ke utang prioritas.</li>
<li><b>Ajukan restrukturisasi</b> ke pemberi pinjaman resmi bila memang tidak mampu, sebelum menunggak lama.</li></ol>"""),
]

EXTRA["take-over-dan-pelunasan-kpr"] = [
    ("Contoh menghitung titik impas take over", """<p>Melanjutkan contoh di atas: take over menghemat cicilan sekitar <b>Rp684.000 per bulan</b>. Misalkan total biaya take over (penalti, provisi, appraisal, notaris, asuransi) sekitar <b>Rp15.000.000</b>.</p>
<div class="formula">Titik impas = Biaya take over ÷ penghematan per bulan
            = Rp15.000.000 ÷ Rp684.000 ≈ 22 bulan</div>
<p>Artinya, take over baru menguntungkan bila Anda akan mempertahankan KPR lebih dari sekitar 22 bulan dan bunga di bank baru benar-benar lebih rendah selama periode tersebut. Ingat juga bahwa bunga promosi bank baru biasanya hanya beberapa tahun, setelah itu berubah menjadi floating.</p>"""),
    ("Pelunasan sebagian: turunkan cicilan atau persingkat tenor?", """<p>Sisa pokok Rp400 juta, bunga 11%, sisa tenor 12 tahun, cicilan Rp5.014.221. Anda melunasi sebagian sebesar <b>Rp50 juta</b>:</p>""" + T(["Pilihan", "Cicilan", "Lama", "Total bunga sisa"], [
        ["Tanpa pelunasan", "Rp5.014.221", "144 bulan", "sekitar Rp322,0 juta"],
        ["Cicilan turun, tenor tetap", "Rp4.387.443", "144 bulan", "sekitar Rp281,8 juta"],
        ["Cicilan tetap, tenor dipersingkat", "Rp5.014.221", "112 bulan", "sekitar Rp211,6 juta"]]) + """
<p>Mempersingkat tenor menghemat bunga sekitar Rp110 juta, jauh lebih besar daripada menurunkan cicilan (sekitar Rp40 juta). Pilih menurunkan cicilan hanya bila arus kas bulanan Anda memang perlu dilonggarkan.</p>"""),
    ("Langkah-langkah proses take over", """<ol><li>Minta <b>surat keterangan sisa pinjaman</b> dan ketentuan penalti dari bank lama.</li>
<li>Ajukan take over ke bank baru dengan dokumen pribadi, penghasilan, dan dokumen KPR lama.</li>
<li>Bank baru melakukan <b>appraisal</b> dan memeriksa riwayat kredit.</li>
<li>Bila disetujui, bank baru <b>melunasi</b> sisa pinjaman ke bank lama.</li>
<li>Sertifikat diambil dari bank lama, dilakukan <b>roya</b>, lalu dibebani hak tanggungan baru untuk bank baru.</li>
<li>Anda mulai membayar cicilan ke bank baru.</li></ol>"""),
]

EXTRA["mengenal-sbn-ritel"] = [
    ("Contoh perhitungan kupon", """<p>Misalkan Anda membeli SBN ritel sebesar <b>Rp10.000.000</b> dengan kupon tetap 6% per tahun yang dibayar setiap bulan (angka kupon hanya contoh; setiap seri memiliki kupon sendiri):</p>""" + T(["Rincian", "Jumlah"], [
        ["Kupon kotor setahun (6% × Rp10 juta)", "Rp600.000"], ["Pajak final 10%", "Rp60.000"], ["=Kupon bersih setahun", "Rp540.000"], ["=Kupon bersih per bulan", "Rp45.000"]]) + """
<p>Bandingkan dengan deposito berbunga 6% per tahun: setelah pajak 20%, hasil bersihnya Rp480.000 per tahun. Dengan kupon yang sama, SBN memberi hasil bersih lebih besar karena tarif pajaknya lebih rendah. Pokok Rp10 juta dikembalikan utuh saat jatuh tempo.</p>"""),
    ("SBN ritel, deposito, dan reksa dana", T(["Aspek", "SBN ritel", "Deposito", "Reksa dana pasar uang"], [
        ["Penjamin", "Negara", "LPS (dengan syarat)", "Tidak dijamin"], ["Pajak hasil", "10% final", "20% final", "Bukan objek pajak bagi investor"],
        ["Pencairan", "Sesuai jenis seri", "Saat jatuh tempo", "Kapan saja di hari bursa"], ["Minimal", "Umumnya Rp1 juta", "Bervariasi", "Bisa sangat kecil"],
        ["Cocok untuk", "Tujuan 2–6 tahun", "Tujuan pasti jangka pendek", "Dana darurat dan jangka pendek"]])),
    ("Langkah membeli SBN ritel", """<ol><li><b>Pilih mitra distribusi</b> resmi (bank, sekuritas, atau platform investasi) yang tercantum di situs Kementerian Keuangan.</li>
<li><b>Daftar dan verifikasi</b> data diri, termasuk rekening dana dan rekening surat berharga.</li>
<li><b>Pantau jadwal penawaran</b> seri yang Anda incar, beserta kupon dan tenornya.</li>
<li><b>Pesan saat masa penawaran</b>, lalu bayar dengan kode billing sebelum batas waktu.</li>
<li><b>Simpan bukti kepemilikan</b>. Kupon akan masuk ke rekening Anda sesuai jadwal.</li></ol>"""),
]

EXTRA["reksa-dana-vs-deposito"] = [
    ("Ilustrasi: Rp10 juta selama satu tahun", """<p>Berikut gambaran sederhana bila dana Rp10 juta disimpan selama satu tahun. Angka reksa dana hanya ilustrasi, bukan janji hasil:</p>""" + T(["Pilihan", "Asumsi", "Perkiraan hasil bersih"], [
        ["Deposito", "Bunga 4% per tahun, pajak 20%", "Rp320.000, pasti"],
        ["Reksa dana pasar uang", "Imbal 4–5% per tahun", "Rp400.000–Rp500.000, bisa berbeda"],
        ["Reksa dana saham", "Bisa −15% sampai +20% dalam setahun", "−Rp1,5 juta sampai +Rp2 juta"]]) + """
<p>Untuk jangka waktu satu tahun, reksa dana saham terlalu berisiko karena bisa saja sedang turun saat dana dibutuhkan. Untuk lima tahun atau lebih, peluang reksa dana saham memberi hasil lebih tinggi menjadi lebih besar, walaupun tetap tidak dijamin.</p>"""),
    ("Cara membaca fund fact sheet", """<p><b>Fund fact sheet</b> adalah ringkasan bulanan reksa dana. Bagian yang perlu diperhatikan:</p>
<ul><li><b>Kebijakan investasi</b>: komposisi aset, misalnya persentase saham dan obligasi.</li>
<li><b>Kinerja</b>: hasil 1 bulan, 1 tahun, 3 tahun, dan sejak diluncurkan, dibandingkan tolok ukur (benchmark).</li>
<li><b>Dana kelolaan</b>: reksa dana dengan dana kelolaan sangat kecil berisiko dibubarkan.</li>
<li><b>Biaya</b>: biaya pembelian, penjualan, pengalihan, dan biaya pengelolaan tahunan.</li>
<li><b>Bank kustodian</b> dan <b>manajer investasi</b>: pastikan terdaftar dan diawasi OJK.</li>
<li><b>Klasifikasi risiko</b>: rendah, sedang, atau tinggi.</li></ul>"""),
    ("Kesalahan pemula saat memilih", """<ul><li><b>Memilih hanya dari kinerja satu bulan terakhir</b>, padahal kinerja masa lalu tidak menjamin kinerja masa depan.</li>
<li><b>Mencairkan reksa dana saham saat turun</b> karena panik, sehingga kerugian menjadi nyata.</li>
<li><b>Menyimpan dana jangka pendek di reksa dana saham</b>.</li>
<li><b>Mengira reksa dana dijamin LPS</b> seperti deposito.</li>
<li><b>Membeli di aplikasi yang tidak terdaftar</b> di OJK.</li></ul>"""),
]

EXTRA["berapa-dana-darurat-yang-ideal"] = [
    ("Contoh menghitung pengeluaran wajib", """<p>Dana darurat dihitung dari pengeluaran yang <b>tetap harus dibayar</b> walaupun penghasilan berhenti. Contoh untuk keluarga kecil:</p>""" + T(["Pos pengeluaran wajib", "Per bulan"], [
        ["Sewa atau cicilan rumah", "Rp2.000.000"], ["Makan dan kebutuhan dapur", "Rp2.500.000"], ["Listrik, air, internet, pulsa", "Rp700.000"],
        ["Transportasi", "Rp600.000"], ["Sekolah anak", "Rp800.000"], ["Cicilan utang minimum dan asuransi", "Rp900.000"], ["=Total pengeluaran wajib", "Rp7.500.000"]]) + """
<p>Dengan status menikah dan satu anak, target dana darurat sekitar 6–9 kali, yaitu <b>Rp45–67,5 juta</b>. Pengeluaran seperti hiburan, liburan, dan belanja tidak perlu masuk hitungan karena bisa dihentikan sementara dalam keadaan darurat.</p>"""),
    ("Kapan dana darurat boleh dipakai?", """<p>Tanyakan tiga hal sebelum memakai dana darurat:</p>
<ul><li><b>Apakah tidak terduga?</b> Biaya sekolah tahunan atau pajak kendaraan bisa direncanakan, jadi bukan darurat.</li>
<li><b>Apakah penting?</b> Kebutuhan kesehatan, tempat tinggal, dan penghasilan yang hilang termasuk penting. Gawai baru tidak.</li>
<li><b>Apakah mendesak?</b> Bila bisa ditunda dan ditabung dalam beberapa bulan, sebaiknya tidak memakai dana darurat.</li></ul>
<p>Bila ketiga jawaban &ldquo;ya&rdquo;, pakailah tanpa ragu. Itulah gunanya dana darurat. Setelah itu, prioritaskan untuk mengisinya kembali.</p>"""),
    ("Dana darurat, asuransi, dan investasi", T(["", "Dana darurat", "Asuransi", "Investasi"], [
        ["Fungsi", "Menutup kebutuhan mendesak jangka pendek", "Memindahkan risiko besar ke perusahaan asuransi", "Menumbuhkan uang untuk tujuan jangka panjang"],
        ["Contoh risiko", "Kehilangan pekerjaan, perbaikan mendadak", "Sakit berat, kecelakaan, meninggal dunia", "–"],
        ["Ketersediaan dana", "Kapan saja", "Saat klaim disetujui", "Bisa sedang turun nilainya"],
        ["Urutan", "Pertama", "Bersamaan atau setelah dana darurat awal", "Setelah keduanya memadai"]]) + """
<p>Ketiganya saling melengkapi. Dana darurat menjaga Anda dari kejadian kecil sampai menengah, asuransi melindungi dari kejadian besar, dan investasi membangun masa depan.</p>"""),
]

# Kesimpulan (bagian penutup) dan FAQ tambahan per artikel
CLOSE = {
    "apa-itu-pph-21-ter": ("""<p>PPh 21 dengan metode TER pada dasarnya hanya mengubah cara pajak dipotong setiap bulan, bukan besar pajak setahun. Januari sampai November dipotong dengan tarif sederhana berdasarkan bruto bulanan, lalu Desember menjadi bulan penyesuaian dengan tarif Pasal 17. Dengan memahami bruto, PTKP, biaya jabatan, dan kategori TER, Anda bisa memeriksa sendiri apakah potongan di slip gaji sudah wajar, merencanakan bulan bonus, dan tidak kaget ketika slip Desember berbeda.</p>""",
        [("Apakah tunjangan makan dan transport ikut kena TER?", "Ya, bila dibayarkan dalam bentuk uang. Semua penghasilan bulan itu dijumlahkan menjadi bruto, lalu dikalikan tarif TER."),
         ("Apakah karyawan kontrak juga memakai TER?", "Pegawai tetap dan pegawai tidak tetap yang dibayar bulanan memakai TER bulanan. Pegawai tidak tetap yang dibayar harian atau mingguan memakai TER harian dengan ketentuan tersendiri.")]),
    "cara-membaca-slip-gaji": ("""<p>Slip gaji adalah ringkasan hubungan finansial Anda dengan perusahaan setiap bulan. Dengan memahami bedanya gaji pokok, tunjangan tetap, dan tunjangan tidak tetap, serta potongan BPJS dan PPh 21, Anda bisa memastikan hak terpenuhi dan menyusun anggaran dari angka yang benar-benar diterima. Biasakan memeriksa slip setiap bulan dan menyimpannya dengan rapi.</p>""",
        [("Kenapa gaji bersih saya berubah padahal gaji pokok sama?", "Bisa karena lembur, tunjangan tidak tetap, potongan absensi, perubahan iuran BPJS, atau tarif TER yang berbeda karena bruto bulan itu berubah."),
         ("Bolehkah perusahaan memotong gaji tanpa persetujuan?", "Potongan di luar kewajiban hukum seperti pajak dan BPJS umumnya harus didasarkan pada perjanjian kerja, peraturan perusahaan, atau persetujuan tertulis pekerja.")]),
    "aturan-thr-dan-tips-mengelolanya": ("""<p>THR adalah hak yang jelas aturannya: minimal satu bulan upah untuk masa kerja 12 bulan atau lebih, dan proporsional untuk masa kerja yang lebih pendek, dibayar paling lambat tujuh hari sebelum hari raya. Karena potongan pajaknya bisa melonjak, susun rencana dari THR bersih. Dengan pembagian yang jelas antara kebutuhan hari raya, berbagi, dan tabungan, THR bisa membawa kebahagiaan tanpa meninggalkan beban setelah lebaran.</p>""",
        [("Apakah THR boleh dibayar dalam bentuk barang?", "THR wajib dibayar dalam bentuk uang rupiah. Pemberian barang seperti parsel tidak menggantikan kewajiban THR."),
         ("Apakah THR dihitung dari upah setelah dipotong BPJS?", "Tidak. THR dihitung dari upah satu bulan, yaitu gaji pokok ditambah tunjangan tetap, sebelum potongan apa pun.")]),
    "mengenal-bpjs-kesehatan-dan-ketenagakerjaan": ("""<p>Iuran BPJS yang dipotong dari gaji bukan sekadar beban. Di baliknya ada perlindungan kesehatan untuk keluarga, tabungan hari tua, pensiun bulanan, perlindungan kecelakaan kerja, santunan kematian, dan bantuan saat kehilangan pekerjaan. Pastikan kepesertaan aktif, data keluarga lengkap, dan upah yang dilaporkan sesuai, agar seluruh manfaat ini benar-benar bisa Anda gunakan saat dibutuhkan.</p>""",
        [("Apakah anak yang sudah bekerja tetap ikut BPJS Kesehatan orang tua?", "Tidak. Anak yang sudah bekerja didaftarkan oleh pemberi kerjanya sendiri. Tanggungan anak juga dibatasi usia tertentu dan status belum menikah."),
         ("Bagaimana jika perusahaan tidak mendaftarkan saya ke BPJS?", "Pemberi kerja wajib mendaftarkan pekerjanya. Anda dapat melaporkan ke BPJS atau dinas ketenagakerjaan setempat.")]),
    "panduan-kpr-rumah-pertama": ("""<p>KPR membuat rumah pertama lebih cepat terjangkau, tetapi juga merupakan komitmen keuangan belasan sampai puluhan tahun. Kuncinya ada pada persiapan: DP yang cukup, cicilan yang tetap aman saat bunga floating naik, biaya awal yang sudah dihitung, dan riwayat kredit yang bersih. Simulasikan beberapa skenario sebelum memilih rumah, sehingga keputusan Anda didasarkan pada angka, bukan sekadar promosi.</p>""",
        [("Apakah freelancer bisa mengajukan KPR?", "Bisa, dengan bukti penghasilan seperti rekening koran beberapa bulan atau tahun terakhir, kontrak kerja, dan laporan pajak. Persyaratannya biasanya lebih ketat daripada karyawan."),
         ("Apakah penghasilan suami dan istri bisa digabung?", "Umumnya bisa (joint income), sehingga plafon yang disetujui bisa lebih besar. Keduanya akan diperiksa riwayat kreditnya.")]),
    "bunga-flat-vs-efektif-kredit-kendaraan": ("""<p>Bunga flat dan bunga efektif adalah dua cara menulis biaya pinjaman yang tidak bisa dibandingkan secara langsung. Ubah selalu ke bunga efektif, hitung total pembayaran, dan perhitungkan biaya lain seperti asuransi dan administrasi. Dengan cara ini Anda bisa memilih penawaran yang benar-benar paling murah dan menjaga cicilan kendaraan tetap sehat bagi keuangan keluarga.</p>""",
        [("Apakah bunga flat selalu lebih mahal?", "Tidak selalu. Yang menentukan adalah bunga efektif setaranya. Bunga flat rendah bisa setara dengan bunga efektif yang kompetitif."),
         ("Apakah bunga kredit kendaraan bisa berubah di tengah jalan?", "Pada kredit dengan bunga flat, cicilan biasanya tetap sampai lunas. Baca perjanjian untuk memastikan tidak ada ketentuan penyesuaian bunga.")]),
    "panduan-deposito-untuk-pemula": ("""<p>Deposito cocok untuk menyimpan dana dengan tujuan dan jangka waktu yang jelas, dengan bunga pasti dan risiko rendah. Hasil bersihnya dipengaruhi pajak 20% dan inflasi, sedangkan keamanannya bergantung pada syarat penjaminan LPS. Pilih bank yang tepat, cocokkan tenor dengan kebutuhan, dan pertimbangkan strategi tangga agar dana tetap mudah dijangkau.</p>""",
        [("Apakah bunga deposito bisa diambil setiap bulan?", "Bisa. Beberapa bank menawarkan pembayaran bunga bulanan ke rekening tabungan, terutama untuk tenor panjang."),
         ("Apakah deposito di bank digital aman?", "Aman bila bank tersebut berizin OJK, peserta LPS, dan bunga yang Anda terima tidak melebihi tingkat bunga penjaminan LPS.")]),
    "bunga-majemuk-dan-investasi-rutin": ("""<p>Bunga majemuk bekerja paling baik bila diberi waktu. Mulai sedini mungkin, berinvestasi rutin, naikkan setoran seiring kenaikan penghasilan, dan pilih instrumen sesuai jangka waktu serta profil risiko. Siapkan dana darurat lebih dulu, gunakan produk yang diawasi OJK, dan tetap tenang saat pasar naik-turun. Konsistensi jauh lebih menentukan daripada menebak waktu terbaik untuk masuk.</p>""",
        [("Berapa minimal investasi yang masuk akal untuk pemula?", "Mulailah dari jumlah yang tidak mengganggu kebutuhan bulanan, bahkan Rp100.000. Yang terpenting adalah kebiasaan rutin dan kenaikan bertahap."),
         ("Apakah perlu memantau investasi setiap hari?", "Untuk investasi jangka panjang tidak perlu. Evaluasi beberapa bulan sekali atau setahun sekali sudah cukup, sambil memastikan tujuan dan alokasi masih sesuai.")]),
    "cara-lapor-spt-tahunan-karyawan": ("""<p>Melapor SPT Tahunan adalah kewajiban rutin yang sebenarnya sederhana bagi karyawan dengan satu pemberi kerja. Siapkan bukti potong dan daftar harta-utang sejak awal tahun, laporkan melalui Coretax sebelum 31 Maret, dan simpan bukti penerimaan elektroniknya. Bila ada penghasilan lain atau pindah kerja, hitung ulang pajak setahun agar tidak terjadi kurang bayar.</p>""",
        [("Apakah suami dan istri lapor SPT sendiri-sendiri?", "Tergantung status perpajakan keluarga. Istri yang memilih menjalankan kewajiban pajak sendiri (atau pisah harta) melapor SPT sendiri; bila kewajiban pajak keluarga digabung, penghasilan istri dilaporkan dalam SPT suami. Periksa status yang tercatat di Coretax."),
         ("Apa yang terjadi bila tidak lapor SPT?", "Ada sanksi administrasi berupa denda, dan status kepatuhan pajak Anda tercatat kurang baik, yang dapat memengaruhi layanan tertentu.")]),
    "cara-menghitung-upah-lembur": ("""<p>Upah lembur dihitung dengan rumus yang jelas: upah sejam sebesar 1/173 upah sebulan, dengan kelipatan 1,5 sampai 4 kali tergantung jam dan hari. Mencatat jam lembur, meminta perintah tertulis, dan memeriksa slip gaji adalah cara sederhana untuk memastikan hak Anda terpenuhi, sekaligus menjaga agar lembur tidak melebihi batas yang aman bagi kesehatan.</p>""",
        [("Apakah lembur di hari libur nasional sama dengan hari Minggu?", "Ya, keduanya termasuk lembur pada hari istirahat atau libur resmi dengan kelipatan yang sama, sesuai pola 5 atau 6 hari kerja."),
         ("Apakah karyawan kontrak berhak atas upah lembur?", "Ya. Ketentuan lembur berlaku bagi pekerja dengan hubungan kerja, baik tetap maupun kontrak.")]),
    "tips-negosiasi-gaji": ("""<p>Negosiasi gaji yang baik dimulai dari riset, bukan perasaan. Pahami kisaran pasar, bedakan gross dan net, hitung nilai benefit, dan sampaikan angka dengan alasan yang kuat dan sikap profesional. Angka yang disepakati di awal akan memengaruhi THR, BPJS, dan kenaikan gaji selama bertahun-tahun, sehingga persiapan beberapa jam sangat sepadan.</p>""",
        [("Kapan waktu terbaik membicarakan gaji?", "Biasanya setelah perusahaan menunjukkan minat serius, misalnya di tahap akhir wawancara atau saat menerima penawaran."),
         ("Bagaimana jika penawaran di bawah ekspektasi?", "Sampaikan terima kasih, jelaskan alasan angka yang Anda harapkan, dan tanyakan apakah ada fleksibilitas dalam gaji atau benefit lain.")]),
    "cara-membuat-anggaran-50-30-20": ("""<p>Metode 50/30/20 memberi kerangka sederhana untuk mengatur gaji: kebutuhan, keinginan, dan tabungan. Angkanya boleh disesuaikan, asalkan tabungan dialokasikan lebih dulu dan pengeluaran tidak melebihi penghasilan. Mulailah dari gaji bersih yang akurat, catat pengeluaran beberapa bulan, lalu evaluasi secara rutin. Kebiasaan kecil yang konsisten akan membawa perubahan besar.</p>""",
        [("Apakah zakat atau sedekah masuk kebutuhan atau keinginan?", "Banyak orang memisahkannya sebagai pos tersendiri di awal, sebelum membagi sisa penghasilan ke 50/30/20."),
         ("Bagaimana bila 50% tidak cukup untuk kebutuhan?", "Kurangi porsi keinginan lebih dulu, cari cara menurunkan biaya tetap, atau tingkatkan penghasilan. Usahakan tabungan tetap ada walaupun kecil.")]),
    "cara-cek-saldo-dan-klaim-jht": ("""<p>Saldo JHT adalah hasil kerja Anda bertahun-tahun. Periksa secara berkala lewat kanal resmi, pastikan data dan upah yang dilaporkan benar, dan cairkan hanya ketika benar-benar dibutuhkan. Bila pindah kerja, menggabungkan saldo ke kepesertaan baru sering menjadi pilihan terbaik agar dana terus berkembang untuk hari tua.</p>""",
        [("Apakah klaim JHT dikenai biaya?", "Klaim melalui kanal resmi BPJS Ketenagakerjaan tidak dipungut biaya. Pajak final dipotong bila saldo melebihi Rp50 juta."),
         ("Bisakah klaim JHT diwakilkan?", "Untuk peserta yang meninggal, klaim diajukan ahli waris. Untuk kondisi lain, ikuti ketentuan resmi terbaru mengenai kuasa dan dokumen pendukung.")]),
    "pinjaman-online-vs-kredit-bank": ("""<p>Pinjaman daring menawarkan kecepatan, tetapi dengan biaya yang jauh lebih tinggi daripada kredit bank. Bandingkan dalam satuan yang sama, hitung total pengembalian, dan pastikan pemberi pinjaman terdaftar di OJK. Utamakan dana darurat dan alternatif lain sebelum meminjam, dan bila utang sudah menumpuk, susun strategi pelunasan secepatnya.</p>""",
        [("Apakah semua pinjaman daring legal?", "Tidak. Hanya platform yang berizin OJK yang legal. Cek daftar resminya sebelum mengajukan pinjaman."),
         ("Bagaimana cara cek riwayat kredit saya?", "Anda dapat mengajukan permintaan informasi debitur (SLIK) melalui layanan resmi OJK untuk melihat riwayat pinjaman yang tercatat.")]),
    "take-over-dan-pelunasan-kpr": ("""<p>Take over dan pelunasan dipercepat adalah dua cara efektif meringankan beban KPR, terutama saat bunga floating tinggi. Hitung titik impas take over dengan memasukkan semua biaya, dan bila melunasi sebagian, pertimbangkan mempersingkat tenor untuk penghematan bunga terbesar. Tetap jaga dana darurat dan minta simulasi tertulis sebelum mengambil keputusan.</p>""",
        [("Apakah take over bisa dilakukan berkali-kali?", "Bisa, tetapi setiap kali ada biaya. Lakukan hanya bila selisih bunga dan sisa tenor cukup besar untuk menutup biaya tersebut."),
         ("Apakah pelunasan sebagian mengubah masa bunga fixed?", "Biasanya tidak, tetapi bank dapat mengenakan penalti selama masa fixed. Tanyakan ketentuannya sebelum melunasi.")]),
    "mengenal-sbn-ritel": ("""<p>SBN ritel memberi cara sederhana dan aman untuk berinvestasi sambil membiayai pembangunan, dengan pembayaran kupon dan pokok yang dijamin negara serta pajak yang lebih rendah daripada deposito. Pilih seri sesuai tujuan dan pandangan Anda terhadap suku bunga, beli melalui mitra distribusi resmi, dan jadikan SBN bagian dari portofolio yang seimbang.</p>""",
        [("Apakah kupon SBN bisa berubah?", "Untuk seri kupon tetap seperti ORI dan SR, kupon tidak berubah. Untuk SBR dan ST, kupon mengikuti suku bunga acuan dengan batas bawah tertentu."),
         ("Apakah SBN ritel bisa dijadikan jaminan?", "Beberapa seri dapat diagunkan sesuai ketentuan masing-masing seri. Cek memorandum informasi seri yang Anda beli.")]),
    "reksa-dana-vs-deposito": ("""<p>Deposito dan reksa dana tidak harus dipilih salah satu. Deposito memberi kepastian dan penjaminan untuk tujuan jangka pendek yang pasti, sedangkan reksa dana memberi fleksibilitas dan potensi hasil lebih tinggi sesuai jenisnya. Cocokkan pilihan dengan tujuan, jangka waktu, dan profil risiko, lalu bandingkan hasil bersih setelah pajak dan biaya.</p>""",
        [("Berapa lama dana reksa dana cair setelah dijual?", "Umumnya beberapa hari kerja setelah penjualan, tergantung jenis reksa dana dan ketentuan manajer investasi."),
         ("Apakah reksa dana syariah berbeda?", "Reksa dana syariah berinvestasi pada efek yang sesuai prinsip syariah dan diawasi Dewan Pengawas Syariah. Cara kerja dan risikonya mirip dengan jenis konvensional sejenis.")]),
    "berapa-dana-darurat-yang-ideal": ("""<p>Dana darurat adalah fondasi yang membuat rencana keuangan lain tetap berjalan saat terjadi hal tak terduga. Hitung dari pengeluaran wajib, sesuaikan dengan status dan kestabilan penghasilan, simpan di tempat yang aman dan mudah dicairkan, lalu isi kembali setiap kali terpakai. Mulai dari target kecil pun sudah jauh lebih baik daripada tidak memilikinya sama sekali.</p>""",
        [("Apakah dana darurat boleh disimpan dalam emas?", "Emas bisa menjadi pelengkap, tetapi harganya naik-turun dan ada selisih harga jual-beli. Sebaiknya sebagian besar dana darurat tetap di tabungan atau reksa dana pasar uang."),
         ("Apakah suami dan istri perlu dana darurat terpisah?", "Tidak harus. Yang penting total dana darurat keluarga cukup untuk pengeluaran wajib rumah tangga sesuai target.")]),
}
