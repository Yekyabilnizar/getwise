(function () {
  var U = UI, T = U.tr;
  U.init(function () {
    var m = U.val('masaKerja'), r = FIN.thr({gaji: U.val('gaji'), masaKerja: m, status: U.val('status'), tidakTetap: U.val('tidakTetap'), bpjs: U.bpjsOpts()});
    if (m < 1) { U.$('res').innerHTML = '<div class="note">' + T('Masa kerja kurang dari 1 bulan belum berhak atas THR menurut Permenaker 6/2016.', 'Employees with less than 1 month of service are not yet entitled to THR under Regulation 6/2016.') + '</div>'; return; }
    var h = '<div class="kpis">' + U.kpi(T('THR kotor', 'Gross THR'), U.rp(r.thr), 'main') + U.kpi(T('THR bersih (perkiraan)', 'Net THR (estimate)'), U.rp(r.thrBersih))
      + U.kpi(T('Tambahan PPh 21 bulan THR', 'Extra PPh 21 in THR month'), U.rp(r.tambahanPajak), 'warn') + U.kpi(T('Dasar', 'Basis'), m >= 12 ? T('1 bulan upah', '1 month of wages') : ((U.EN ? String(m) : String(m).replace('.', ',')) + T('/12 × upah', '/12 × wages'))) + '</div>';
    h += '<h3>' + T('Pajak di bulan THR dibayarkan', 'Tax in the month THR is paid') + '</h3>' + U.table(['', T('Bulan biasa', 'Normal month'), T('Bulan THR', 'THR month')], [
      U.row([T('Penghasilan bruto', 'Gross income'), U.rp(r.brutoBiasa), U.rp(r.brutoThr)]), U.row([T('Tarif TER kategori ', 'TER rate, category ') + r.kategori, U.pct(r.rateBiasa), U.pct(r.rateThr)]),
      U.row(['PPh 21', U.rp(r.pajakBiasa), U.rp(r.pajakThrBulan)], 'tot')]);
    h += '<div class="note info">' + T('Tambahan potongan ini akan diperhitungkan ulang di bulan Desember dengan tarif Pasal 17, jadi total pajak setahun tidak bertambah hanya karena THR dipotong dengan TER.', 'This extra withholding is reconciled in December using the Article 17 rates, so total annual tax does not increase just because THR is withheld with TER.') + '</div>';
    U.$('res').innerHTML = h;
  });
})();
