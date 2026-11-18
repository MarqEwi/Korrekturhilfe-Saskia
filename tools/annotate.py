import sys
from PIL import Image, ImageDraw, ImageFont
W=sys.argv[1]; sys.path.insert(0,W+'/work')
from errors import P
RED=(215,20,25)
fc=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf',40)
fm=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf',62)
for p,d in P.items():
    im=Image.open(f'{W}/scans/S{p}.jpg').convert('RGB'); dr=ImageDraw.Draw(im)
    used={}
    for (ln,x0,x1,by,corr,sign,cnt,*_) in d['items']:
        dr.line((x0,by+20,x1,by+20),fill=RED,width=6)
        tw=dr.textlength(corr,font=fc); tx=max(10,(x0+x1)/2-tw/2)
        ty=by-102
        dr.text((tx,ty),corr,fill=RED,font=fc,stroke_width=4,stroke_fill=(246,241,226))
        mx=d['margin']+25+used.get(ln,0)
        dr.text((mx,by-50),sign,fill=RED,font=fm)
        used[ln]=used.get(ln,0)+dr.textlength(sign,font=fm)+30
    im.save(f'{W}/out/S{p}_korrigiert.jpg',quality=88)
    w,h=im.size
    for k,(a,b) in enumerate([(0,0.36),(0.32,0.68),(0.64,1.0)]):
        c=im.crop((0,int(a*h),w,int(b*h))); c=c.resize((1800,int(c.size[1]*0.6))); c.save(f'{W}/work/chk{p}_{k}.jpg',quality=82)
