(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var r = FIN.kreditFlat({harga: U.val('harga'), dpPersen: U.val('dpPersen'), tenorBulan: U.val('tenorBulan'), bungaFlat: U.val('bungaFlat')});
    if (!r.n || r.pinjaman <= 0) { U.$('res').innerHTML = '<div class="note">' + T('Isi harga, DP di bawah 100%, dan tenor lebih dari 0.', 'Enter a price, a down payment below 100%, and a term above 0.') + '</div>'; return; }
    var fl = U.pct(U.val('bungaFlat') / 100);
    var h = '<div class="kpis">' + U.kpi(T('Cicilan per bulan', 'Monthly installment'), U.rp(r.cicilan), 'main') + U.kpi(T('Bunga efektif per tahun', 'Effective rate per year'), U.pct(r.efektif), 'warn')
      + U.kpi(T('Total bunga', 'Total interest'), U.rp(r.totalBunga)) + U.kpi(T('Total bayar (+ DP)', 'Total paid (+ down payment)'), U.rp(r.totalBayar + r.dp)) + '</div>';
    h += U.table([T('Rincian', 'Breakdown'), ''], [U.row([T('Harga kendaraan', 'Vehicle price'), U.rp(r.harga)]), U.row([T('Uang muka', 'Down payment'), U.rp(r.dp)]), U.row([T('Pokok pinjaman', 'Loan principal'), U.rp(r.pinjaman)], 'tot'),
      U.row([T('Bunga flat ', 'Flat interest ') + fl + ' × ' + r.n + T(' bulan', ' months'), U.rp(r.totalBunga)]),
      U.row([T('Cicilan = (pokok + bunga) ÷ ', 'Installment = (principal + interest) ÷ ') + r.n, U.rp(r.cicilan)], 'tot')]);
    h += '<div class="note info">' + T('Bila pinjaman yang sama memakai bunga efektif ', 'If the same loan used an effective rate of ') + fl + T(' (seperti KPR), cicilannya hanya ', ' (like a mortgage), the installment would be only ') + U.rp(r.cicilanAnuitasSetara)
      + T('. Bunga flat ', '. A flat rate of ') + fl + T(' setara bunga efektif <b>', ' equals an effective rate of <b>') + U.pct(r.efektif) + T('</b> per tahun.', '</b> per year.') + '</div>';
    U.$('res').innerHTML = h;
  });
})();
