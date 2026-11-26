"""Grafik SVG sederhana (tanpa JavaScript) untuk artikel panduan."""
from html import escape

D, E, M, G, C, MU, LN = "#0B2E26", "#0E7C66", "#9ED9C6", "#E8A90C", "#F27A5E", "#55665F", "#DCE7E2"
FONT = 'font-family="-apple-system,Segoe UI,Roboto,Arial,sans-serif"'
W, H, L, R, T, B = 680, 300, 70, 16, 20, 44


def _nice(v):
    import math
    if v <= 0:
        return 1
    e = 10 ** math.floor(math.log10(v))
    for m in (1, 2, 2.5, 5, 10):
        if v <= m * e:
            return m * e
    return 10 * e


def _axes(ymax, fmt, labels, step=1):
    top = _nice(ymax)
    s = []
    for i in range(5):
        v = top * i / 4
        y = T + (H - T - B) * (1 - i / 4)
        s.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" stroke="{LN}"/>'
                 f'<text x="{L-8}" y="{y+4:.1f}" font-size="11" fill="{MU}" text-anchor="end">{escape(fmt(v))}</text>')
    n = len(labels)
    bw = (W - L - R) / n
    for i, lab in enumerate(labels):
        if i % step == 0 or i == n - 1:
            s.append(f'<text x="{L + bw*(i+.5):.1f}" y="{H-B+18}" font-size="11" fill="{MU}" text-anchor="middle">{escape(str(lab))}</text>')
    return top, bw, "".join(s)


def _legend(series):
    x, out = L, []
    for name, color, _ in series:
        out.append(f'<rect x="{x}" y="{H-14}" width="11" height="11" rx="2" fill="{color}"/><text x="{x+16}" y="{H-4}" font-size="12" fill="{D}">{escape(name)}</text>')
        x += 26 + 7.2 * len(name)
    return "".join(out)


def _wrap(inner, title):
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(title)}" {FONT}>{inner}</svg>')


def bars(labels, series, fmt, title, stacked=False, step=1, values_on_top=None):
    ymax = max(sum(v[i] for _, _, v in series) for i in range(len(labels))) if stacked else max(max(v) for _, _, v in series)
    top, bw, s = _axes(ymax, fmt, labels, step)
    ph = H - T - B
    body = []
    prev = None
    for i in range(len(labels)):
        base = 0
        k = len(series)
        for j, (_, color, vals) in enumerate(series):
            v = vals[i]
            h = ph * v / top
            if stacked:
                x, w = L + bw * i + bw * .18, bw * .64
                y = T + ph - h - ph * base / top
                base += v
            else:
                w = bw * .7 / k
                x, y = L + bw * i + bw * .15 + w * j, T + ph - h
            body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{max(h,0):.1f}" rx="2" fill="{color}"/>')
        if values_on_top:
            tot = sum(v[i] for _, _, v in series) if stacked else max(v[i] for _, _, v in series)
            if tot == prev:
                continue
            prev = tot
            body.append(f'<text x="{L + bw*(i+.5):.1f}" y="{T + ph - ph*tot/top - 5:.1f}" font-size="10.5" font-weight="700" fill="{D}" text-anchor="middle">{escape(values_on_top(tot))}</text>')
    return _wrap(s + "".join(body) + (_legend(series) if len(series) > 1 else ""), title)


def lines(labels, series, fmt, title, step=1):
    ymax = max(max(v) for _, _, v in series)
    top, bw, s = _axes(ymax, fmt, labels, step)
    ph = H - T - B
    body = []
    for name, color, vals in series:
        pts = " ".join(f"{L + bw*(i+.5):.1f},{T + ph - ph*v/top:.1f}" for i, v in enumerate(vals))
        body.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        lx, ly = L + bw * (len(vals) - .5), T + ph - ph * vals[-1] / top
        body.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="4" fill="{color}"/>')
    return _wrap(s + "".join(body) + _legend(series), title)


def figure(svg, caption):
    return f'<figure class="chart">{svg}<figcaption>{caption}</figcaption></figure>'
