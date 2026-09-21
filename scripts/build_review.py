"""Build review/index.html: every letter in lotties/manifest.json, playing live with lottie-web, tap to react,
letter name spoken on tap when an audio clip exists. Static, works from GitHub Pages or file://."""
import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
m = json.load(open(f'{ROOT}/lotties/manifest.json'))
cards = []
for L in m['letters']:
    seg = json.dumps(L['segments']) if L['segments'] else 'null'
    w, h = m['_meta']['canvas'][L['canvas']]
    cards.append(f'''<div class="card" data-file="../lotties/{L['file']}" data-seg='{seg}' data-audio="../{L['audio_name']}">
  <div class="head"><span class="urdu">{L['ch']}</span><span class="meta">{html.escape(L['name'])} · {html.escape(L['word'])}</span></div>
  <div class="stage" style="--ar:{w}/{h}" role="button" tabindex="0" aria-label="Tap {html.escape(L['name'])}"></div>
  <p class="note"><b>{html.escape(L['character'])}</b> · {html.escape(L['status'])}</p></div>''')
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Urdu Letter Friends · review</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&family=Noto+Nastaliq+Urdu:wght@600&display=swap">
<style>
body{{margin:0;background:#fbf7ee;color:#2b2a33;font-family:Fredoka,system-ui,sans-serif;padding:24px 16px 40px}}
.wrap{{max-width:1100px;margin:0 auto}} h1{{font-size:1.6rem;margin:0 0 4px}} p.sub{{color:#7a7684;margin:0 0 24px;max-width:65ch}}
.grid{{display:flex;flex-wrap:wrap;gap:20px}} .card{{flex:1 1 300px;background:#fff;border:1px solid #e6dfd0;border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:12px}}
.stage{{background:#fff;border-radius:10px;width:100%;aspect-ratio:var(--ar);cursor:pointer;overflow:hidden}} .stage svg{{display:block}}
.head{{display:flex;justify-content:space-between;align-items:baseline;gap:12px}} .urdu{{font-family:"Noto Nastaliq Urdu",serif;font-size:2rem;color:#e8557a;line-height:1}}
.meta,.note{{color:#7a7684;font-size:.9rem;margin:0}}
</style></head><body><div class="wrap">
<h1>Urdu Letter Friends · review</h1>
<p class="sub">Tap any character. Ones with <code>idle</code>/<code>tap</code> markers play their reaction and say the letter name; reference files without markers just loop. Built from <code>lotties/manifest.json</code> by <code>scripts/build_review.py</code>.</p>
<div class="grid">{''.join(cards)}</div></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
<script>
document.querySelectorAll('.card').forEach(async card=>{{
  const seg=JSON.parse(card.dataset.seg), stage=card.querySelector('.stage');
  const data=await (await fetch(card.dataset.file)).json();
  const a=lottie.loadAnimation({{container:stage,renderer:'svg',loop:true,autoplay:!seg,animationData:data}});
  const snd=new Audio(card.dataset.audio); let busy=false;
  if(seg) a.addEventListener('DOMLoaded',()=>a.playSegments(seg.idle,true));
  const tap=()=>{{ snd.currentTime=0; snd.play().catch(()=>{{}}); if(!seg||busy) return; busy=true; a.loop=false; a.playSegments(seg.tap,true);
    a.addEventListener('complete',function once(){{a.removeEventListener('complete',once);a.loop=true;a.playSegments(seg.idle,true);busy=false}}); }};
  stage.onclick=tap; stage.onkeydown=e=>{{if(e.key==='Enter'||e.key===' '){{e.preventDefault();tap()}}}};
}});
</script></body></html>'''
open(f'{ROOT}/review/index.html','w').write(page); print('review/index.html', len(page))
