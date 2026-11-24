import sys,subprocess
from playwright.sync_api import sync_playwright
# Uso: python3 render.py /percorso/assoluto/effetto.html out.mp4 <secondi> [larghezza] [altezza] [fps]
html,out,dur=sys.argv[1],sys.argv[2],float(sys.argv[3])
w=int(sys.argv[4]) if len(sys.argv)>4 else 1080
h=int(sys.argv[5]) if len(sys.argv)>5 else 1920
fps=int(sys.argv[6]) if len(sys.argv)>6 else 30
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':w,'height':h})
    pg.goto('file://'+html+'?render'); pg.wait_for_function('typeof window.seek==="function"')
    pg.evaluate('document.fonts.ready')
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(fps),'-i','-','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-vf','scale=out_color_matrix=bt709:out_range=tv,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','18','-color_range','tv','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','aac','-shortest','-movflags','+faststart',out],stdin=subprocess.PIPE)
    for i in range(int(dur*fps)):
        pg.evaluate(f'window.seek({i/fps})'); ff.stdin.write(pg.screenshot(type='png'))
    ff.stdin.close(); ff.wait(); b.close()
