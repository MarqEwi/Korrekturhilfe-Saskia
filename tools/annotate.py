import sys
from PIL import Image, ImageDraw, ImageFont
W=sys.argv[1]
import importlib.util
spec=importlib.util.spec_from_file_location('errdata',sys.argv[2]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
P=m.P; SC=sys.argv[3]; OUT=sys.argv[4]; K=sys.argv[5]
RED=(215,20,25)
fc=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf',40)
fm=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf',62)
for p,d in P.items():
    im=Image.open(f'{SC}/S{p}.jpg').convert('RGB'); dr=ImageDraw.Draw(im)
    for (a,b,c,e) in d.get('mask',[]): dr.rectangle((a,b,c,e),fill=(232,228,220))
    used={}
    for (ln,x0,x1,by,corr,sign,cnt,*_) in d['items']:
        dr.line((x0,by+20,x1,by+20),fill=RED,width=6)
        tw=dr.textlength(corr,font=fc); tx=max(10,(x0+x1)/2-tw/2)
        ty=by-102+(_[2] if len(_)>2 else 0)
        dr.text((tx,ty),corr,fill=RED,font=fc,stroke_width=4,stroke_fill=(246,241,226))
        mx=d['margin']+25+used.get(ln,0)
        dr.text((mx,by-50),sign,fill=RED,font=fm)
        used[ln]=used.get(ln,0)+dr.textlength(sign,font=fm)+30
    im.resize((2250,3000),Image.LANCZOS).save(f'{OUT}/{K}_S{p}_korrigiert.jpg',quality=85)
    w,h=im.size
    for k,(a,b) in enumerate([(0,0.36),(0.32,0.68),(0.64,1.0)]):
        c=im.crop((0,int(a*h),w,int(b*h))); c=c.resize((1800,int(c.size[1]*0.6))); c.save(f'{W}/work/chk{p}_{k}.jpg',quality=82)
