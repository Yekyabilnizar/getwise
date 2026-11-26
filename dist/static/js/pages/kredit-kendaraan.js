(function () {
  var U = UI;
  U.init(function () {
    var r = FIN.kreditFlat({harga: U.val('harga'), dpPersen: U.val('dpPersen'), tenorBulan: U.val('tenorBulan'), bungaFlat: U.val('bungaFlat')});
    if (!r.n || r.pinjaman <= 0) { U.$('res').innerHTML = '<div class="note">Isi harga, DP di bawah 100%, dan tenor lebih dari 0.</div>'; return; }
    var h = '<div class="kpis">' + U.kpi('Cicilan per bulan', U.rp(r.cicilan), 'main') + U.kpi('Bunga efektif per tahun', U.pct(r.efektif), 'warn')
      + U.kpi('Total bunga', U.rp(r.totalBunga)) + U.kpi('Total bayar (+ DP)', U.rp(r.totalBayar + r.dp)) + '</div>';
    h += U.table(['Rincian', ''], [U.row(['Harga kendaraan', U.rp(r.harga)]), U.row(['Uang muka', U.rp(r.dp)]), U.row(['Pokok pinjaman', U.rp(r.pinjaman)], 'tot'),
      U.row(['Bunga flat ' + U.pct(U.val('bungaFlat') / 100) + ' × ' + r.n + ' bulan', U.rp(r.totalBunga)]),
      U.row(['Cicilan = (pokok + bunga) ÷ ' + r.n, U.rp(r.cicilan)], 'tot')]);
    h += '<div class="note info">Bila pinjaman yang sama memakai bunga efektif ' + U.pct(U.val('bungaFlat') / 100) + ' (seperti KPR), cicilannya hanya ' + U.rp(r.cicilanAnuitasSetara)
      + '. Bunga flat ' + U.pct(U.val('bungaFlat') / 100) + ' setara bunga efektif <b>' + U.pct(r.efektif) + '</b> per tahun.</div>';
    U.$('res').innerHTML = h;
  });
})();
