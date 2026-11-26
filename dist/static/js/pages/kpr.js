(function () {
  var U = UI;
  U.init(function () {
    var r = FIN.kpr({harga: U.val('harga'), dpPersen: U.val('dpPersen'), tenorTahun: U.val('tenorTahun'), fixTahun: U.val('fixTahun'), bungaFix: U.val('bungaFix'), bungaFloat: U.val('bungaFloat')});
    if (!r.n || r.pinjaman <= 0) { U.$('res').innerHTML = '<div class="note">Isi harga rumah, DP di bawah 100%, dan tenor lebih dari 0.</div>'; return; }
    var h = '<div class="kpis">' + U.kpi('Cicilan masa fixed', U.rp(r.cicilanFix), 'main')
      + (r.cicilanFloat !== null ? U.kpi('Cicilan setelah floating', U.rp(r.cicilanFloat), 'warn') : '')
      + U.kpi('Total bunga', U.rp(r.totalBunga)) + U.kpi('Penghasilan minimal (30%)', U.rp(r.penghasilanMin)) + '</div>';
    h += U.table(['Ringkasan', ''], [U.row(['Harga rumah', U.rp(r.harga)]), U.row(['Uang muka', U.rp(r.dp)]), U.row(['Pokok pinjaman', U.rp(r.pinjaman)], 'tot'),
      U.row(['Total bunga ' + r.n + ' bulan', U.rp(r.totalBunga)]), U.row(['Total pembayaran ke bank', U.rp(r.totalBayar)], 'tot'), U.row(['Total keluar uang (+ DP)', U.rp(r.totalBayar + r.dp)])]);
    if (r.cicilanFloat !== null && r.cicilanFloat > r.cicilanFix) h += '<div class="note">Setelah ' + r.fixM + ' bulan, cicilan naik ' + U.rp(r.cicilanFloat - r.cicilanFix) + ' per bulan (' + U.pct(r.cicilanFloat / r.cicilanFix - 1, 0) + '). Pastikan anggaran Anda sanggup.</div>';
    h += '<h3>Jadwal per tahun</h3>' + U.table(['Tahun', 'Cicilan / bulan', 'Bayar pokok', 'Bayar bunga', 'Sisa pokok'], r.tahunan.map(function (y) {
      return U.row([y.tahun, U.rp(y.cicilan / 12), U.rp(y.pokok), U.rp(y.bunga), U.rp(y.sisa)]); }));
    U.$('res').innerHTML = h;
  });
})();
