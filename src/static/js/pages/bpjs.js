(function () {
  var U = UI;
  U.init(function () {
    var b = FIN.bpjs(U.val('gaji'), U.bpjsOpts());
    var h = '<div class="kpis">' + U.kpi('Dipotong dari gaji', U.rp(b.totalEmployee), 'main') + U.kpi('Ditanggung perusahaan', U.rp(b.totalEmployer))
      + U.kpi('Total iuran per bulan', U.rp(b.totalEmployee + b.totalEmployer)) + '</div>';
    var R = function (n, x, re, rk) { return U.row([n, U.rp(x.base), re, U.rp(x.employer), rk, U.rp(x.employee)]); };
    h += U.table(['Program', 'Dasar upah', 'Tarif perusahaan', 'Perusahaan', 'Tarif karyawan', 'Karyawan'], [
      R('BPJS Kesehatan', b.kes, '4%', '1%'), R('JHT', b.jht, '3,7%', '2%'), R('JP', b.jp, '2%', '1%'), R('JKK', b.jkk, U.pct(b.jkk.rate), '–'), R('JKM', b.jkm, '0,3%', '–'),
      U.row(['Total', '', '', U.rp(b.totalEmployer), '', U.rp(b.totalEmployee)], 'tot')]);
    var caps = [];
    if (U.val('gaji') > FIN.RULES.kesCap) caps.push('BPJS Kesehatan dihitung dari batas upah ' + U.rp(FIN.RULES.kesCap));
    if (U.val('gaji') > FIN.RULES.jpCap) caps.push('JP dihitung dari batas upah ' + U.rp(FIN.RULES.jpCap));
    if (caps.length) h += '<div class="note info">' + caps.join('; ') + '.</div>';
    h += '<div class="note info">Setahun: potongan karyawan ' + U.rp(b.totalEmployee * 12) + ', iuran perusahaan ' + U.rp(b.totalEmployer * 12) + '.</div>';
    U.$('res').innerHTML = h;
  });
})();
