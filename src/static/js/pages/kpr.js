(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var r = FIN.kpr({harga: U.val('harga'), dpPersen: U.val('dpPersen'), tenorTahun: U.val('tenorTahun'), fixTahun: U.val('fixTahun'), bungaFix: U.val('bungaFix'), bungaFloat: U.val('bungaFloat')});
    if (!r.n || r.pinjaman <= 0) { U.$('res').innerHTML = '<div class="note">' + T('Isi harga rumah, DP di bawah 100%, dan tenor lebih dari 0.', 'Enter a house price, a down payment below 100%, and a term above 0.') + '</div>'; return; }
    var h = '<div class="kpis">' + U.kpi(T('Cicilan masa fixed', 'Installment, fixed period'), U.rp(r.cicilanFix), 'main')
      + (r.cicilanFloat !== null ? U.kpi(T('Cicilan setelah floating', 'Installment after floating'), U.rp(r.cicilanFloat), 'warn') : '')
      + U.kpi(T('Total bunga', 'Total interest'), U.rp(r.totalBunga)) + U.kpi(T('Penghasilan minimal (30%)', 'Minimum income (30%)'), U.rp(r.penghasilanMin)) + '</div>';
    h += U.table([T('Ringkasan', 'Summary'), ''], [U.row([T('Harga rumah', 'House price'), U.rp(r.harga)]), U.row([T('Uang muka', 'Down payment'), U.rp(r.dp)]), U.row([T('Pokok pinjaman', 'Loan principal'), U.rp(r.pinjaman)], 'tot'),
      U.row([T('Total bunga ', 'Total interest over ') + r.n + T(' bulan', ' months'), U.rp(r.totalBunga)]), U.row([T('Total pembayaran ke bank', 'Total paid to the bank'), U.rp(r.totalBayar)], 'tot'), U.row([T('Total keluar uang (+ DP)', 'Total cash outlay (+ down payment)'), U.rp(r.totalBayar + r.dp)])]);
    if (r.cicilanFloat !== null && r.cicilanFloat > r.cicilanFix) h += '<div class="note">' + T('Setelah ', 'After ') + r.fixM + T(' bulan, cicilan naik ', ' months, the installment rises by ') + U.rp(r.cicilanFloat - r.cicilanFix) + T(' per bulan (', ' a month (') + U.pct(r.cicilanFloat / r.cicilanFix - 1, 0) + T('). Pastikan anggaran Anda sanggup.', '). Make sure your budget can handle it.') + '</div>';
    h += '<h3>' + T('Jadwal per tahun', 'Yearly schedule') + '</h3>' + U.table([T('Tahun', 'Year'), T('Cicilan / bulan', 'Installment / month'), T('Bayar pokok', 'Principal paid'), T('Bayar bunga', 'Interest paid'), T('Sisa pokok', 'Remaining principal')], r.tahunan.map(function (y) {
      return U.row([y.tahun, U.rp(y.cicilan / 12), U.rp(y.pokok), U.rp(y.bunga), U.rp(y.sisa)]); }));
    U.$('res').innerHTML = h;
  });
})();
