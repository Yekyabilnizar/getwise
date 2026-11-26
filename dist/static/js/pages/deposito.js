(function () {
  var U = UI;
  U.init(function () {
    var aro = U.val('aro'), r = FIN.deposito({nominal: U.val('nominal'), bunga: U.val('bunga'), tenorBulan: +U.val('tenorBulan'), perpanjang: U.val('perpanjang'), aro: aro});
    var h = '<div class="kpis">' + U.kpi('Bunga bersih periode pertama', U.rp(r.bungaBersih), 'main') + U.kpi('Pajak 20%', U.rp(r.pajak))
      + U.kpi('Saldo akhir', U.rp(r.saldoAkhir)) + U.kpi('Imbal bersih per tahun', U.pct(r.imbalBersihTahunan)) + '</div>';
    if (!r.kenaPajak) h += '<div class="note info">Nominal tidak lebih dari Rp7.500.000, sehingga bunga tidak dipotong pajak (dengan asumsi tidak ada simpanan lain di bank yang sama).</div>';
    h += U.table(['Periode', 'Bunga kotor', 'Pajak', 'Bunga bersih', aro ? 'Saldo deposito' : 'Pokok'], r.rows.map(function (x) {
      return U.row([x.periode, U.rp(x.bungaKotor), U.rp(x.pajak), U.rp(x.bungaBersih), U.rp(x.saldo)]); })
      .concat([U.row(['Total bunga bersih', '', '', U.rp(r.totalBersih), U.rp(r.saldoAkhir)], 'tot')]));
    U.$('res').innerHTML = h;
  });
})();
