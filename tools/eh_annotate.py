import sys, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps
W=sys.argv[1]
U='/root/.claude/uploads/55f28959-2730-5b78-b24e-eadc36c6f310/'
RED=(205,20,25)
FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; FR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fp=ImageFont.truetype(FB,64); ft=ImageFont.truetype(FR,36); fh=ImageFont.truetype(FB,38); fbig=ImageFont.truetype(FB,72)
PW=1650
# (x, y, Punkte-Text, Kopf, Begründung)
P={
1:('6f3b655f',[
 (2487,955,"4","1.1.1: 4 von 7","Anzeige/Kampagne genannt (1), Veröffentlichung mit Website und Jahr (1; Jahr 2020 laut Aufgabenblatt). Implizite Botschaft „leaner and healthier“ (1 von 2). Zielgruppe „young adults and teenagers“ erst in 1.2 (1 von 2). Herausgeber und „verkauft Milch“ fehlen."),
 (2487,1610,"0","1.1.2: 0 von 2","Aufbau der Anzeige (ein großes Foto, Elemente auf dem Foto) wird nicht genannt."),
 (2487,1840,"6","1.1.3: 6 von 7","Taylor Swift (1), „milk beard“ (1), Kleid mit Blumenmuster (1), rote Wand (1); Gitarre ohne Sitzen/Anlehnen und Lächeln ohne Blickkontakt: zusammen 1 von 2. Haare fehlen (0). Zusatzpunkt für Armbänder und Ohrringe (1 ZP)."),
 (2504,2654,"1","1.1.4: 1 von 2","Weiße Buchstaben richtig (1). Position falsch: „top right corner“ statt oben links (0)."),
 (2504,2836,"2","1.1.5: 2 von 3","Text rechts neben Taylor Swift (1), weiße Buchstaben (1). Überschrift „Swift pick“ in der Beschreibung nicht genannt (0)."),
 (2504,3080,"4","1.1.6: 4 von 6","„leaner“ (1), drei Gläser am Tag (1), „chooses milk“ (1) und „build muscle“ (1), die letzten beiden aus dem Analyseteil. Ich-Form, Studien und „Music to my ears“ fehlen."),
]),
2:('90d8fb1e',[
 (2290,616,"2","1.1.7: 2 von 2","„website logo and website link under it“: Logo und Webadresse unter dem Text genannt."),
 (2290,790,"1","1.1.8: 1 (max. 4)","Zusatz: unscharfer Hintergrund, Detail am rechten Handgelenk."),
 (2290,982,"20","Summe 1.1: 20 von 29",""),
 (2302,1468,"2","1.2.1: 2 von 3","Milchbart als Eye-catcher, weckt Interesse (1); „something everybody has experienced“ = nahbar (1). Markenzeichen der Kampagne fehlt."),
 (2302,1844,"4","1.2.2: 4 von 4","Große Fangemeinde, beeinflusst Teenager (2); Fans kaufen und trinken mehr Milch, weil sie es tut (2)."),
 (2318,2157,"0","1.2.3: 0 von 3","Farben nur als „warm and bright“ gedeutet (unter 1.2.10 gewertet). Bezug Weiß = Milch, Kontrast zur Wand und Gitarre fehlen."),
 (2337,2796,"2","1.2.4: 2 von 3","„fast or easy pick“: swift = schnell, pick = Wahl erkannt (1), Milch als schnelle Wahl (1). Doppeldeutung Nachname/Plektrum fehlt."),
 (2337,3191,"2","1.2.5: 2 von 3","Persönliche Aussage „she herself chooses to drink milk“ (1), „personal connection to the consumers“ (1). Milch als Teil ihres Erfolgs fehlt."),
 (2354,3538,"0","1.2.6: 0 von 2","„Music to my ears“ wird nicht erwähnt."),
]),
3:('3dbfc4bf',[
 (2588,474,"1","1.2.7: 1 von 3","Wunsch nach schlankem, muskulösem Körper angesprochen (Desire) (1). Studien und Kontrast zu zuckerhaltigen Getränken werden nicht untersucht."),
 (2588,1018,"0","1.2.8: 0 von 2","Imperative, Aufzählung und Zahl im Anzeigentext werden nicht untersucht."),
 (2588,1386,"1","1.2.9: 1 von 2","Frage „got milk?“ als Handlungsaufforderung erkannt (1). Sprachliche Gestaltung (Umgangssprache, Kleinschreibung) fehlt."),
 (2588,1690,"4","1.2.10: 4 (max. 8)","AIDA vollständig am Material angewendet (3). Wirkung von Farben und Lächeln: „warm and comforting feeling“ (1)."),
 (2588,1974,"16","Summe 1.2: 16 von 25",""),
 (2588,2390,"4","1.3.1: 4 von 7","Urteil „very well made“ (1), große Fangemeinde (1 von 2), Milchbart fällt auf und weckt sofort Interesse (2). Kritische Punkte (bezahlt, kein Beweis, vage Studien) fehlen (0 von 2)."),
 (2588,2844,"1","1.3.2: 1 von 4","Wirkung auf das Publikum angedeutet: „you already get the attention of most of the people“ (1). Kritik an Schlankheitsversprechen und Interessen der Industrie fehlt."),
 (2588,3302,"1","1.3.3: 1 von 1","Eigene Meinung vorhanden: „I would say …“, „what really stands out to me“."),
 (2588,3404,"6","Summe 1.3: 6 von 12",""),
 (1330,3545,"→ 42 / 66","Teil A gesamt: 42 von 66","20 + 16 + 6"),
]),
4:('aa74d783',[
 (2577,868,"✓","1.1: Textformat, ohne Punkte","Einleitung vorhanden (Titel, Autor, Zeitung, Thema). Datum falsch übertragen: „21 June“ statt 18 June 2021."),
 (2577,1042,"4","1.2: 4 von 4","Zwei Coca-Cola-Flaschen entfernt (1), Pressekonferenz (1), Wasserflasche gezeigt (1); „agua“ fehlt (0). SP: Protest gegen Werbung für zuckerhaltige Getränke (1)."),
 (2577,1287,"2","1.3: 2 von 4","Flasche entfernt (1), Heineken alkoholfrei (1). Anlass (Pressekonferenz nach Sieg über Deutschland) und Heineken als EM-Sponsor fehlen."),
 (2577,1587,"2","1.4: 2 von 5","Gruppe von Manchester United (1) boykottiert Sponsoren-Event (1). Jahr 2018, Grund (Reiseplanung) und Champions League fehlen."),
 (2577,1918,"2","1.5: 2 (max. 2)","Zusatz: Coca-Cola als EM-Sponsor, „health fanatic“, Schlussgedanke zum Ende von Product Placement."),
 (2577,2018,"10","Summe Teil B: 10 von 13",""),
 (1250,2225,"→ 10 / 13","",""),
 (1595,2395,"52","Inhalt gesamt: 52 von 79","Teil A 42 + Teil B 10 = 52 Punkte (66 %)."),
]),
}
for p,(f,items) in P.items():
    src=ImageOps.exif_transpose(Image.open(U+f+'-image.jpg')).convert('RGB')
    w,h=src.size
    im=Image.new('RGB',(w+PW,h),(255,255,255)); im.paste(src,(0,0)); d=ImageDraw.Draw(im)
    d.text((w+40,40),f"GY2-01 – Begründung der Punkte (Seite {p} von 4)",fill=(40,40,40),font=fh)
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
    im.save(f'{W}/out/GY2-01_Erwartungshorizont_S{p}.jpg',quality=86)
    im.resize((1700,int(1700*im.size[1]/im.size[0]))).save(f'{W}/work/ehchk{p}.jpg',quality=80)
