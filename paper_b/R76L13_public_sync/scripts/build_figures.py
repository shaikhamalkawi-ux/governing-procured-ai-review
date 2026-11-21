#!/usr/bin/env python3
"""Journal-width vector redraws of author-selected 99aiB R76L10 candidate figures 1-4,6.
Maintains data/semantics; removes AUTHOR SELECTION drafting artefacts and enlarges labels.
No invented empirical values. Uses verified source manifest and source-register counts.
"""
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
from math import pi,cos,sin
from pathlib import Path
import json
BASE=Path(__file__).parent
O=BASE.parent/'rebuild_figures'; O.mkdir(exist_ok=True)
# Prefer locally installed DejaVu fonts; never bundle or redistribute font binaries.
def _available_fonts():
    from os import environ
    options = [
        (Path(environ.get('DEJAVU_REGULAR', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')),
         Path(environ.get('DEJAVU_BOLD', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))),
        (Path('/usr/local/share/fonts/DejaVuSans.ttf'),
         Path('/usr/local/share/fonts/DejaVuSans-Bold.ttf')),
    ]
    for regular, bold in options:
        if regular.is_file() and bold.is_file():
            pdfmetrics.registerFont(TTFont('DV', str(regular)))
            pdfmetrics.registerFont(TTFont('DVB', str(bold)))
            return
    # Fallback is a built-in standard PDF font, not a packaged font asset.
    from reportlab.pdfbase.pdfmetrics import Font
    pdfmetrics.registerFont(Font('DV','Helvetica','WinAnsiEncoding'))
    pdfmetrics.registerFont(Font('DVB','Helvetica-Bold','WinAnsiEncoding'))

_available_fonts()
N='#10293C';D='#142F41';G='#5C7183';M='#778998'; BLUE='#47799E'; TEAL='#167D79'; AMBER='#B6742A';SLATE='#6C8298';RED='#B2615A';TAUPE='#AFA5A3';LIGHT='#EAF1F5'; LINE='#D8E2E8'; WHITE='#FFFFFF'; BG='#F4F7F9'
W=505

def drawtext(c,x,y,s,size=9,color=D,bold=False,align='left'):
    c.setFillColor(HexColor(color));c.setFont('DVB' if bold else 'DV',size)
    if align=='right':c.drawRightString(x,y,str(s))
    elif align=='center':c.drawCentredString(x,y,str(s))
    else:c.drawString(x,y,str(s))

def rect(c,x,y,w,h,fill,r=0,stroke=None):
    c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke or fill))
    if r:c.roundRect(x,y,w,h,r,fill=1,stroke=int(bool(stroke)))
    else:c.rect(x,y,w,h,fill=1,stroke=int(bool(stroke)))

def stroke(c,x0,y0,x1,y1,color=LINE,lw=.8,dash=None):
    c.saveState();c.setStrokeColor(HexColor(color));c.setLineWidth(lw)
    if dash:c.setDash(*dash)
    c.line(x0,y0,x1,y1);c.restoreState()

def init(name,h,title,subtitle):
    c=canvas.Canvas(str(O/name),pagesize=(W,h),pageCompression=1,initialFontName='DV',initialFontSize=9)
    c.setTitle(title);c.setAuthor('99aiB author-review: source-verified journal figures')
    rect(c,0,0,W,h,WHITE)
    drawtext(c,14,h-26,title,12.5,N,True)
    drawtext(c,14,h-43,subtitle,8.5,G)
    stroke(c,14,h-52,W-14,h-52,LINE,1)
    return c

def end(c):c.showPage();c.save()

# Figure 1
h=217;c=init('Figure1_Auditor_Evidence_Chain.pdf',h,
    'From acquisition to an auditable claim','Each link is a distinct record request, not a maturity ladder or observed causal chain')
steps=[('01','ACQUISITION',['Buyer, contract,','AI object'],BLUE),('02','AUTHORITY',['Operative clause','or statute'],SLATE),('03','EXERCISE',['Dated inspection','or request'],TEAL),('04','RESPONSE',['Named supplier,','version, change'],AMBER),('05','OUTCOME',['Metric, period,','comparator'],RED)]
bx=11;bw=89;gap=12.0
for i,(num,name,sub,color) in enumerate(steps):
    x=bx+i*(bw+gap);rect(c,x,64,bw,82,BG,r=6,stroke=LINE)
    rect(c,x+25,131,39,28,color,r=14)
    drawtext(c,x+44.5,140,num,10,WHITE,True,'center')
    drawtext(c,x+bw/2,115,name,7.9,N,True,'center')
    for j,s in enumerate(sub):drawtext(c,x+bw/2,96-j*13,s,7.5,D,False,'center')
    if i<4:
        stroke(c,x+bw+1,113,x+bw+gap-2,113,M,.9,[2,2])
        c.setStrokeColor(HexColor(M));c.line(x+bw+gap-6,116,x+bw+gap-2,113);c.line(x+bw+gap-6,110,x+bw+gap-2,113)
rect(c,18,16,W-36,32,LIGHT,r=6)
drawtext(c,W/2,29,'Stop at the strongest claim actually supported by the dated source.',8.3,N,True,'center');end(c)

# Figure 2
h=242;c=init('Figure3_OECD_National_Indicators.pdf',h,
    'Public-sector AI: acquisition support versus oversight','OECD 2026 country-level reporting, 36 participating governments')
labels=[('Central support for', 'buying AI',21,BLUE),('Audit after','deployment',11,TEAL),('Any AI impact','measurement',10,AMBER)]
startx=218;scale=251/70; ys=[165,115,65]
for y,(a,b,n,color) in zip(ys,labels):
    drawtext(c,14,y+12,a,9,N,True);drawtext(c,14,y-1,b,9,N,True)
    drawtext(c,14,y-16,f'{n} / 36 governments',8,G)
    v=100*n/36;rect(c,startx,y-8,scale*v,25,color,r=3)
    drawtext(c,min(startx+scale*v+7,468),y, f'{v:.1f}%',9.5,N,True)
stroke(c,startx,28,startx+251,28,M,.8)
for val in range(0,71,10):
    x=startx+scale*val;stroke(c,x,28,x,22,M,.7);drawtext(c,x,10,f'{val}%',7.5,G,False,'center')
end(c)

# Figure 3
h=265;c=init('Figure2_State_AI_Contract_Clauses.pdf',h,
    'Selected clause types in U.S. state AI contracts','Kim and Kesari (2026): 215 contracts, 3,771 provisions, CA / FL / UT')
labels=[('Boilerplate / generic',77.0,BLUE),('Transparency',5.3,TEAL),('Cybersecurity',3.0,AMBER),('Fairness / accountability',2.4,SLATE)]
startx=194;scale=259/80;ys=[189,151,113,75]
for y,(name,v,color) in zip(ys,labels):
    drawtext(c,14,y+4,name,8.6,N,True)
    rect(c,startx,y-3,scale*v,21,color,r=2)
    drawtext(c,min(startx+scale*v+8,468),y+4,f'{v:.1f}%',9.5,N,True)
stroke(c,startx,46,startx+259,46,M,.8)
for val in range(0,81,20):
    x=startx+scale*val;stroke(c,x,46,x,41,M,.7);drawtext(c,x,29,f'{val}%',7.7,G,False,'center')
drawtext(c,W/2,12,'Shares of classified provisions; selected categories are not a success-rate sample.',7.4,G,False,'center')
end(c)

# Figure 4
h=261;c=init('Figure4_GOV_Voice_Weights.pdf',h,
    'GOV Voice: announced evaluation design','Tender UK4 (May 2026) — published weights and an arithmetic decomposition')
left=48;width=410
# Top original 70/30
label_y=181;drawtext(c,left,label_y+17,'Tender headline weights',9,N,True)
rect(c,left,label_y-9,.70*width,24,BLUE,r=1);rect(c,left+.70*width,label_y-9,.30*width,24,AMBER,r=1)
drawtext(c,left+.35*width,label_y, 'Quality 70%',9,WHITE,True,'center');drawtext(c,left+.85*width,label_y, 'Commercial 30%',9,WHITE,True,'center')
# Bottom conditional
label_y=128;drawtext(c,left,label_y+21,'Derived share of the TOTAL tender score',9,N,True)
segments=[(42,TEAL,'Product'),(21,SLATE,'Written'),(7,RED,'Social'),(30,AMBER,'Commercial')]
x=left
for val,color,name in segments:
    rect(c,x,label_y-8,width*val/100,26,color);txt=f'{val}%'
    if val>=10:drawtext(c,x+width*val/200,label_y,txt,9,WHITE,True,'center')
    x+=width*val/100
stroke(c,left,88,left+width,88,LINE,.9)
for i,(n,color,label) in enumerate(segments):
    col=i%2;row=i//2;xx=50+col*224;yy=74-row*22
    rect(c,xx,yy-2,9,9,color,r=3);drawtext(c,xx+15,yy, f'{label}: {n}% of total',8.7,D)
rect(c,29,10,447,24,LIGHT,r=6)
drawtext(c,252,19,'0.70 x (60%, 30%, 10%) = (42%, 21%, 7%); + 30% commercial = 100%',7.2,N,True,'center')
end(c)

# Supplement figure S1
h=254;c=init('SupplementaryFigureS1_Source_Roles.pdf',h,
    'What the 93 cited sources contain','Descriptive roles in the selected bibliography — not 93 eligible studies')
vals=[34,25,16,9,6,3]; names=['Official / public records','Empirical / observed research','Legal / doctrinal','Standards / methods','Reviews / methodology','Other scholarship'];cols=[BLUE,TEAL,AMBER,SLATE,RED,TAUPE]
# doughnut geometrically exact slices
cx,cy,ro,ri=119,120,86,48
angle=90
for value,color in zip(vals,cols):
    nxt=angle-360*value/93
    path=c.beginPath();n=round((angle-nxt)/2);n=max(n,10)
    for k in range(n+1):
        a=(angle+(nxt-angle)*k/n)*pi/180;x=cx+ro*cos(a);y=cy+ro*sin(a)
        if k==0:path.moveTo(x,y)
        else:path.lineTo(x,y)
    for k in range(n,-1,-1):
        a=(angle+(nxt-angle)*k/n)*pi/180;x=cx+ri*cos(a);y=cy+ri*sin(a);path.lineTo(x,y)
    path.close();c.setFillColor(HexColor(color));c.drawPath(path,fill=1,stroke=0)
    angle=nxt
# Contrast separators between the six correctly proportional citation groups.
a=90
for value in vals:
    ang=a*pi/180
    stroke(c,cx+(ri-1)*cos(ang),cy+(ri-1)*sin(ang),cx+(ro+1)*cos(ang),cy+(ro+1)*sin(ang),WHITE,2.0)
    a-=360*value/93
rect(c,cx-24,cy-30,48,60,WHITE,r=0)
# redraw white circular center to avoid square visual
c.setFillColor(HexColor(WHITE));c.circle(cx,cy,ri+1,stroke=0,fill=1)
drawtext(c,cx,cy+4,'93',27,N,True,'center');drawtext(c,cx,cy-14,'sources',9,G,False,'center')
for i,(v,name,color) in enumerate(zip(vals,names,cols)):
    y=192-i*28
    c.setFillColor(HexColor(color));c.circle(235,y,5,stroke=0,fill=1)
    drawtext(c,247,y-3,name,8.4,D)
    drawtext(c,493,y-3,f'{v}  ({100*v/93:.1f}%)',8.6,N,True,'right')
drawtext(c,253,9,'Percentages sum to 100.1% because of one-decimal rounding.',7.1,G,False,'center')
end(c)
manifest={"scientific_baseline":"R76L10","new_version":"R76L13 (figures inherited from R76L11)","assets":["Figure1_Auditor_Evidence_Chain.pdf","Figure3_OECD_National_Indicators.pdf","Figure2_State_AI_Contract_Clauses.pdf","Figure4_GOV_Voice_Weights.pdf","SupplementaryFigureS1_Source_Roles.pdf"],"counts":{"source_roles":[34,25,16,9,6,3],"total":93,"oecd":{"n":36,"support":21,"audit":11,"impact":10},"state_contracts":215,"state_provisions":3771,"clause_proportions":[77.0,5.3,3.0,2.4],"govvoice_quality":70,"govvoice_commercial":30,"govvoice_quality_subweights":[60,30,10],"govvoice_derived":[42,21,7,30]},"claim_guardrails":["None of these charts are new empirical study results","OECD country indicators are not contract cohort transitions","Clause percentages are selected provision shares, not contract success rates","Tender weights are planned criteria and derived arithmetic, not scores achieved","Cited-source distribution is a purposive bibliography, not systematic eligible studies"]}
(O/'FIGURE_DATA_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print('created vector PDFs in',O)
