(function () {
  var U = UI, BLN = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des'];
  U.init(function () {
    var r = FIN.pph21({gaji: U.val('gaji'), tidakTetap: U.val('tidakTetap'), bonus: U.val('bonus'), bulanBonus: +U.val('bulanBonus'), status: U.val('status'), bpjs: U.bpjsOpts()});
    var h = '<div class="kpis">' + U.kpi('PPh 21 per bulan (Jan–Nov)', U.rp(r.pajakBulan), 'main') + U.kpi('PPh 21 Desember', U.rp(r.pajakDes), r.pajakDes < 0 ? 'warn' : '')
      + U.kpi('PPh 21 setahun', U.rp(r.pajakSetahun)) + U.kpi('Tarif TER bulan biasa', 'Kategori ' + r.kategori + ' · ' + U.pct(r.terRate)) + '</div>';
    if (r.pajakDes < 0) h += '<div class="note">Potongan Januari–November lebih besar dari pajak setahun, sehingga ada <b>kelebihan ' + U.rp(-r.pajakDes) + '</b> yang dikembalikan di Desember.</div>';
    h += '<h3>Potongan per bulan</h3>' + U.table(['Bulan', 'Bruto', 'Tarif', 'PPh 21'], r.months.map(function (m) {
      return U.row([BLN[m.m - 1], U.rp(m.bruto), m.rate === null ? 'Pasal 17' : U.pct(m.rate), U.rp(m.pajak)]);
    }).concat([U.row(['Total', U.rp(r.brutoSetahun), '', U.rp(r.pajakSetahun)], 'tot')]));
    h += '<h3>Perhitungan Desember</h3>' + U.table(['Komponen', 'Setahun'], [
      U.row(['Gaji + tunjangan', U.rp((U.val('gaji') + U.val('tidakTetap')) * 12)]),
      U.row(['Premi BPJS dibayar perusahaan (Kes, JKK, JKM)', U.rp(r.natura * 12)]),
      U.row(['Bonus / THR', U.rp(U.val('bonus'))]),
      U.row(['Penghasilan bruto', U.rp(r.brutoSetahun)], 'tot'),
      U.row(['− Biaya jabatan', U.rp(r.biayaJabatan)]), U.row(['− Iuran JHT &amp; JP karyawan', U.rp(r.iuranSetahun)]),
      U.row(['Penghasilan neto', U.rp(r.netto)], 'tot'), U.row(['− PTKP ' + U.val('status'), U.rp(r.ptkp)]),
      U.row(['PKP (dibulatkan ke ribuan)', U.rp(r.pkp)], 'tot')]);
    if (r.pasal17.length) h += U.table(['Lapisan PKP', 'Tarif', 'Pajak'], r.pasal17.map(function (x) { return U.row([U.rp(x.from) + ' – ' + U.rp(x.to), U.pct(x.rate, 0), U.rp(x.tax)]); })
      .concat([U.row(['PPh 21 setahun', '', U.rp(r.pajakSetahun)], 'tot'), U.row(['− Sudah dipotong Jan–Nov', '', U.rp(r.terTotal)]), U.row(['PPh 21 Desember', '', U.rp(r.pajakDes)], 'tot')]));
    else h += '<div class="note info">Penghasilan neto setahun di bawah PTKP, sehingga tidak ada PPh 21 terutang setahun.</div>';
    U.$('res').innerHTML = h;
  });
})();
