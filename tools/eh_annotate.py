import sys, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps
W=sys.argv[1]
U='/root/.claude/uploads/55f28959-2730-5b78-b24e-eadc36c6f310/'
RED=(205,20,25)
FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; FR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fp=ImageFont.truetype(FB,64); ft=ImageFont.truetype(FR,36); fh=ImageFont.truetype(FB,38); fbig=ImageFont.truetype(FB,72)
PW=1650
import importlib.util
spec=importlib.util.spec_from_file_location('ehdata',sys.argv[2]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
P=m.P; K=sys.argv[3]; OUT=sys.argv[4]
for p,(f,items) in P.items():
    src=ImageOps.exif_transpose(Image.open(U+f+'-image.jpg')).convert('RGB')
    w,h=src.size
    im=Image.new('RGB',(w+PW,h),(255,255,255)); im.paste(src,(0,0)); d=ImageDraw.Draw(im)
    d.text((w+40,40),f"{K} – Begründung der Punkte (Seite {p} von 4)",fill=(40,40,40),font=fh)
    bottom=110
    for (x,y,pts,head,why) in items:
        big = pts.startswith("→") or pts=="52"
        fnt=fbig if big else fp
        if big: d.text((x,y-45),pts,fill=RED,font=fnt,stroke_width=5,stroke_fill=(245,243,238))
        else:
            tw=d.textlength(pts,font=fnt); d.text((x-tw/2,y-38),pts,fill=RED,font=fnt,stroke_width=5,stroke_fill=(245,243,238))
        if not head: continue
        ty=max(y-30,bottom+22)
        d.line((x+70 if not big else x+380,y,w+25,ty+22),fill=RED,width=3)
        d.text((w+40,ty),head,fill=RED,font=fh); ty+=50
        for line in textwrap.wrap(why,width=74):
            d.text((w+40,ty),line,fill=(30,30,30),font=ft); ty+=45
        bottom=ty
    im=im.resize((int((w+PW)*0.6),int(h*0.6)),Image.LANCZOS)
    im.save(f'{OUT}/{K}_Erwartungshorizont_S{p}.jpg',quality=86)
    im.resize((1700,int(1700*im.size[1]/im.size[0]))).save(f'{W}/work/ehchk{p}.jpg',quality=80)
