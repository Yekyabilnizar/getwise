(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var b = FIN.bpjs(U.val('gaji'), U.bpjsOpts());
    var h = '<div class="kpis">' + U.kpi(T('Dipotong dari gaji', 'Deducted from salary'), U.rp(b.totalEmployee), 'main') + U.kpi(T('Ditanggung perusahaan', 'Paid by employer'), U.rp(b.totalEmployer))
      + U.kpi(T('Total iuran per bulan', 'Total contributions per month'), U.rp(b.totalEmployee + b.totalEmployer)) + '</div>';
    var R = function (n, x, re, rk) { return U.row([n, U.rp(x.base), re, U.rp(x.employer), rk, U.rp(x.employee)]); };
    h += U.table([T('Program', 'Program'), T('Dasar upah', 'Wage base'), T('Tarif perusahaan', 'Employer rate'), T('Perusahaan', 'Employer'), T('Tarif karyawan', 'Employee rate'), T('Karyawan', 'Employee')], [
      R(T('BPJS Kesehatan', 'BPJS Health'), b.kes, '4%', '1%'), R('JHT', b.jht, T('3,7%', '3.7%'), '2%'), R('JP', b.jp, '2%', '1%'), R('JKK', b.jkk, U.pct(b.jkk.rate), '–'), R('JKM', b.jkm, T('0,3%', '0.3%'), '–'),
      U.row(['Total', '', '', U.rp(b.totalEmployer), '', U.rp(b.totalEmployee)], 'tot')]);
    var caps = [];
    if (U.val('gaji') > FIN.RULES.kesCap) caps.push(T('BPJS Kesehatan dihitung dari batas upah ', 'BPJS Health is calculated on the wage cap of ') + U.rp(FIN.RULES.kesCap));
    if (U.val('gaji') > FIN.RULES.jpCap) caps.push(T('JP dihitung dari batas upah ', 'JP is calculated on the wage cap of ') + U.rp(FIN.RULES.jpCap));
    if (caps.length) h += '<div class="note info">' + caps.join('; ') + '.</div>';
    h += '<div class="note info">' + T('Setahun: potongan karyawan ', 'Per year: employee deductions ') + U.rp(b.totalEmployee * 12) + T(', iuran perusahaan ', ', employer contributions ') + U.rp(b.totalEmployer * 12) + '.</div>';
    U.$('res').innerHTML = h;
  });
})();
