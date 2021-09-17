import feedparser
from bs4 import BeautifulSoup
import qrcode
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import time
import textwrap 


Data=feedparser.parse("http://url_to_your_rsshub/people/opinion/223228")
print (Data.feed.title)

print (Data.entries[4].title)
ContentStart = Data.entries[4].description.index("<div class=\"box_pic\"></div>") 
ContentEnd = Data.entries[4].description.index("<!--left-banner-->") 

Content = BeautifulSoup(Data.entries[4].description[ContentStart:ContentEnd],features="html.parser")

print (Content.get_text())

qr = qrcode.make(Data.entries[4].link)

res = Image.new("RGB",(2100,2970),"#fff")

# Customize your logo here
logo = Image.open("logo.png")
qr = qr.resize((230,230),Image.ANTIALIAS)
boxqr = (1830,50,2060,280)
# Change the size of you logo
logo = logo.resize((264, 100),Image.ANTIALIAS)
boxlogo = (70,90,334,190)
res.paste(qr, boxqr)
res.paste(logo, boxlogo)

# Customize your fonts here
FontBold = ImageFont.truetype("font1.ttf",55) 
FontMedium = ImageFont.truetype("font2.ttf",30)
FontRegular = ImageFont.truetype("font3.ttf",47)       

titlepos = (70,220)
timepos = (450,90)
contentpos = (70,300)
copyrightpos = (450,150)
color = (0,0,0)
draw = ImageDraw.Draw(res)
draw.text(titlepos,Data.entries[4].title,color,font=FontBold)
draw.text(copyrightpos,"© KiraKiseki, Project DailyPrint",color,font=FontMedium)
draw.text(timepos,time.strftime("%a, %b %d %H:%M:%S %Y Asia/Shanghai GMT+08:00", time.strptime(Data.entries[4].published,"%a, %d %b %Y %H:%M:%S GMT")) ,color,font=FontMedium)


Contentstr=Content.get_text().replace('　　', '\n\r  ')
para = textwrap.wrap(Contentstr, width=42) 

current_h, pad = 50, 10 
for line in para: 
    w, h = draw.textsize(line, font=FontRegular) 
    draw.text((70, current_h+300), line,color,font=FontRegular) 
    current_h += h + pad 


res.save('res.png')

