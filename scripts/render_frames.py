"""Render N evenly spaced frames of lotties/<name>.json with lottie-web in headless Chrome into review/frames/<name>.png.
Usage: python3 scripts/render_frames.py tay-titli 12   (same renderer the app will use, so what you see is what ships)"""
import json, asyncio, sys, io, os, shutil
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))

async def render(name, n=8):
    data = open(f'{HERE}/../lotties/{name}.json').read(); d = json.loads(data)
    w, h, ip, op = d['w'], d['h'], d['ip'], d['op']
    html = f"""<html><body style="margin:0;background:#fff"><div id=a style="width:{w}px;height:{h}px"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
    <script>window.anim=lottie.loadAnimation({{container:document.getElementById('a'),renderer:'svg',loop:false,autoplay:false,animationData:{data}}});</script></body></html>"""
    async with async_playwright() as p:
        exe = shutil.which('google-chrome') or shutil.which('chromium')
        b = await (p.chromium.launch(executable_path=exe) if exe else p.chromium.launch())
        pg = await b.new_page(viewport={'width': w, 'height': h}); await pg.set_content(html)
        await pg.wait_for_function('window.anim && window.anim.isLoaded')
        frames = []
        for i in range(n):
            f = ip + (op - ip) * i / n
            await pg.evaluate(f'window.anim.goToAndStop({f}, true)'); await pg.wait_for_timeout(50)
            frames.append((round(f), Image.open(io.BytesIO(await pg.screenshot()))))
        await b.close()
    scale = 260 / h; tw, th = int(w * scale), 260
    out = Image.new('RGB', (tw * n + 8 * (n + 1), th + 40), '#222'); dr = ImageDraw.Draw(out)
    for i, (f, im) in enumerate(frames):
        x = 8 + i * (tw + 8); out.paste(im.resize((tw, th)), (x, 30)); dr.text((x, 8), f'f{f}', fill='white')
    dr.text((out.width - 220, 8), f'{name} {w}x{h} {op - ip}f@{d["fr"]}fps', fill='#aaa')
    os.makedirs(f'{HERE}/../review/frames', exist_ok=True); out.save(f'{HERE}/../review/frames/{name}.png'); print(name, 'ok')

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 8))
