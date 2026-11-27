(function () {
  var U = UI, T = U.tr;
  var BLN = U.EN ? ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] : ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des'];
  U.init(function () {
    var r = FIN.pph21({gaji: U.val('gaji'), tidakTetap: U.val('tidakTetap'), bonus: U.val('bonus'), bulanBonus: +U.val('bulanBonus'), status: U.val('status'), bpjs: U.bpjsOpts()});
    var h = '<div class="kpis">' + U.kpi(T('PPh 21 per bulan (Jan–Nov)', 'PPh 21 per month (Jan–Nov)'), U.rp(r.pajakBulan), 'main') + U.kpi(T('PPh 21 Desember', 'PPh 21 December'), U.rp(r.pajakDes), r.pajakDes < 0 ? 'warn' : '')
      + U.kpi(T('PPh 21 setahun', 'PPh 21 per year'), U.rp(r.pajakSetahun)) + U.kpi(T('Tarif TER bulan biasa', 'TER rate, normal month'), T('Kategori ', 'Category ') + r.kategori + ' · ' + U.pct(r.terRate)) + '</div>';
    if (r.pajakDes < 0) h += '<div class="note">' + T('Potongan Januari–November lebih besar dari pajak setahun, sehingga ada <b>kelebihan ', 'January–November withholding exceeds the annual tax, so there is an <b>overpayment of ') + U.rp(-r.pajakDes) + T('</b> yang dikembalikan di Desember.', '</b> refunded in December.') + '</div>';
    h += '<h3>' + T('Potongan per bulan', 'Monthly withholding') + '</h3>' + U.table([T('Bulan', 'Month'), 'Bruto', T('Tarif', 'Rate'), 'PPh 21'].map(function (x, i) { return i === 1 ? T('Bruto', 'Gross') : x; }), r.months.map(function (m) {
      return U.row([BLN[m.m - 1], U.rp(m.bruto), m.rate === null ? T('Pasal 17', 'Article 17') : U.pct(m.rate), U.rp(m.pajak)]);
    }).concat([U.row(['Total', U.rp(r.brutoSetahun), '', U.rp(r.pajakSetahun)], 'tot')]));
    h += '<h3>' + T('Perhitungan Desember', 'December calculation') + '</h3>' + U.table([T('Komponen', 'Component'), T('Setahun', 'Annual')], [
      U.row([T('Gaji + tunjangan', 'Salary + allowances'), U.rp((U.val('gaji') + U.val('tidakTetap')) * 12)]),
      U.row([T('Premi BPJS dibayar perusahaan (Kes, JKK, JKM)', 'BPJS premiums paid by employer (Health, JKK, JKM)'), U.rp(r.natura * 12)]),
      U.row([T('Bonus / THR', 'Bonus / THR'), U.rp(U.val('bonus'))]),
      U.row([T('Penghasilan bruto', 'Gross income'), U.rp(r.brutoSetahun)], 'tot'),
      U.row([T('− Biaya jabatan', '− Job expense deduction'), U.rp(r.biayaJabatan)]), U.row([T('− Iuran JHT &amp; JP karyawan', '− Employee JHT &amp; JP'), U.rp(r.iuranSetahun)]),
      U.row([T('Penghasilan neto', 'Net income'), U.rp(r.netto)], 'tot'), U.row(['− PTKP ' + U.val('status'), U.rp(r.ptkp)]),
      U.row([T('PKP (dibulatkan ke ribuan)', 'Taxable income (rounded to thousands)'), U.rp(r.pkp)], 'tot')]);
    if (r.pasal17.length) h += U.table([T('Lapisan PKP', 'Taxable income bracket'), T('Tarif', 'Rate'), T('Pajak', 'Tax')], r.pasal17.map(function (x) { return U.row([U.rp(x.from) + ' – ' + U.rp(x.to), U.pct(x.rate, 0), U.rp(x.tax)]); })
      .concat([U.row([T('PPh 21 setahun', 'Annual PPh 21'), '', U.rp(r.pajakSetahun)], 'tot'), U.row([T('− Sudah dipotong Jan–Nov', '− Withheld Jan–Nov'), '', U.rp(r.terTotal)]), U.row([T('PPh 21 Desember', 'December PPh 21'), '', U.rp(r.pajakDes)], 'tot')]));
    else h += '<div class="note info">' + T('Penghasilan neto setahun di bawah PTKP, sehingga tidak ada PPh 21 terutang setahun.', 'Annual net income is below PTKP, so no PPh 21 is due for the year.') + '</div>';
    U.$('res').innerHTML = h;
  });
})();
