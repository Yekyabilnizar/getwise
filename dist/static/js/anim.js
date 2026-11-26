/* anim.js – animasi kecil: muncul saat digulir, angka berjalan, header, hasil kalkulator */
(function () {
  'use strict';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var top = document.querySelector('.top');
  var onScroll = function () { if (top) top.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, {passive: true}); onScroll();
  if (reduce || !('IntersectionObserver' in window)) { document.documentElement.classList.remove('js'); return; }

  // muncul saat digulir, berurutan di dalam grid
  var sel = '.cat-h,.grid>.card,.band,.chart,.prose>h2,.calc-grid>aside>.card,.calc-grid>aside>a,.guide-cta,.stats .wrap>div,.intoc';
  var els = Array.prototype.slice.call(document.querySelectorAll(sel));
  els.forEach(function (el) {
    el.classList.add('rv');
    var p = el.parentElement, i = Array.prototype.indexOf.call(p.children, el);
    if (p.classList.contains('grid') || p.classList.contains('wrap') || p.tagName === 'ASIDE') el.style.transitionDelay = Math.min(i % 4, 3) * 90 + 'ms';
  });
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); if (e.target.querySelector('[data-n]')) count(e.target); } });
  }, {rootMargin: '0px 0px -8% 0px', threshold: 0.08});
  els.forEach(function (el) { io.observe(el); });

  // angka berjalan
  function count(root) {
    root.querySelectorAll('[data-n]').forEach(function (b) {
      var n = +b.getAttribute('data-n'), t0 = null, d = 1100, from = n > 1000 ? n - 30 : 0;
      var step = function (t) { if (!t0) t0 = t; var k = Math.min(1, (t - t0) / d), e = 1 - Math.pow(1 - k, 3);
        b.firstChild.nodeValue = Math.round(from + (n - from) * e); if (k < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    });
  }

  // hasil kalkulator: animasi saat diperbarui
  var res = document.getElementById('res');
  if (res && 'MutationObserver' in window) {
    new MutationObserver(function () {
      var k = res.querySelector('.kpis'); if (!k) return;
      k.classList.remove('pop'); void k.offsetWidth; k.classList.add('pop');
    }).observe(res, {childList: true});
  }
})();
