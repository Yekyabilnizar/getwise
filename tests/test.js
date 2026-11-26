const F=require('../src/static/js/finance.js'); const a=require('assert');
const eq=(x,y,m)=>{ if(Math.abs(x-y)>0.5) throw new Error(m+': '+x+' != '+y); };
// TER rates
eq(F.terRate('K/0',30160000),0.13,'ddtc'); eq(F.terRate('TK/0',5400000),0,'A0'); eq(F.terRate('TK/0',5400001),0.0025,'A1');
eq(F.terRate('K/3',10000000),0.015,'C7'); eq(F.terRate('K/1',10000000),0.015,'B6'); eq(F.terRate('TK/0',1500000000),0.34,'top');
// table monotonic
for (const k of ['A','B','C']) { const t=F.TER[k]; for(let i=1;i<t.length;i++){ if(!(t[i][0]>t[i-1][0])) throw k+' bound '+i; if(!(t[i][1]>t[i-1][1])) throw k+' rate '+i; } }
console.log('TER rows', F.TER.A.length, F.TER.B.length, F.TER.C.length);
// PTKP
eq(F.ptkp('TK/0'),54e6,'ptkp'); eq(F.ptkp('K/3'),72e6,'ptkpK3'); eq(F.ptkp('TK/3'),67.5e6,'TK3');
// pph21 no bpjs
let p=F.pph21({gaji:10e6,status:'TK/0',bpjs:{kes:false,jht:false,jp:false,jkk:false,jkm:false}});
eq(p.pajakBulan,200000,'m'); eq(p.pkp,60e6,'pkp'); eq(p.pajakSetahun,3e6,'yr'); eq(p.pajakDes,800000,'des');
// pasal17 progressive
eq(F.pasal17(300e6).tax, 60e6*.05+190e6*.15+50e6*.25,'p17');
// bpjs caps
let b=F.bpjs(20e6,{jkk:'sangat_rendah'}); eq(b.kes.employee,120000,'kes'); eq(b.jp.employee,110863,'jp'); eq(b.jht.employee,400000,'jht');
// kpr annuity check: 500jt 10% 20y => known 4.825.108
eq(F.anuitas(500e6,0.10,240),4825108.6,'anuitas');
let k=F.kpr({harga:600e6,dpPersen:20,tenorTahun:15,fixTahun:3,bungaFix:4.5,bungaFloat:11});
console.log('kpr', Math.round(k.cicilanFix), Math.round(k.cicilanFloat), Math.round(k.totalBunga), k.tahunan.length, Math.round(k.tahunan[14].sisa));
let f=F.kreditFlat({harga:30e6,dpPersen:20,tenorBulan:36,bungaFlat:6}); console.log('flat', Math.round(f.cicilan), (f.efektif*100).toFixed(2));
let d=F.deposito({nominal:100e6,bunga:4,tenorBulan:12,perpanjang:3}); console.log('depo', d.bungaKotor, d.pajak, d.bungaBersih, Math.round(d.saldoAkhir));
let bm=F.bungaMajemuk({awal:10e6,bulanan:1e6,imbal:8,tahun:10}); console.log('bm', Math.round(bm.saldoAkhir), bm.totalSetor);
let t=F.thr({gaji:8e6,masaKerja:6,status:'K/1',bpjs:{kes:false,jkk:false,jkm:false}}); console.log('thr', JSON.stringify(t));
console.log(F.rp(1234567.5), F.rp(-500), F.pct(0.0025), F.pct(0.12), F.parseNum('12.500.000'), F.parseNum('4,5'));
console.log('ALL OK');
