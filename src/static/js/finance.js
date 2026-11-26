/* finance.js – mesin hitung HitungDuit (dipakai di peramban dan di uji Node). Semua angka rupiah. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.FIN = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ---------------- konstanta aturan (perbarui di sini bila aturan berubah) ---------------- */
  var RULES = {
    updated: '27 November 2026',
    // PTKP setahun (UU HPP / PMK 101/2016, berlaku 2026)
    ptkpBase: 54000000, ptkpKawin: 4500000, ptkpTanggungan: 4500000,
    // Tarif Pasal 17 UU HPP
    pasal17: [[60000000, 0.05], [250000000, 0.15], [500000000, 0.25], [5000000000, 0.30], [Infinity, 0.35]],
    biayaJabatanRate: 0.05, biayaJabatanMaxTahun: 6000000,
    // BPJS
    kesRateEmployer: 0.04, kesRateEmployee: 0.01, kesCap: 12000000,
    jhtEmployer: 0.037, jhtEmployee: 0.02,
    jpEmployer: 0.02, jpEmployee: 0.01, jpCap: 11086300, jpCapNote: 'berlaku mulai Maret 2026 (sebelumnya Rp10.547.400)',
    jkm: 0.003,
    jkk: {sangat_rendah: 0.0024, rendah: 0.0054, sedang: 0.0089, tinggi: 0.0127, sangat_tinggi: 0.0174},
    // pajak bunga deposito (PPh final)
    depoTax: 0.20, depoTaxThreshold: 7500000
  };

  /* TER bulanan PP 58/2023: [batas atas (inklusif), tarif] */
  var TER = {
    A: [[5400000, 0], [5650000, .0025], [5950000, .005], [6300000, .0075], [6750000, .01], [7500000, .0125], [8550000, .015], [9650000, .0175],
        [10050000, .02], [10350000, .0225], [10700000, .025], [11050000, .03], [11600000, .035], [12500000, .04], [13750000, .05], [15100000, .06],
        [16950000, .07], [19750000, .08], [24150000, .09], [26450000, .10], [28000000, .11], [30050000, .12], [32400000, .13], [35400000, .14],
        [39100000, .15], [43850000, .16], [47800000, .17], [51400000, .18], [56300000, .19], [62200000, .20], [68600000, .21], [77500000, .22],
        [89000000, .23], [103000000, .24], [125000000, .25], [157000000, .26], [206000000, .27], [337000000, .28], [454000000, .29],
        [550000000, .30], [695000000, .31], [910000000, .32], [1400000000, .33], [Infinity, .34]],
    B: [[6200000, 0], [6500000, .0025], [6850000, .005], [7300000, .0075], [9200000, .01], [10750000, .015], [11250000, .02], [11600000, .025],
        [12600000, .03], [13600000, .04], [14950000, .05], [16400000, .06], [18450000, .07], [21850000, .08], [26000000, .09], [27700000, .10],
        [29350000, .11], [31450000, .12], [33950000, .13], [37100000, .14], [41100000, .15], [45800000, .16], [49500000, .17], [53800000, .18],
        [58500000, .19], [64000000, .20], [71000000, .21], [80000000, .22], [93000000, .23], [109000000, .24], [129000000, .25], [163000000, .26],
        [211000000, .27], [374000000, .28], [459000000, .29], [555000000, .30], [704000000, .31], [957000000, .32], [1405000000, .33], [Infinity, .34]],
    C: [[6600000, 0], [6950000, .0025], [7350000, .005], [7800000, .0075], [8850000, .01], [9800000, .0125], [10950000, .015], [11200000, .0175],
        [12050000, .02], [12950000, .03], [14150000, .04], [15550000, .05], [17050000, .06], [19500000, .07], [22700000, .08], [26600000, .09],
        [28100000, .10], [30100000, .11], [32600000, .12], [35400000, .13], [38900000, .14], [43000000, .15], [47400000, .16], [51200000, .17],
        [55800000, .18], [60400000, .19], [66700000, .20], [74500000, .21], [83200000, .22], [95600000, .23], [110000000, .24], [134000000, .25],
        [169000000, .26], [221000000, .27], [390000000, .28], [463000000, .29], [561000000, .30], [709000000, .31], [965000000, .32],
        [1419000000, .33], [Infinity, .34]]
  };

  var STATUS = ['TK/0', 'TK/1', 'TK/2', 'TK/3', 'K/0', 'K/1', 'K/2', 'K/3'];

  function terCategory(status) {
    if (status === 'TK/0' || status === 'TK/1' || status === 'K/0') return 'A';
    if (status === 'K/3') return 'C';
    return 'B';
  }
  function terRate(status, bruto) {
    var t = TER[terCategory(status)];
    for (var i = 0; i < t.length; i++) if (bruto <= t[i][0]) return t[i][1];
    return t[t.length - 1][1];
  }
  function ptkp(status) {
    var kawin = status.charAt(0) === 'K', n = +status.split('/')[1] || 0;
    return RULES.ptkpBase + (kawin ? RULES.ptkpKawin : 0) + Math.min(n, 3) * RULES.ptkpTanggungan;
  }
  function pasal17(pkp) {
    var tax = 0, prev = 0, rows = [];
    for (var i = 0; i < RULES.pasal17.length && pkp > prev; i++) {
      var top = RULES.pasal17[i][0], r = RULES.pasal17[i][1], part = Math.min(pkp, top) - prev;
      tax += part * r; rows.push({from: prev, to: Math.min(pkp, top), rate: r, tax: part * r}); prev = top;
    }
    return {tax: tax, rows: rows};
  }
  var floor1000 = function (x) { return Math.floor(x / 1000) * 1000; };

  /* ---------------- BPJS ---------------- */
  function bpjs(upah, o) {
    o = o || {};
    var kesBase = Math.min(upah, RULES.kesCap), jpBase = Math.min(upah, RULES.jpCap), jkkRate = RULES.jkk[o.jkk || 'sangat_rendah'];
    var on = function (k) { return o[k] !== false; };
    var r = {
      kes: {employer: on('kes') ? kesBase * RULES.kesRateEmployer : 0, employee: on('kes') ? kesBase * RULES.kesRateEmployee : 0, base: kesBase},
      jht: {employer: on('jht') ? upah * RULES.jhtEmployer : 0, employee: on('jht') ? upah * RULES.jhtEmployee : 0, base: upah},
      jp: {employer: on('jp') ? jpBase * RULES.jpEmployer : 0, employee: on('jp') ? jpBase * RULES.jpEmployee : 0, base: jpBase},
      jkk: {employer: on('jkk') ? upah * jkkRate : 0, employee: 0, base: upah, rate: jkkRate},
      jkm: {employer: on('jkm') ? upah * RULES.jkm : 0, employee: 0, base: upah}
    };
    r.totalEmployer = r.kes.employer + r.jht.employer + r.jp.employer + r.jkk.employer + r.jkm.employer;
    r.totalEmployee = r.kes.employee + r.jht.employee + r.jp.employee;
    return r;
  }

  /* ---------------- PPh 21 karyawan tetap ---------------- */
  // o: {gaji, tidakTetap (per bulan, tetap tiap bulan), bonus (sekali, dibayar di bulanBonus), status, bpjs opsi, bulanBonus 1..12}
  function pph21(o) {
    var gaji = +o.gaji || 0, tt = +o.tidakTetap || 0, bonus = +o.bonus || 0, status = o.status || 'TK/0';
    var b = bpjs(gaji, o.bpjs || {});
    var natura = b.kes.employer + b.jkk.employer + b.jkm.employer;        // premi yang dibayar pemberi kerja: menambah bruto
    var brutoBulan = gaji + tt + natura;
    var iuranPegawai = b.jht.employee + b.jp.employee;                    // pengurang penghasilan (bukan BPJS Kesehatan)
    var bulanBonus = Math.min(12, Math.max(1, +o.bulanBonus || 12));
    var months = [], terTotal = 0;
    for (var m = 1; m <= 11; m++) {
      var br = brutoBulan + (m === bulanBonus ? bonus : 0), rate = terRate(status, br), pajak = Math.floor(br * rate);
      months.push({m: m, bruto: br, rate: rate, pajak: pajak}); terTotal += pajak;
    }
    var brutoDes = brutoBulan + (bulanBonus === 12 ? bonus : 0);
    var brutoSetahun = brutoBulan * 12 + bonus;
    var bj = Math.min(brutoSetahun * RULES.biayaJabatanRate, RULES.biayaJabatanMaxTahun);
    var iuranSetahun = iuranPegawai * 12;
    var netto = brutoSetahun - bj - iuranSetahun;
    var pt = ptkp(status), pkp = Math.max(0, floor1000(netto - pt));
    var p17 = pasal17(pkp), pajakSetahun = Math.floor(p17.tax);
    var pajakDes = pajakSetahun - terTotal;
    months.push({m: 12, bruto: brutoDes, rate: null, pajak: pajakDes});
    return {bpjs: b, natura: natura, brutoBulan: brutoBulan, kategori: terCategory(status), terRate: terRate(status, brutoBulan),
            pajakBulan: Math.floor(brutoBulan * terRate(status, brutoBulan)), months: months, terTotal: terTotal,
            brutoSetahun: brutoSetahun, biayaJabatan: bj, iuranSetahun: iuranSetahun, netto: netto, ptkp: pt, pkp: pkp,
            pasal17: p17.rows, pajakSetahun: pajakSetahun, pajakDes: pajakDes, iuranPegawai: iuranPegawai};
  }

  /* ---------------- gaji bersih (take home pay) ---------------- */
  function gajiBersih(o) {
    var p = pph21(o), gaji = +o.gaji || 0, tt = +o.tidakTetap || 0;
    var potongan = p.bpjs.totalEmployee + p.pajakBulan;
    return {pph: p, gajiKotor: gaji + tt, potonganBpjs: p.bpjs.totalEmployee, pajak: p.pajakBulan, thp: gaji + tt - potongan,
            biayaPerusahaan: gaji + tt + p.bpjs.totalEmployer, rataPajakSetahun: p.pajakSetahun / 12, thpRata: gaji + tt - p.bpjs.totalEmployee - p.pajakSetahun / 12};
  }

  /* ---------------- THR ---------------- */
  function thr(o) {
    var gaji = +o.gaji || 0, masa = +o.masaKerja || 0, status = o.status || 'TK/0';
    var besar = masa >= 12 ? gaji : (masa >= 1 ? Math.round(gaji * masa / 12) : 0);
    var b = bpjs(gaji, o.bpjs || {}), natura = b.kes.employer + b.jkk.employer + b.jkm.employer;
    var brutoBiasa = gaji + (+o.tidakTetap || 0) + natura;
    var pajakBiasa = Math.floor(brutoBiasa * terRate(status, brutoBiasa));
    var brutoThr = brutoBiasa + besar, rateThr = terRate(status, brutoThr), pajakThrBulan = Math.floor(brutoThr * rateThr);
    var tambahan = pajakThrBulan - pajakBiasa;
    return {thr: besar, brutoBiasa: brutoBiasa, rateBiasa: terRate(status, brutoBiasa), pajakBiasa: pajakBiasa,
            brutoThr: brutoThr, rateThr: rateThr, pajakThrBulan: pajakThrBulan, tambahanPajak: tambahan, thrBersih: besar - tambahan, kategori: terCategory(status)};
  }

  /* ---------------- kredit ---------------- */
  function anuitas(P, rTahun, nBulan) {
    var r = rTahun / 12;
    if (nBulan <= 0) return 0;
    if (r === 0) return P / nBulan;
    return P * r / (1 - Math.pow(1 + r, -nBulan));
  }
  // KPR dengan bunga fixed lalu floating (anuitas dihitung ulang saat suku bunga berubah)
  function kpr(o) {
    var harga = +o.harga || 0, dp = harga * (+o.dpPersen || 0) / 100, P = harga - dp, n = Math.round((+o.tenorTahun || 0) * 12);
    var fixM = Math.min(n, Math.round((+o.fixTahun || 0) * 12)), rFix = (+o.bungaFix || 0) / 100, rFloat = (+o.bungaFloat || 0) / 100;
    var bal = P, rows = [], totalBunga = 0, cicFix = anuitas(P, rFix, n), cicFloat = null, cic = cicFix, yearAgg = {};
    for (var m = 1; m <= n; m++) {
      if (m === fixM + 1) { cicFloat = anuitas(bal, rFloat, n - fixM); cic = cicFloat; }
      var r = (m <= fixM ? rFix : rFloat) / 12, bunga = bal * r, pokok = Math.min(bal, cic - bunga);
      bal = Math.max(0, bal - pokok); totalBunga += bunga;
      var y = Math.ceil(m / 12);
      if (!yearAgg[y]) yearAgg[y] = {tahun: y, cicilan: 0, pokok: 0, bunga: 0, sisa: 0};
      yearAgg[y].cicilan += pokok + bunga; yearAgg[y].pokok += pokok; yearAgg[y].bunga += bunga; yearAgg[y].sisa = bal;
    }
    for (var k in yearAgg) rows.push(yearAgg[k]);
    return {harga: harga, dp: dp, pinjaman: P, n: n, fixM: fixM, cicilanFix: cicFix, cicilanFloat: cicFloat, totalBunga: totalBunga,
            totalBayar: P + totalBunga, penghasilanMin: Math.max(cicFix, cicFloat || 0) / 0.3, tahunan: rows};
  }
  // bunga efektif tahunan dari cicilan tetap (cari r dengan bisection)
  function bungaEfektif(P, cicilan, n) {
    if (cicilan * n <= P) return 0;
    var lo = 0, hi = 1;
    for (var i = 0; i < 200; i++) { var mid = (lo + hi) / 2; if (anuitas(P, mid * 12, n) > cicilan) hi = mid; else lo = mid; }
    return (lo + hi) / 2 * 12;
  }
  function kreditFlat(o) {
    var harga = +o.harga || 0, dp = harga * (+o.dpPersen || 0) / 100, P = harga - dp, n = Math.round(+o.tenorBulan || 0), r = (+o.bungaFlat || 0) / 100;
    var bunga = P * r * n / 12, cic = n ? (P + bunga) / n : 0;
    return {harga: harga, dp: dp, pinjaman: P, n: n, totalBunga: bunga, cicilan: cic, totalBayar: P + bunga, efektif: bungaEfektif(P, cic, n),
            cicilanAnuitasSetara: anuitas(P, r, n)};
  }

  /* ---------------- tabungan & investasi ---------------- */
  function deposito(o) {
    var P = +o.nominal || 0, r = (+o.bunga || 0) / 100, bln = +o.tenorBulan || 1, ulang = Math.max(1, +o.perpanjang || 1);
    var kena = P > RULES.depoTaxThreshold, rows = [], saldo = P, totalBersih = 0;
    for (var i = 1; i <= ulang; i++) {
      var kotor = saldo * r * bln / 12, pajak = (saldo > RULES.depoTaxThreshold) ? kotor * RULES.depoTax : 0, bersih = kotor - pajak;
      saldo += o.aro === false ? 0 : bersih; totalBersih += bersih;
      rows.push({periode: i, bungaKotor: kotor, pajak: pajak, bungaBersih: bersih, saldo: o.aro === false ? P : saldo});
    }
    var first = rows[0];
    return {nominal: P, kenaPajak: kena, bungaKotor: first.bungaKotor, pajak: first.pajak, bungaBersih: first.bungaBersih,
            totalBersih: totalBersih, saldoAkhir: o.aro === false ? P + totalBersih : saldo, rows: rows,
            imbalBersihTahunan: (r * (kena ? 1 - RULES.depoTax : 1))};
  }
  function bungaMajemuk(o) {
    var awal = +o.awal || 0, bulanan = +o.bulanan || 0, r = (+o.imbal || 0) / 100, th = Math.round(+o.tahun || 0), naik = (+o.kenaikan || 0) / 100;
    var rm = Math.pow(1 + r, 1 / 12) - 1, saldo = awal, setor = awal, rows = [], s = bulanan;
    for (var y = 1; y <= th; y++) {
      for (var m = 0; m < 12; m++) { saldo = saldo * (1 + rm) + s; setor += s; }
      rows.push({tahun: y, setoran: setor, saldo: saldo, hasil: saldo - setor});
      s = s * (1 + naik);
    }
    return {saldoAkhir: saldo, totalSetor: setor, hasil: saldo - setor, rows: rows};
  }

  /* ---------------- format ---------------- */
  function rp(x, dec) {
    if (x === null || x === undefined || isNaN(x)) return '–';
    var neg = x < 0; x = Math.abs(x);
    var s = (dec ? x.toFixed(dec) : Math.round(x).toString()).split('.');
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return (neg ? '−' : '') + 'Rp' + s.join(',');
  }
  function pct(x, dec) {
    var s = (x * 100).toFixed(dec === undefined ? 2 : dec);
    if (s.indexOf('.') >= 0) s = s.replace(/0+$/, '').replace(/\.$/, '');
    return s.replace('.', ',') + '%';
  }
  function parseNum(s) {
    if (typeof s === 'number') return s;
    s = String(s || '').replace(/[^\d,.-]/g, '');
    if (s.indexOf(',') >= 0) s = s.replace(/\./g, '').replace(',', '.'); else s = s.replace(/\./g, '');
    var v = parseFloat(s); return isNaN(v) ? 0 : v;
  }

  return {RULES: RULES, TER: TER, STATUS: STATUS, terCategory: terCategory, terRate: terRate, ptkp: ptkp, pasal17: pasal17, bpjs: bpjs,
          pph21: pph21, gajiBersih: gajiBersih, thr: thr, anuitas: anuitas, kpr: kpr, kreditFlat: kreditFlat, bungaEfektif: bungaEfektif,
          deposito: deposito, bungaMajemuk: bungaMajemuk, rp: rp, pct: pct, parseNum: parseNum};
});
