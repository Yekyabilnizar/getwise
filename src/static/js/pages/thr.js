(function () {
  var U = UI;
  U.init(function () {
    var m = U.val('masaKerja'), r = FIN.thr({gaji: U.val('gaji'), masaKerja: m, status: U.val('status'), tidakTetap: U.val('tidakTetap'), bpjs: U.bpjsOpts()});
    if (m < 1) { U.$('res').innerHTML = '<div class="note">Masa kerja kurang dari 1 bulan belum berhak atas THR menurut Permenaker 6/2016.</div>'; return; }
    var h = '<div class="kpis">' + U.kpi('THR kotor', U.rp(r.thr), 'main') + U.kpi('THR bersih (perkiraan)', U.rp(r.thrBersih))
      + U.kpi('Tambahan PPh 21 bulan THR', U.rp(r.tambahanPajak), 'warn') + U.kpi('Dasar', m >= 12 ? '1 bulan upah' : (String(m).replace('.', ',') + '/12 × upah')) + '</div>';
    h += '<h3>Pajak di bulan THR dibayarkan</h3>' + U.table(['', 'Bulan biasa', 'Bulan THR'], [
      U.row(['Penghasilan bruto', U.rp(r.brutoBiasa), U.rp(r.brutoThr)]), U.row(['Tarif TER kategori ' + r.kategori, U.pct(r.rateBiasa), U.pct(r.rateThr)]),
      U.row(['PPh 21', U.rp(r.pajakBiasa), U.rp(r.pajakThrBulan)], 'tot')]);
    h += '<div class="note info">Tambahan potongan ini akan diperhitungkan ulang di bulan Desember dengan tarif Pasal 17, jadi total pajak setahun tidak bertambah hanya karena THR dipotong dengan TER.</div>';
    U.$('res').innerHTML = h;
  });
})();
