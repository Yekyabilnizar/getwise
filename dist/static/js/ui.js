/* ui.js – utilitas antarmuka: format angka, baca isian, hitung otomatis, tautan berbagi, pencarian */
(function () {
  'use strict';
  var F = window.FIN, $ = function (id) { return document.getElementById(id); };
  var fmtThousand = function (v) {
    var s = String(v).replace(/[^\d]/g, '');
    return s ? s.replace(/^0+(?=\d)/, '').replace(/\B(?=(\d{3})+(?!\d))/g, '.') : '';
  };
  function val(id) {
    var el = $(id); if (!el) return null;
    if (el.type === 'checkbox') return el.checked;
    if (el.tagName === 'SELECT') return el.value;
    if (el.hasAttribute('data-money')) return F.parseNum(el.value);
    var v = parseFloat(String(el.value).replace(/\s/g, '').replace(',', '.'));
    return isNaN(v) ? 0 : v;
  }
  function setVal(id, v) {
    var el = $(id); if (!el) return;
    if (el.type === 'checkbox') el.checked = v === true || v === '1' || v === 'true';
    else if (el.tagName === 'SELECT') el.value = v;
    else el.value = el.hasAttribute('data-money') ? fmtThousand(v) : String(v).replace('.', ',');
  }
  window.UI = {
    val: val, $: $, rp: F.rp, pct: F.pct,
    row: function (cells, cls) { return '<tr' + (cls ? ' class="' + cls + '"' : '') + '>' + cells.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; },
    table: function (head, rows) {
      return '<div class="tscroll"><table class="tbl"><thead><tr>' + head.map(function (h) { return '<th>' + h + '</th>'; }).join('') + '</tr></thead><tbody>' + rows.join('') + '</tbody></table></div>';
    },
    bpjsOpts: function () {
      var on = function (id) { var e = $(id); return !e || e.checked; }, kk = on('jkkjkm');
      return {kes: on('kes'), jht: on('jht'), jp: on('jp'), jkk: kk ? (($('jkk') || {}).value || 'sangat_rendah') : false, jkm: kk};
    },
    kpi: function (label, value, cls) { return '<div class="kpi' + (cls ? ' ' + cls : '') + '"><small>' + label + '</small><b>' + value + '</b></div>'; },
    /* pasang kalkulator: compute() dipanggil saat isian berubah */
    init: function (compute) {
      var form = $('calc'); if (!form) return;
      var ids = Array.prototype.map.call(form.querySelectorAll('input,select'), function (e) { return e.id; }).filter(Boolean);
      // pulihkan dari URL (tautan berbagi)
      var q = new URLSearchParams(location.search);
      ids.forEach(function (id) { if (q.has(id)) setVal(id, q.get(id)); });
      form.querySelectorAll('input[data-money]').forEach(function (el) {
        el.value = fmtThousand(el.value);
        el.addEventListener('input', function () {
          var pos = el.value.length - el.selectionStart; el.value = fmtThousand(el.value);
          var p = Math.max(0, el.value.length - pos); try { el.setSelectionRange(p, p); } catch (e) {}
        });
      });
      var t, run = function () {
        try { compute(); } catch (e) { $('res').innerHTML = '<div class="note">Periksa kembali isian Anda.</div>'; }
      };
      form.addEventListener('input', function () { clearTimeout(t); t = setTimeout(run, 250); });
      form.addEventListener('change', run);
      form.addEventListener('submit', function (e) { e.preventDefault(); run(); var r = $('res'); if (r) r.scrollIntoView({behavior: 'smooth', block: 'start'}); });
      var share = $('share');
      if (share) share.addEventListener('click', function () {
        var p = new URLSearchParams();
        ids.forEach(function (id) { var v = val(id); p.set(id, typeof v === 'boolean' ? (v ? '1' : '0') : v); });
        var url = location.origin + location.pathname + '?' + p.toString();
        var done = function () { share.textContent = '✓ Tautan disalin'; setTimeout(function () { share.textContent = '🔗 Salin tautan hasil'; }, 2000); };
        if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () { prompt('Salin tautan ini:', url); });
        else prompt('Salin tautan ini:', url);
      });
      var pr = $('print'); if (pr) pr.addEventListener('click', function () { window.print(); });
      run();
    }
  };

  /* pencarian kalkulator */
  var q = $('q'), box = $('sres');
  if (q && box && window.SEARCH) {
    var norm = function (s) { return (s || '').toLowerCase(); };
    q.addEventListener('input', function () {
      var t = norm(q.value).split(/\s+/).filter(Boolean);
      if (!t.length) { box.style.display = 'none'; return; }
      var hits = window.SEARCH.filter(function (it) { var h = norm(it.t + ' ' + it.k); return t.every(function (x) { return h.indexOf(x) >= 0; }); }).slice(0, 8);
      box.innerHTML = hits.length ? hits.map(function (it) { return '<a href="' + it.u + '"><b>' + it.t + '</b><small>' + it.d + '</small></a>'; }).join('') : '<a>Belum ada kalkulator yang cocok.</a>';
      box.style.display = 'block';
    });
    document.addEventListener('click', function (e) { if (!e.target.closest('.search')) box.style.display = 'none'; });
    q.addEventListener('keydown', function (e) {
      var items = box.querySelectorAll('a[href]'); if (!items.length) return;
      var cur = box.querySelector('a.act'), i = Array.prototype.indexOf.call(items, cur);
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault(); if (cur) cur.classList.remove('act');
        i = e.key === 'ArrowDown' ? (i + 1) % items.length : (i <= 0 ? items.length - 1 : i - 1);
        items[i].classList.add('act'); items[i].scrollIntoView({block: 'nearest'});
      } else if (e.key === 'Enter') { e.preventDefault(); location.href = (cur || items[0]).href; }
      else if (e.key === 'Escape') { box.style.display = 'none'; }
    });
  }
})();
