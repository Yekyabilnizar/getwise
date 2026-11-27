(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var g = U.val('gaji'), tt = U.val('tidakTetap'), r = FIN.gajiBersih({gaji: g, tidakTetap: tt, status: U.val('status'), bpjs: U.bpjsOpts()}), b = r.pph.bpjs;
    var h = '<div class="kpis">' + U.kpi(T('Gaji bersih bulan biasa', 'Take-home pay, normal month'), U.rp(r.thp), 'main') + U.kpi(T('Rata-rata setahun', 'Annual average'), U.rp(r.thpRata))
      + U.kpi(T('Total potongan', 'Total deductions'), U.rp(r.potonganBpjs + r.pajak)) + U.kpi(T('Biaya perusahaan', 'Cost to employer'), U.rp(r.biayaPerusahaan)) + '</div>';
    h += '<h3>' + T('Rincian slip gaji (bulan Januari–November)', 'Payslip breakdown (January–November)') + '</h3>' + U.table([T('Komponen', 'Component'), T('Per bulan', 'Per month')], [
      U.row([T('Gaji pokok + tunjangan tetap', 'Base salary + fixed allowances'), U.rp(g)]), U.row([T('Tunjangan tidak tetap', 'Variable allowances'), U.rp(tt)]), U.row([T('Gaji kotor', 'Gross salary'), U.rp(r.gajiKotor)], 'tot'),
      U.row([T('− BPJS Kesehatan (1%)', '− BPJS Health (1%)'), U.rp(b.kes.employee)]), U.row(['− JHT (2%)', U.rp(b.jht.employee)]), U.row(['− JP (1%)', U.rp(b.jp.employee)]),
      U.row(['− PPh 21 (TER ' + r.pph.kategori + ' ' + U.pct(r.pph.terRate) + ' × ' + T('bruto ', 'gross ') + U.rp(r.pph.brutoBulan) + ')', U.rp(r.pajak)]),
      U.row([T('Gaji bersih diterima', 'Take-home pay'), U.rp(r.thp)], 'tot')]);
    h += '<div class="note info">' + T('PPh 21 setahun ', 'Annual PPh 21 is ') + U.rp(r.pph.pajakSetahun) + T(', sehingga potongan Desember ', ', so December withholding is ') + U.rp(r.pph.pajakDes)
      + T('. Rata-rata gaji bersih per bulan sepanjang tahun: <b>', '. Average monthly take-home pay over the year: <b>') + U.rp(r.thpRata) + '</b>.</div>';
    h += '<h3>' + T('Iuran yang dibayar perusahaan', 'Contributions paid by the employer') + '</h3>' + U.table([T('Program', 'Program'), T('Per bulan', 'Per month')], [
      U.row([T('BPJS Kesehatan (4%)', 'BPJS Health (4%)'), U.rp(b.kes.employer)]), U.row([T('JHT (3,7%)', 'JHT (3.7%)'), U.rp(b.jht.employer)]), U.row(['JP (2%)', U.rp(b.jp.employer)]),
      U.row(['JKK (' + U.pct(b.jkk.rate) + ')', U.rp(b.jkk.employer)]), U.row([T('JKM (0,3%)', 'JKM (0.3%)'), U.rp(b.jkm.employer)]),
      U.row([T('Total iuran perusahaan', 'Total employer contributions'), U.rp(b.totalEmployer)], 'tot'), U.row([T('Biaya total karyawan bagi perusahaan', 'Total cost of the employee to the employer'), U.rp(r.biayaPerusahaan)], 'tot')]);
    U.$('res').innerHTML = h;
  });
})();
