(function () {
  var U = UI;
  U.init(function () {
    var g = U.val('gaji'), tt = U.val('tidakTetap'), r = FIN.gajiBersih({gaji: g, tidakTetap: tt, status: U.val('status'), bpjs: U.bpjsOpts()}), b = r.pph.bpjs;
    var h = '<div class="kpis">' + U.kpi('Gaji bersih bulan biasa', U.rp(r.thp), 'main') + U.kpi('Rata-rata setahun', U.rp(r.thpRata))
      + U.kpi('Total potongan', U.rp(r.potonganBpjs + r.pajak)) + U.kpi('Biaya perusahaan', U.rp(r.biayaPerusahaan)) + '</div>';
    h += '<h3>Rincian slip gaji (bulan Januari–November)</h3>' + U.table(['Komponen', 'Per bulan'], [
      U.row(['Gaji pokok + tunjangan tetap', U.rp(g)]), U.row(['Tunjangan tidak tetap', U.rp(tt)]), U.row(['Gaji kotor', U.rp(r.gajiKotor)], 'tot'),
      U.row(['− BPJS Kesehatan (1%)', U.rp(b.kes.employee)]), U.row(['− JHT (2%)', U.rp(b.jht.employee)]), U.row(['− JP (1%)', U.rp(b.jp.employee)]),
      U.row(['− PPh 21 (TER ' + r.pph.kategori + ' ' + U.pct(r.pph.terRate) + ' × bruto ' + U.rp(r.pph.brutoBulan) + ')', U.rp(r.pajak)]),
      U.row(['Gaji bersih diterima', U.rp(r.thp)], 'tot')]);
    h += '<div class="note info">PPh 21 setahun ' + U.rp(r.pph.pajakSetahun) + ', sehingga potongan Desember ' + U.rp(r.pph.pajakDes)
      + '. Rata-rata gaji bersih per bulan sepanjang tahun: <b>' + U.rp(r.thpRata) + '</b>.</div>';
    h += '<h3>Iuran yang dibayar perusahaan</h3>' + U.table(['Program', 'Per bulan'], [
      U.row(['BPJS Kesehatan (4%)', U.rp(b.kes.employer)]), U.row(['JHT (3,7%)', U.rp(b.jht.employer)]), U.row(['JP (2%)', U.rp(b.jp.employer)]),
      U.row(['JKK (' + U.pct(b.jkk.rate) + ')', U.rp(b.jkk.employer)]), U.row(['JKM (0,3%)', U.rp(b.jkm.employer)]),
      U.row(['Total iuran perusahaan', U.rp(b.totalEmployer)], 'tot'), U.row(['Biaya total karyawan bagi perusahaan', U.rp(r.biayaPerusahaan)], 'tot')]);
    U.$('res').innerHTML = h;
  });
})();
