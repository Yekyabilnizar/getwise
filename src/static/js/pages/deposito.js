(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var aro = U.val('aro'), r = FIN.deposito({nominal: U.val('nominal'), bunga: U.val('bunga'), tenorBulan: +U.val('tenorBulan'), perpanjang: U.val('perpanjang'), aro: aro});
    var h = '<div class="kpis">' + U.kpi(T('Bunga bersih periode pertama', 'Net interest, first period'), U.rp(r.bungaBersih), 'main') + U.kpi(T('Pajak 20%', '20% tax'), U.rp(r.pajak))
      + U.kpi(T('Saldo akhir', 'Final balance'), U.rp(r.saldoAkhir)) + U.kpi(T('Imbal bersih per tahun', 'Net return per year'), U.pct(r.imbalBersihTahunan)) + '</div>';
    if (!r.kenaPajak) h += '<div class="note info">' + T('Nominal tidak lebih dari Rp7.500.000, sehingga bunga tidak dipotong pajak (dengan asumsi tidak ada simpanan lain di bank yang sama).', 'The amount does not exceed Rp7,500,000, so interest is not taxed (assuming no other deposits at the same bank).') + '</div>';
    h += U.table([T('Periode', 'Period'), T('Bunga kotor', 'Gross interest'), T('Pajak', 'Tax'), T('Bunga bersih', 'Net interest'), aro ? T('Saldo deposito', 'Deposit balance') : T('Pokok', 'Principal')], r.rows.map(function (x) {
      return U.row([x.periode, U.rp(x.bungaKotor), U.rp(x.pajak), U.rp(x.bungaBersih), U.rp(x.saldo)]); })
      .concat([U.row([T('Total bunga bersih', 'Total net interest'), '', '', U.rp(r.totalBersih), U.rp(r.saldoAkhir)], 'tot')]));
    U.$('res').innerHTML = h;
  });
})();
