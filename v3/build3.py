import base64, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT.parent / 'index.html'   # repo root → served by GitHub Pages
head=(ROOT/'src/01-head.html').read_text(encoding='utf-8')
body=(ROOT/'src/02-body.html').read_text(encoding='utf-8')
js=(ROOT/'src/03-js.html').read_text(encoding='utf-8')
def b64(p,m): return f"data:{m};base64,"+base64.b64encode((ROOT/p).read_bytes()).decode('ascii')
tokens={
 'F_DISP_300':b64('fonts/display-normal-300.woff2','font/woff2'),
 'F_DISP_500':b64('fonts/display-normal-500.woff2','font/woff2'),
 'F_SERIF':b64('fonts/serif-normal-400.woff2','font/woff2'),
 'F_SERIF_I':b64('fonts/serif-italic-400.woff2','font/woff2'),
 'F_SANS_300':b64('fonts/sans-normal-300.woff2','font/woff2'),
 'F_SANS_400':b64('fonts/sans-normal-400.woff2','font/woff2'),
 'F_SANS_500':b64('fonts/sans-normal-500.woff2','font/woff2'),
 'IMG_HERO':b64('opt/hero.webp','image/webp'),
 'IMG_P1':b64('opt/p1.webp','image/webp'),'IMG_P2':b64('opt/p2.webp','image/webp'),
 'IMG_P3':b64('opt/p3.webp','image/webp'),'IMG_P4':b64('opt/p4.webp','image/webp'),
 'IMG_P5':b64('opt/p5.webp','image/webp'),'IMG_P6':b64('opt/p6.webp','image/webp'),
 'IMG_WORKSHOP':b64('opt/workshop.webp','image/webp'),
 'IMG_DETAIL':b64('opt/detail.webp','image/webp'),
}
html=head+body+js
for k,v in tokens.items(): html=html.replace('{{'+k+'}}',v)
left=re.findall(r'\{\{[A-Z0-9_]+\}\}',html)
if left: print('UNRESOLVED',set(left)); sys.exit(1)
out=OUT; out.write_text(html,encoding='utf-8')
print(f'{out.name} — {out.stat().st_size/1024:.0f} KB · fonts {html.count("@font-face")}')
