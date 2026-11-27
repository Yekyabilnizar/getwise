(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var r = FIN.bungaMajemuk({awal: U.val('awal'), bulanan: U.val('bulanan'), imbal: U.val('imbal'), tahun: U.val('tahun'), kenaikan: U.val('kenaikan')});
    if (!r.rows.length) { U.$('res').innerHTML = '<div class="note">' + T('Isi jangka waktu minimal 1 tahun.', 'Enter a time horizon of at least 1 year.') + '</div>'; return; }
    var h = '<div class="kpis">' + U.kpi(T('Nilai akhir', 'Final value'), U.rp(r.saldoAkhir), 'main') + U.kpi(T('Total setoran', 'Total contributions'), U.rp(r.totalSetor))
      + U.kpi(T('Hasil investasi', 'Investment returns'), U.rp(r.hasil)) + U.kpi(T('Porsi hasil', 'Share from returns'), U.pct(r.saldoAkhir ? r.hasil / r.saldoAkhir : 0, 0)) + '</div>';
    var max = r.rows[r.rows.length - 1].saldo || 1;
    h += '<div class="bars" aria-hidden="true">' + r.rows.map(function (y) {
      return '<div class="bar" title="' + T('Tahun ', 'Year ') + y.tahun + ': ' + U.rp(y.saldo) + '"><i style="height:' + (y.saldo / max * 100).toFixed(1) + '%"><s style="height:' + (y.saldo ? y.setoran / y.saldo * 100 : 0).toFixed(1) + '%"></s></i><small>' + y.tahun + '</small></div>';
    }).join('') + '</div><p class="legend"><span class="k1"></span> ' + T('Setoran', 'Contributions') + ' <span class="k2"></span> ' + T('Hasil investasi', 'Investment returns') + '</p>';
    h += U.table([T('Tahun', 'Year'), T('Total setoran', 'Total contributions'), T('Hasil', 'Returns'), T('Nilai', 'Value')], r.rows.map(function (y) { return U.row([y.tahun, U.rp(y.setoran), U.rp(y.hasil), U.rp(y.saldo)]); }));
    U.$('res').innerHTML = h;
  });
})();
