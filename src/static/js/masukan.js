/* masukan.js – kirim formulir masukan ke /api/masukan */
(function () {
  'use strict';
  var f = document.getElementById('fb'); if (!f) return;
  var $ = function (id) { return document.getElementById(id); }, t0 = Date.now(), msg = $('fbmsg'), btn = $('kirim');
  var q = new URLSearchParams(location.search);
  if (q.get('dari')) { var s = $('halaman'); s.value = q.get('dari'); }
  if (q.get('jenis')) { var r = f.querySelector('input[name=jenis][value="' + q.get('jenis') + '"]'); if (r) r.checked = true; }
  $('pesan').addEventListener('input', function () { $('cnt').textContent = this.value.length; });
  var show = function (cls, html) { msg.className = 'note ' + cls; msg.innerHTML = html; msg.scrollIntoView({behavior: 'smooth', block: 'nearest'}); };
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var pesan = $('pesan').value.trim();
    if (pesan.length < 10) { show('', 'Tulis masukan minimal 10 karakter.'); $('pesan').focus(); return; }
    var email = $('email').value.trim();
    if (email && !/^\S+@\S+\.\S+$/.test(email)) { show('', 'Format email belum benar.'); $('email').focus(); return; }
    btn.disabled = true; btn.textContent = 'Mengirim…';
    fetch('/api/masukan', {method: 'POST', headers: {'content-type': 'application/json'}, body: JSON.stringify({
      jenis: (f.querySelector('input[name=jenis]:checked') || {}).value, halaman: $('halaman').value, pesan: pesan,
      nama: $('nama').value.trim(), email: email, website: $('website').value, t: Date.now() - t0})})
      .then(function (r) { return r.json().catch(function () { return {ok: false}; }); })
      .then(function (d) {
        if (d.ok) {
          f.querySelectorAll('.fld,.fields,.small,.btns,.tool-h').forEach(function (el) { el.style.display = 'none'; });
          show('info done', '<b>🎉 Terima kasih!</b><br>Masukan Anda sudah kami terima dan akan dibaca langsung oleh pengelola.<br><a href="/">Kembali ke beranda</a> · <a href="/masukan/">Kirim masukan lain</a>');
        } else { show('', d.error || 'Masukan belum terkirim. Silakan coba lagi.'); btn.disabled = false; btn.textContent = 'Kirim masukan'; }
      })
      .catch(function () { show('', 'Koneksi bermasalah. Periksa internet Anda lalu coba lagi.'); btn.disabled = false; btn.textContent = 'Kirim masukan'; });
  });
})();
