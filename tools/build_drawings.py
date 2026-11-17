from pathlib import Path
import math,html,json
import numpy as np
from shapely.geometry import Polygon,LineString,box,Point
from shapely.ops import unary_union
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
import fitz
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'drawings'/'number-14';OUT.mkdir(parents=True,exist_ok=True)
for d in ['svg','pdf','qa']:(OUT/d).mkdir(exist_ok=True)
from drawing_fonts import register_drawing_font
register_drawing_font();META=[]
class Sheet:
 def __init__(self,ex,title,scale='1:1',status='PROPOSED DETAIL DIMENSIONS - INSTRUCTOR REVIEW'):
  self.ex=ex;self.title=title;self.scale=scale;self.els=[];self.filename=f'Exercise_{ex}_Variant_14';self.pdf=canvas.Canvas(str(OUT/'pdf'/(self.filename+'.pdf')),pagesize=(420*mm,297*mm));self.pdf.setTitle(f'Exercise {ex} - Variant 14 - {title}');self.pdf.setAuthor('Student 14')
  self.rect(10,7,403,283,w=.5)
  if ex=='1a':self.text(233,28,'EXERCISE 1a / VARIANT 14',3.6);self.text(233,34,'PROVISIONAL RECONSTRUCTION',2.6)
  else:self.text(15,15,f'EXERCISE {ex} / VARIANT 14 / {title.upper()}',4);self.text(15,21,status,2.5)
  self.rect(233,263,180,27,w=.5);self.line(233,274,413,274,.25);self.line(233,283,413,283,.25)
  for x in [271,319,365]:self.line(x,274,x,290,.25)
  self.text(236,270,title,3.2)
  for x,t in [(236,'STUDENT 14'),(274,'A3 LANDSCAPE'),(322,'SCALE '+scale),(368,'UNITS mm')]:self.text(x,280,t,2.5)
  for x,t in [(236,('14.01.00' if ex=='6' else f'14.{ex}.00')),(274,'2026-11-17'),(322,'FIRST ANGLE'),(368,'SHEET 1 / 1')]:self.text(x,287,t,2.5)
 def line(self,x1,y1,x2,y2,w=.5,style='',color='black'):
  dash={'hidden':'2,1','center':'7,1.3,1,1.3','cut':'9,2,1.5,2'}.get(style,'');self.els.append(f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" stroke="{color}" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>');c=self.pdf;c.setStrokeColorRGB(*((0,0,0) if color=='black' else (.65,.65,.65)));c.setLineWidth(w*mm);c.setDash([float(n)*mm for n in dash.split(',')] if dash else []);c.line(x1*mm,(297-y1)*mm,x2*mm,(297-y2)*mm)
 def poly(self,pts,closed=False,w=.5,style=''):
  if len(pts)<2:return
  dash={'hidden':'2,1','center':'7,1.3,1,1.3','cut':'9,2,1.5,2'}.get(style,'');tag='polygon' if closed else 'polyline';coords=' '.join(f'{x:.4f},{y:.4f}' for x,y in pts);self.els.append(f'<{tag} points="{coords}" fill="none" stroke="black" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>');c=self.pdf;c.setStrokeColorRGB(0,0,0);c.setLineWidth(w*mm);c.setDash([float(n)*mm for n in dash.split(',')] if dash else []);path=c.beginPath();path.moveTo(pts[0][0]*mm,(297-pts[0][1])*mm)
  for x,y in pts[1:]:path.lineTo(x*mm,(297-y)*mm)
  if closed:path.close()
  c.drawPath(path)
 def white(self,x,y,w,h):
  self.els.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white"/>');c=self.pdf;c.setFillColorRGB(1,1,1);c.rect(x*mm,(297-y-h)*mm,w*mm,h*mm,fill=1,stroke=0)
 def whitecircle(self,x,y,r):
  self.els.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="white"/>');c=self.pdf;c.setFillColorRGB(1,1,1);c.circle(x*mm,(297-y)*mm,r*mm,fill=1,stroke=0)
 def rect(self,x,y,wid,hei,w=.5,r=0):
  if not r:self.poly([(x,y),(x+wid,y),(x+wid,y+hei),(x,y+hei)],True,w);return
  pts=[]
  for cx,cy,a in [(x+wid-r,y+r,-90),(x+wid-r,y+hei-r,0),(x+r,y+hei-r,90),(x+r,y+r,180)]:pts +=[(cx+r*math.cos(math.radians(t)),cy+r*math.sin(math.radians(t))) for t in np.linspace(a,a+90,19)]
  self.poly(pts,True,w)
 def circle(self,x,y,r,w=.5,style=''):self.arc(x,y,r,0,360,w,style)
 def arc(self,x,y,r,a,b,w=.5,style=''):self.poly([(x+r*math.cos(math.radians(t)),y+r*math.sin(math.radians(t))) for t in np.linspace(a,b,max(8,int(abs(b-a)/3)+1))],w=w,style=style)
 def text(self,x,y,t,size=2.8,align='left',rotate=0):
  t=str(t);anc={'left':'start','center':'middle','right':'end'}[align];self.els.append(f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" text-anchor="{anc}"'+(f' transform="rotate({rotate} {x} {y})"' if rotate else '')+'>'+html.escape(t)+'</text>');c=self.pdf;c.saveState();c.setFillColorRGB(0,0,0);c.translate(x*mm,(297-y)*mm);c.rotate(-rotate);c.setFont('Arial',size*mm);{'left':c.drawString,'center':c.drawCentredString,'right':c.drawRightString}[align](0,0,t);c.restoreState()
 def center(self,x,y,rx,ry=None):
  ry=rx if ry is None else ry;self.line(x-rx,y,x+rx,y,.18,'center');self.line(x,y-ry,x,y+ry,.18,'center')
 def arrow(self,x,y,angle,size=2.7):
  a=math.radians(angle);u=np.array([math.cos(a),math.sin(a)]);v=np.array([-u[1],u[0]]);p=np.array([x,y]);q=p+size*u;self.poly([tuple(q+.4*v),tuple(p),tuple(q-.4*v)],w=.22)
 def dimh(self,x1,x2,y1,y2,yd,label):
  self.line(x1,y1,x1,yd+(-2 if yd<min(y1,y2) else 2),.18);self.line(x2,y2,x2,yd+(-2 if yd<min(y1,y2) else 2),.18);self.line(x1,yd,x2,yd,.18);self.arrow(x1,yd,0);self.arrow(x2,yd,180);self.text((x1+x2)/2,yd-1.7,label,2.8,'center')
 def dimv(self,y1,y2,x1,x2,xd,label):
  self.line(x1,y1,xd+(-2 if xd<min(x1,x2) else 2),y1,.18);self.line(x2,y2,xd+(-2 if xd<min(x1,x2) else 2),y2,.18);self.line(xd,y1,xd,y2,.18);self.arrow(xd,y1,90);self.arrow(xd,y2,270);self.text(xd-1.7,(y1+y2)/2,label,2.8,'center',-90)
 def leader(self,p,elbow,end,label):
  self.poly([p,elbow,end],w=.18);self.arrow(*p,math.degrees(math.atan2(elbow[1]-p[1],elbow[0]-p[0])));self.text(end[0],end[1]-1.5,label,2.8)
 def hatch(self,poly,spacing=3,reverse=False):
  if isinstance(poly,list):poly=Polygon(poly)
  if poly.is_empty:return
  x0,y0,x1,y1=poly.bounds
  for b in np.arange(y0-x1-5,y1-x0+5,spacing):
   line=LineString([(x0-5,x0-5+b),(x1+5,x1+5+b)]) if not reverse else LineString([(x0-5,-(x0-5)+b+x0+x1),(x1+5,-(x1+5)+b+x0+x1)])
   g=poly.intersection(line)
   if g.is_empty:continue
   for part in ([g] if g.geom_type=='LineString' else getattr(g,'geoms',[])):
    if part.geom_type=='LineString':self.line(*part.coords[0],*part.coords[-1],.16)
 def sectionpoly(self,pts,holes=[],reverse=False):
  p=Polygon(pts,holes);self.hatch(p,reverse=reverse);self.poly(pts,True)
  for h in holes:self.poly(h,True)
 def rough(self,x,y,value='3.2'):self.poly([(x,y-2),(x+2,y),(x+5,y-6),(x+11,y-6)],w=.25);self.text(x+5,y-7,'Ra '+value,2.5)
 def frame(self,x,y,values):
  for i,v in enumerate(values):
   xx=x+i*13;self.rect(xx,y,13,6,w=.25)
   if v=='↗':self.line(xx+4,y+4.5,xx+8.5,y+1.2,.25);self.arrow(xx+8.5,y+1.2,144,size=1.4)
   elif v=='∥':self.line(xx+4,y+4.5,xx+6,y+1.2,.25);self.line(xx+7,y+4.5,xx+9,y+1.2,.25)
   else:self.text(xx+6.5,y+4.2,v,2.8,'center')
 def table(self,x,y,widths,rows,height=6,size=2.6):
  for j,row in enumerate(rows):
   xx=x
   for wid,t in zip(widths,row):self.rect(xx,y+j*height,wid,height,w=.18);self.text(xx+2,y+j*height+height*.7,t,size);xx+=wid
 def notes(self,x,y,lines,size=2.8):
  for j,t in enumerate(lines):self.text(x,y+j*5,t,size)
 def finish(self):
  self.pdf.showPage();self.pdf.save();(OUT/'svg'/(self.filename+'.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297"><rect width="420" height="297" fill="white"/>'+''.join(self.els)+'</svg>',encoding='utf-8');META.append({'exercise':self.ex,'title':self.title,'scale':self.scale,'file':self.filename});return self

def mappts(pts,ox,oy,s=1):return [(ox+s*x,oy-s*y) for x,y in pts]
def arcpts(cx,cy,r,a,b,n=40):return [(cx+r*math.cos(t),cy+r*math.sin(t)) for t in np.linspace(math.radians(a),math.radians(b),n)]
s=Sheet('1','Flat sheet component');ye=math.sqrt(40**2-12**2)
p=[(-40,60),(40,60),(80,49),(80,ye)]+arcpts(92,0,40,math.degrees(math.acos(-.3)),360-math.degrees(math.acos(-.3)))[1:]+[(80,-49),(40,-60),(40,-52),(-40,-52),(-40,-60),(-80,-49),(-80,-ye)]+arcpts(-92,0,40,-math.degrees(math.acos(.3)),math.degrees(math.acos(.3)))[1:]+[(-80,49)]
ox,oy=139,158;s.poly(mappts(p,ox,oy),True);s.poly(mappts([(0,44),(44,0),(0,-44),(-44,0)],ox,oy),True);s.line(ox,85,ox,230,.18,'center');s.line(ox-52,oy,ox+52,oy,.18,'center')
s.dimh(ox-80,ox+80,oy-49,oy-49,78,'160');s.dimv(oy-60,oy+60,ox+40,ox+40,235,'120');s.dimh(ox-40,ox+40,oy-60,oy-60,88,'80');s.dimv(oy-60,oy-49,ox+40,ox+80,249,'11');s.dimh(ox-40,ox+40,oy+52,oy+52,232,'80');s.dimv(oy+52,oy+60,ox+40,ox+40,221,'8');s.leader((ox+55,oy-16),(265,110),(283,110),'2 × R40');s.leader((ox-22,oy-22),(67,110),(32,110),'Square at 45°');s.dimh(ox-44,ox+44,oy,oy,oy+1,'88 across corners');s.text(28,251,'t = 4 mm | All internal cut-outs through.',3)
s.notes(281,134,['PROPOSED NOMINAL GEOMETRY','Symmetry about vertical centre line.','Arc centres: x = ±92, y = 0.','Square centre: x = 0, y = 0.','Upper edge: y = +60.','Lower notch floor: y = −52.','Lower tips: y = −60.','Origin: square centre.'],2.6);s.finish()
profile=[(0,32),(44,43),(44,55),(68,55),(68,51),(76,51),(76,55),(135,55),(150,49),(150,27),(125,27),(58,20),(58,0),(46,0),(20,20),(0,20)]
def rotational(ex,maxd,ends=False):
 s=Sheet(ex,'Axisymmetric component' if ends else 'Rotational component half section');k=maxd/110;ox,oy=(133,143) if ends else (94,140);pr=[(x,r*k) for x,r in profile];s.sectionpoly([(ox+x,oy+r) for x,r in pr]);s.poly([(ox+x,oy-r) for x,r in pr[:9]]);s.line(ox,oy-pr[0][1],ox,oy,.5);s.line(ox+150,oy-pr[8][1],ox+150,oy,.5)
 for x,r in [(44,55*k),(68,55*k),(76,55*k),(135,55*k)]:s.line(ox+x,oy-r,ox+x,oy,.5)
 s.line(ox-8,oy,ox+158,oy,.18,'center');s.dimh(ox,ox+150,oy+32*k,oy+49*k,226,'150');s.dimv(oy-55*k,oy+55*k,ox+100,ox+100,ox+(154 if ends else 170),'Ø'+str(maxd));s.dimh(ox+68,ox+76,oy-55*k,oy-55*k,61,'8');s.dimh(ox,ox+44,oy-32*k,oy-55*k,72,'44');s.dimh(ox,ox+46,oy+32*k,oy,242,'46 left depth');s.dimh(ox+125,ox+150,oy+27*k,oy+27*k,210,'25')
 if ends:
  for cx,which,rads in [(61,'RIGHT END',[65,49*k,27*k]),(355,'LEFT END',[65,43*k,32*k,20*k])]:
   for r in sorted(set(rads)):
    group=[]
    for theta in np.linspace(-math.pi,math.pi,3201):
     x,y=cx+r*math.cos(theta),oy+r*math.sin(theta);bound=cx-3+1.5*math.sin((y-oy)*.5);keep=x>=bound if cx<100 else x<=bound
     if keep:group.append((x,y))
     elif len(group)>1:s.poly(group);group=[]
    if len(group)>1:s.poly(group)
   s.center(cx,oy,12,72);ys=np.linspace(oy-68,oy+68,90);s.poly([(cx-3+1.5*math.sin((y-oy)*.5),y) for y in ys],w=.18);s.text(cx,45,which,3,'center')
  s.notes(19,250,['Partial end views; curved limits are view breaks.','Lower half: axial section; holes unhatched.'],2.6)
 else:
  s.table(284,30,[13,13,13,13],[[str(x),str(r),str(x2),str(r2)] for (x,r),(x2,r2) in zip(profile[:8],profile[8:])],height=5.5,size=2.3);s.text(284,28,'PROFILE x / r (mm), left and right columns',2.4);s.leader((ox,oy+20),(51,182),(25,182),'Ø40 left opening');s.leader((ox+150,oy+27),(275,185),(291,185),'Ø54 right recess');s.leader((ox+58,oy+20),(275,195),(291,195),'Ø40 cone end');s.rough(210,85,'3.2');s.rough(299,249,'12.5');s.frame(294,150,['↗','0.05','A']);s.leader((ox+135,oy-55),(281,153),(294,153),'');s.rect(ox+43,oy-72,6,6,w=.25);s.text(ox+46,oy-67.5,'A',3,'center');s.line(ox+51,oy-55,ox+46,oy-66,.25);s.notes(292,203,['General Ra 12.5 proposed.','Selected surface Ra 3.2.','Datum A: Ø110 axis.','Run-out 0.05/A proposed.'],2.6)
 s.finish()
rotational('2',110);rotational('4a',130,True)
def projectmesh(s,faces,proj,offset):
 u,v,d=map(np.array,proj);ox,oy=offset;polys=[]
 for face in faces:
  pts=np.array(face);uv=np.column_stack((pts@u,pts@v));p=Polygon(uv)
  if p.is_valid and p.area>1e-6:polys.append((p,np.linalg.lstsq(np.column_stack((uv,np.ones(len(uv)))),pts@d,rcond=None)[0]))
 edges={}
 for face in faces:
  for p,q in zip(face,face[1:]+face[:1]):edges[tuple(sorted([tuple(np.round(p,7)),tuple(np.round(q,7))]))]=(p,q)
 for p,q in edges.values():
  p=np.array(p);q=np.array(q);dt=q-p;n=max(2,int(np.linalg.norm(dt)*2));last=None;start=None
  for i in range(n):
   r=p+(i+.5)/n*dt;uv=np.array([r@u,r@v]);dep=r@d;hid=any(poly.covers(Point(uv)) and co@np.r_[uv,1]>dep+1e-5 for poly,co in polys);typ='hidden' if hid else ''
   if last!=typ:
    if last is not None:
     pp=p+start*dt;qq=p+i/n*dt;s.line(ox+pp@u,oy-pp@v,ox+qq@u,oy-qq@v,.18 if last else .5,last)
    start=i/n;last=typ
  pp=p+start*dt;s.line(ox+pp@u,oy-pp@v,ox+q@u,oy-q@v,.18 if last else .5,last)
 return lambda p:(ox+np.dot(p,u),oy-np.dot(p,v))
s=Sheet('2a','Pyramid cut by perpendicular plane');tan=math.tan(math.radians(50));base=np.array([[-55,-8,0],[-32,42,0],[55,25,0],[15,-52,0]],float);verts=list(base)+[np.array([0,0,90.])];faces=[[0,1,2,3],[0,4,1],[1,4,2],[2,4,3],[3,4,0]]
def fp(p):return p[2]-45-tan*p[0]
def clipface(vs):
 out=[]
 for p,q in zip(vs,vs[1:]+vs[:1]):
  a,b=fp(p),fp(q)
  if a<=1e-8:out.append(p)
  if (a<0)!=(b<0):out.append(p+(q-p)*a/(a-b))
 return out
clipped=[clipface([verts[i] for i in f]) for f in faces];clipped=[f for f in clipped if len(f)>=3];sec=[]
for f in clipped:
 for p in f:
  if abs(fp(p))<1e-7 and not any(np.linalg.norm(p-q)<1e-6 for q in sec):sec.append(p)
cc=np.mean(sec,axis=0);sec=sorted(sec,key=lambda p:math.atan2(p[1]-cc[1],np.dot(p-cc,np.array([1,0,tan]))));clipped.append(sec)
for proj,off,name in [(((1,0,0),(0,0,1),(0,-1,0)),(99,145),'FRONT'),(((1,0,0),(0,-1,0),(0,0,1)),(99,222),'TOP'),(((0,-1,0),(0,0,1),(1,0,0)),(271,145),'LEFT SIDE')]:
 P=projectmesh(s,clipped,proj,off);s.text(off[0],off[1]-103 if name!='TOP' else 164,name,3,'center')
 if name!='FRONT':s.hatch([P(p) for p in sec])
 for i,p in enumerate(sec):x,y=P(p);s.circle(x,y,.6,w=.2);s.text(x+1.5,y-1.5,str(i+1),2.5)
 if name=='FRONT':
  s.poly([(44,145),(99,55),(154,145)],w=.16);s.line(55,145-(45-44*tan),145,145-(45+46*tan),.25,'cut');s.text(156,47,'α = 50°',3);s.center(99,100,4,51);s.dimv(55,145,99,99,29,'h = 90');s.text(103,98,'h/2 = 45',2.6)
s.dimh(44,154,230,197,281,'a = 110');s.notes(332,56,['SCHEME II','a = 110 mm','h = 90 mm','α = 50°','Retain base side.','','Base XY coordinates:','A (−55, −8)','B (−32, +42)','C (+55, +25)','D (+15, −52)','Apex (0, 0, 90)','','Coordinates proposed','from scheme proportions.'],2.6);sectiondata=[list(map(float,p)) for p in sec];s.finish()
s=Sheet('3a','Intersection of two cylinders');r1,r2=40,37.5;alpha=math.radians(70);sa,ca=math.sin(alpha),math.cos(alpha);branches=[]
for signz in [-1,1]:
 for signq in [-1,1]:
  arr=[]
  for t in np.linspace(-math.pi/2,math.pi/2,361):
   y=r2*math.sin(t);z=signz*math.sqrt(max(0,r1*r1-y*y));x=(ca*z+signq*math.sqrt(max(0,r2*r2-y*y)))/sa;arr.append(np.array([x,y,z]))
  branches.append(arr)
def viewcurve(arr,u,v,ox,oy,hiddenfunc):
 group=[];previous=None
 for p,q in zip(arr,arr[1:]):
  hid=hiddenfunc((p+q)/2)
  if previous is not None and hid!=previous:
   s.poly(group,w=.18 if previous else .5,style='hidden' if previous else '');group=[]
  if not group:group=[(ox+p@u,oy-p@v)]
  group.append((ox+q@u,oy-q@v));previous=hid
 if group:s.poly(group,w=.18 if previous else .5,style='hidden' if previous else '')
front=(111,104);top=(111,218);side=(277,104)
for off,name,u,v,hid in [(front,'FRONT',np.array([1,0,0]),np.array([0,0,1]),lambda p:p[1]>0),(top,'TOP',np.array([1,0,0]),np.array([0,-1,0]),lambda p:p[2]<0),(side,'LEFT SIDE',np.array([0,-1,0]),np.array([0,0,1]),lambda p:p[0]<0)]:
 ox,oy=off;s.text(ox,164 if name=='TOP' else oy-64,name,3,'center');s.center(ox,oy,65,50)
 if name=='FRONT':
  for z in [-40,40]:s.line(ox-64,oy-z,ox+64,oy-z,.5)
  axis=np.array([ca,sa]);normal=np.array([-sa,ca])
  for sidev in [-1,1]:
   a2=-57*axis+sidev*r2*normal;b2=57*axis+sidev*r2*normal;s.line(ox+a2[0],oy-a2[1],ox+b2[0],oy-b2[1],.5)
  s.line(ox-58*ca,oy+58*sa,ox+58*ca,oy-58*sa,.18,'center');s.arc(ox,oy,24,-70,0,.18);s.text(ox+25,oy-13,'70°',2.8)
 elif name=='TOP':
  for y in [-40,40]:s.line(ox-64,oy+y,ox+64,oy+y,.5)
  for y in [-37.5,37.5]:s.line(ox-30,oy+y,ox+30,oy+y,.18)
 else:s.circle(ox,oy,40)
 for arr in sorted(branches,key=lambda arr:not hid(arr[len(arr)//2])):viewcurve(arr,u,v,ox,oy,hid)
sphere_points=[]
for i,R in enumerate([41,44,48],1):
 ox,oy=front;s.circle(ox,oy,R,w=.14);x=math.sqrt(R*R-r1*r1);t2=math.sqrt(R*R-r2*r2);z=(t2-ca*x)/sa;y2=r1*r1-z*z
 if y2<0:raise ValueError('invalid sphere')
 s.line(ox+x,oy-40,ox+x,oy+40,.16);axis=np.array([ca,sa]);nor=np.array([-sa,ca]);c=t2*axis;pp=c-r2*nor;qq=c+r2*nor;s.line(ox+pp[0],oy-pp[1],ox+qq[0],oy-qq[1],.16)
 for sign in [-1,1]:
  p=np.array([x,sign*math.sqrt(y2),z]);sphere_points.append((R,p.tolist()));num=2*i+(3 if sign<0 else 4)
  for off,u,v in [(front,np.array([1,0,0]),np.array([0,0,1])),(top,np.array([1,0,0]),np.array([0,-1,0])),(side,np.array([0,-1,0]),np.array([0,0,1]))]:
   xx,yy=off[0]+p@u,off[1]-p@v;s.circle(xx,yy,.7,w=.2)
   if sign<0 or off!=front:s.text(xx+1.5,yy-1.5,str(num),2.4)
# Characteristic outline and visibility-change points.
for num,p in [(1,np.array([(ca*40-r2)/sa,0,40])),(2,np.array([(ca*40+r2)/sa,0,40])),(3,np.array([ca*math.sqrt(40**2-r2**2)/sa,-r2,math.sqrt(40**2-r2**2)])),(4,np.array([ca*math.sqrt(40**2-r2**2)/sa,r2,math.sqrt(40**2-r2**2)]))]:
 for off,u,v in [(front,np.array([1,0,0]),np.array([0,0,1])),(top,np.array([1,0,0]),np.array([0,-1,0])),(side,np.array([0,-1,0]),np.array([0,0,1]))]:
  xx,yy=off[0]+p@u,off[1]-p@v;s.circle(xx,yy,.7,w=.2)
  if not(num==4 and off==front) and not(num==2 and off==side):s.text(xx+1.5,yy-1.5,'1=2' if num==1 and off==side else str(num),2.4)
for R,pp in sphere_points[::2]:
 p=np.array(pp);xx=front[0]+p[0];yf=front[1]-p[2];yt=top[1]+p[1];xs=side[0]-p[1];s.line(xx,yf,xx,yt,.1,color='gray');s.line(xx,yf,xs,side[1]-p[2],.1,color='gray')
s.notes(338,58,['TASK 14','d1 = 80 mm','d2 = 75 mm','α = 70°','','Auxiliary spheres','common centre O:','R1 = 41 mm','R2 = 44 mm','R3 = 48 mm','','All four branches shown.','Rear curves dashed.','Sphere circles thin.'],2.6);s.text(27,282,'Cylinder ends illustrative; intersection geometry exact for the stated axes.',2.6);s.finish()
s=Sheet('4','Threaded connection diagram F','2:1')
def connection(ox,oy,detailed):
 def P(x,y):return (ox+x*2,oy+y*2)
 def poly(pts,closed=False,w=.5):s.poly([P(*p) for p in pts],closed,w)
 def ln(x,y,x2,y2,w=.5,st=''):s.line(*P(x,y),*P(x2,y2),w,st)
 upperL=[(-28,0),(-11,0),(-11,14.4),(-6.5,14.4),(-6.5,20),(-28,20)];upperR=[(-x,y) for x,y in upperL];lowerL=[(-28,20),(-6,20),(-6,42),(-5.1,42),(-5.1,45),(0,48),(0,52),(-28,52)];lowerR=[(-x,y) for x,y in lowerL]
 for pts in [upperL,upperR]:s.sectionpoly([P(*p) for p in pts])
 lower_material=unary_union([Polygon(lowerL),Polygon(lowerR)])
 for part in ([lower_material] if lower_material.geom_type=='Polygon' else lower_material.geoms):s.sectionpoly([P(*p) for p in list(part.exterior.coords)[:-1]],reverse=True)
 poly([(-9,0),(-9,12),(-6,12),(-6,39),(-5,40),(5,40),(6,39),(6,12),(9,12),(9,0)],True)
 for sign in [-1,1]:
  poly([(sign*6.3,12),(sign*9.3,12),(sign*9.3,14.4),(sign*6.3,14.4)],True)
  if detailed:ln(sign*4.93,14.4,sign*4.93,39,.18);ln(sign*5.1,40,sign*5.1,45,.5);ln(sign*6,40,sign*6,42,.18)
 if detailed:poly([(-5,0),(-5,6),(0,8.9),(5,6),(5,0)],w=.25)
 else:ln(-9,0,9,12,.18);ln(-9,12,9,0,.18)
 s.line(ox,oy-8,ox,oy+106,.18,'center');cx,cy=ox,oy+140;s.rect(cx-56,cy-25,112,50,w=.5,r=3);s.circle(cx,cy,22);s.circle(cx,cy,18);s.center(cx,cy,28)
 if detailed:s.poly([(cx+11.547*math.cos(math.radians(t)),cy+11.547*math.sin(math.radians(t))) for t in range(0,360,60)],True);s.circle(cx,cy,18.6,w=.18)
 else:s.line(cx-13,cy-13,cx+13,cy+13,.18)
 return P
p1=connection(98,53,True);p2=connection(275,53,False);s.text(98,39,'DETAILED SECTION',3.2,'center');s.text(275,39,'SIMPLIFIED SECTION',3.2,'center');s.leader(p1(6,31),(148,105),(159,105),'M12');s.dimv(53,93,42,42,29,'20');s.dimv(93,157,42,42,20,'32');s.dimh(76,120,53,53,45,'Ø22 recess')
s.notes(29,233,['Diagram F: upper clearance hole / lower blind tapped hole.','Components 3 + 11: cylindrical-head bolt and spring washer.','Selected: M12 × 28 under-head length; washer 2.4 thick.','Threaded hole: full thread22; drillØ10.2 to25 + drill point.','Bolt end20 mm below joint; full thread reserve2 mm.','HeadØ18 ×12; socket10 A/F. Dimensions are actual mm.'],2.7);s.finish()
def housing(ex,thread=False):
 s=Sheet(ex,'Housing with section and thread' if thread else 'Housing with full section');ox,oy=90,208;s.rect(ox-60,oy-150,120,150,r=18);s.poly([(ox-50,oy-132),(ox-50,oy-140),(ox+50,oy-140),(ox+50,oy-10),(ox-50,oy-10),(ox-50,oy-132)],w=.18,style='hidden')
 for z,rs in [(45,[25,20,10]),(112,([18,16,10.5,12,8] if thread else [18,16,11,8]))]:
  cy=oy-z
  for r in rs:
   if thread and z==112 and r==12:s.arc(ox,cy,12,35,305,.18)
   else:s.circle(ox,cy,r,w=.18 if z==112 and r==18 else .5)
  s.center(ox,cy,max(rs)+5)
 s.line(ox-4,oy-70,ox-4,oy-94);s.line(ox+4,oy-70,ox+4,oy-94);s.line(ox,oy-159,ox,oy+9,.35,'cut');s.arrow(ox,oy-155,180);s.arrow(ox,oy+5,180);s.text(ox+4,oy-155,'A',3);s.text(ox+4,oy+7,'A',3)
 s.dimh(ox-60,ox+60,oy,oy,227,'120  0 / −0.05');s.dimv(oy-150,oy,ox-60,ox-60,17,'150  0 / −0.05');s.dimv(oy-112,oy-45,ox+25,ox+25,165,'67');s.dimv(oy-45,oy,ox+25,ox+25,153,'45');sx,sy=231,208
 def P(y,z):return (sx+y,sy-z)
 s.text(sx+35,42,'A–A',3.5,'center');plate=box(0,0,20,150).difference(box(-1,10,10,140));lower=box(20,20,80,70);upper=Polygon([(20,94),(50,96),(50,128),(20,130)]);mat=unary_union([plate,lower,upper]);holes=unary_union([box(9,35,50,55),box(50,25,81,65)])
 if thread:holes=unary_union([holes,box(9,104,26,120),box(26,101.5,51,122.5)])
 else:holes=unary_union([holes,box(9,104,40,120),box(40,101,51,123)])
 mat=mat.difference(holes)
 if thread:mat=mat.union(box(20,17,23,20).difference(Point(23,17).buffer(3,resolution=32)))
 for poly in ([mat] if mat.geom_type=='Polygon' else mat.geoms):
  hatch_region=poly.difference(box(32,100,51,124)) if thread else poly
  for hp in ([hatch_region] if hatch_region.geom_type=='Polygon' else hatch_region.geoms):
   if hp.geom_type=='Polygon' and not hp.is_empty:s.hatch(Polygon([P(*p) for p in hp.exterior.coords],[[P(*p) for p in ring.coords] for ring in hp.interiors]))
  s.poly([P(*p) for p in list(poly.exterior.coords)[:-1]],True)
  for ring in poly.interiors:s.poly([P(*p) for p in list(ring.coords)[:-1]],True)
 s.poly([P(20,70),P(76,70),P(45,96),P(20,94)],True)
 for z in [45,112]:s.line(sx-5,sy-z,sx+88,sy-z,.18,'center')
 if thread:
  for z in [100,124]:s.line(*P(32,z),*P(50,z),.18)
  s.line(*P(32,100),*P(32,101.5),.35);s.line(*P(32,122.5),*P(32,124),.35);s.leader(P(46,124),(337,67),(350,67),'M24–6H DEPTH18');s.leader(P(34,101.5),(337,87),(350,87),'Ø21 counterdrill24; THRUØ16');s.leader(P(20,20),(330,235),(341,235),'B');s.text(369,165,'B (2:1)',3,'center');s.sectionpoly([(360,210),(360,198)]+arcpts(366,198,6,180,270)+[(393,192),(393,177),(348,177),(348,210)]);s.poly([(348,205),(374,205),(374,177)],w=.18,style='center');s.leader((361.76,193.76),(383,166),(390,166),'R3');s.circle(*P(20,20),7,w=.18)
 else:s.leader(P(65,65),(332,77),(347,77),'Ø40 H8 DEPTH30');s.leader(P(25,120),(332,98),(347,98),'Ø16 H7 THRU');s.leader(P(45,123),(332,116),(347,116),'Ø22 DEPTH10')
 s.dimh(sx,sx+80,sy,sy-20,227,'80');s.dimh(sx,sx+20,sy,sy,239,'20');s.dimh(sx,sx+10,sy-10,sy-10,251,'10 pocket');s.leader(P(30,55),(328,157),(337,157),'Ø20 H7 THRU');s.leader((ox+4,oy-81),(170,135),(180,135),'Rib t8');s.rough(346,251,'6.3');s.leader(P(65,65),(320,176),(328,176),'');s.rough(326,176,'3.2');s.frame(174,45,['∥','0.05','A']);s.leader(P(20,145),(219,48),(213,48),'');s.line(sx,sy,sx-5,sy+5,.25);s.rect(sx-11,sy+5,6,6,w=.25);s.text(sx-8,sy+9.5,'A',3,'center');rows=[['HOLE','UPPER mm','LOWER mm'],['Ø20 H7','+0.021','0'],['Ø40 H8','+0.039','0']]+([] if thread else [['Ø16 H7','+0.018','0']]);s.table(22,30,[27,27,27],rows,height=5.5,size=2.4)
 s.notes(20,247,['Variant14: 120 ×150 ×80. Longitudinal rib left unhatched.','Proposed: plateR18; pocket100 ×130 ×10,R8; boss centres x0.','General Ra6.3; bore Ra3.2; rear datumA; front face parallel0.05/A.'],2.6);s.finish()
housing('5a');housing('6a',True)
s=Sheet('5','Working drawing of stepped shaft');sections=[('L2',65,28,28),('SH',80,7,7),('R2',85,70,70),('C2',80,95,35),('L1',75,33,33),('C1',65,27,27),('R1',60,60,60)];ox,oy=45,146;xx=ox;positions={};bounds=[ox]
for name,d,L,disp in sections:
 positions[name]=(xx,xx+disp,d,L);s.line(xx,oy-d/2,xx+disp,oy-d/2);s.line(xx,oy+d/2,xx+disp,oy+d/2)
 if name!='C2':s.dimv(oy-d/2,oy+d/2,xx+disp/2,xx+disp/2,xx+disp/2,'Ø'+str(d)+(' k6' if name in ['L1','L2'] else ' p6' if name in ['R1','R2'] else ''))
 s.text(xx+disp/2,oy+d/2+6,name,2.5,'center');s.dimh(xx,xx+disp,oy-d/2,oy-d/2,84,str(L));xx+=disp;bounds.append(xx)
for i,x in enumerate(bounds):
 dl=0 if i==0 else sections[i-1][1]/2;dr=0 if i==len(sections) else sections[i][1]/2
 if i in [0,len(sections)]:s.line(x,oy-max(dl,dr),x,oy+max(dl,dr))
 else:s.line(x,oy-max(dl,dr),x,oy-min(dl,dr));s.line(x,oy+min(dl,dr),x,oy+max(dl,dr))
s.line(ox-7,oy,xx+7,oy,.18,'center');s.dimh(ox,xx,oy+32.5,oy+30,205,'320 actual / C2 shortened by60');x0,x1,d,L=positions['C2']
for sign in [-1,1]:s.line(x0,oy+sign*(d/2-1),x1-5,oy+sign*(d/2-1),.18);s.line(x1-5,oy+sign*(d/2-1),x1,oy+sign*d/2,.18)
s.white(x0+13,oy-43,8,86)
for xb in [x0+15,x0+19]:s.poly([(xb-1,oy-42),(xb+1,oy-20),(xb-1,oy),(xb+1,oy+20),(xb-1,oy+42)],w=.25)
s.line(x0+13,oy,x0+21,oy,.18,'center')
s.leader((x0+8,oy-35),(x0+6,65),(x0+25,65),'M80 ×1.5–6g /90 long')
for name,b,Lkey,t in [('R2',22,63,9),('R1',18,50,7)]:
 xa,xb,d,L=positions[name];s.rect(xa+(L-Lkey)/2,oy-b/2,Lkey,b,w=.5,r=b/2);s.leader((xa+L/2,oy-b/2),(xa+L/2,oy-47),(xa+L/2+3,oy-47),f'{b} N9 ×{Lkey} keyway')
xa,xb,d,L=positions['L1'];gx=xb-5.35-2.65
for sign in [-1,1]:s.poly([(gx,oy+sign*37.5),(gx,oy+sign*36),(gx+2.65,oy+sign*36),(gx+2.65,oy+sign*37.5)])
s.circle(gx+1.325,oy-36.8,5,w=.18);s.leader((gx,oy-37),(243,63),(260,63),'B');s.text(365,105,'B (4:1)',3,'center');s.poly([(335,126),(351,126),(351,132),(361.6,132),(361.6,126),(393,126)]);s.dimh(351,361.6,132,132,142,'2.65 H13');s.text(335,154,'RootØ72 h11; h = 5.35',2.6)
for cx,cy,name,b,t in [(78,247,'R2',22,9),(167,247,'R1',18,7)]:
 d=positions[name][2];r=d/2;cross=Polygon(arcpts(0,0,r,0,360,180)).difference(box(-b/2,r-t,b/2,r+1));pts=[(cx+x*.6,cy-y*.6) for x,y in list(cross.exterior.coords)[:-1]];s.sectionpoly(pts);s.center(cx,cy,r*.6+4);s.text(cx,cy-r*.6-5,f'{name} SECTION (3:5)',2.6,'center');s.text(cx,cy+r*.6+6,f'b{b} N9; d−t1 = {d-t}',2.5,'center')
s.rect(228,188,6,6,w=.25);s.text(231,192.5,'A',3,'center');s.line(231,188,201.5,183.5,.25);s.frame(329,171,['↗','0.03','A']);s.leader((positions['R1'][0]+26,oy+30),(319,174),(329,174),'');s.rough(323,204,'3.2');s.table(19,30,[30,22,22],[['FEATURE','UPPER','LOWER'],['Ø65/75 k6','+0.021','+0.002'],['Ø60 p6','+0.051','+0.032'],['Ø85 p6','+0.059','+0.037'],['18 N9','0','−0.043'],['22 N9','0','−0.052']],height=5.5,size=2.4);s.notes(267,224,['BEARINGS / SELECTION','L1:6215,d75,B25; L33.','L2:6213,d65,B23; L28.','R2:keyA22×14×63; L70.','R1:keyA18×11×50; L60.','Ends2×45°. General Ra3.2.','Seats:k6 Ra0.8; p6 Ra1.6.'],2.6);s.finish()
s=Sheet('3','Housing bracket orthographic views');ox,oy=105,126
outline=[(-60,0),(-60,8),(-38,8),(-30,36),(30,36),(38,8),(60,8),(60,0),(18,0)]+arcpts(0,0,18,0,180)[1:]+[(-60,0)];s.poly(mappts(outline,ox,oy),True);lug=[(-18,36),(-18,62)]+arcpts(0,62,18,180,0)[1:]+[(18,36)];s.poly(mappts(lug,ox,oy),True);s.circle(ox,oy-62,9);s.center(ox,oy-62,23)
for x in [-48,48]:
 for dx in [-5,5]:s.line(ox+x+dx,oy,ox+x+dx,oy-8,.18,'hidden')
for x in [-10,10]:s.line(ox+x,oy-36,ox+x,oy-15,.18,'hidden')
s.line(ox,oy+6,ox,oy-87,.18,'center');s.dimh(ox-60,ox+60,oy,oy,143,'120');s.dimv(oy-80,oy,ox-18,ox-60,29,'80');s.dimv(oy-36,oy,ox+30,ox+38,177,'36');s.dimv(oy-62,oy,ox+18,ox+18,188,'62');s.leader((ox+6,oy-56),(146,49),(159,49),'2 ×Ø18 THRU');s.leader((ox+12,oy-13),(180,104),(195,104),'R18 saddle')
ox,oy=105,205;s.rect(ox-60,oy-30,120,60,r=10)
for sign in [-1,1]:
 x=ox+sign*60;s.els.append(f'<rect x="{min(x,ox+sign*40)-1}" y="{oy-10}" width="22" height="20" fill="white"/>');s.pdf.setFillColorRGB(1,1,1);s.pdf.rect((min(x,ox+sign*40)-1)*mm,(297-(oy+10))*mm,22*mm,20*mm,fill=1,stroke=0);s.poly([(x,oy-10),(ox+sign*40,oy-10),(ox+sign*40,oy+10),(x,oy+10)])
for x in [-48,48]:
 for y in [-20,20]:s.circle(ox+x,oy+y,5);s.center(ox+x,oy+y,7)
for x in [-38,38,-30,30]:s.line(ox+x,oy-30,ox+x,oy+30)
for y in [-24,16]:
 s.rect(ox-18,oy+y,36,8)
 for x in [-9,9]:s.line(ox+x,oy+y,ox+x,oy+y+8,.18,'hidden')
s.circle(ox,oy,10);s.center(ox,oy,15);s.line(ox,oy-36,ox,oy+36,.18,'center');s.dimh(ox-48,ox+48,oy+20,oy+20,249,'96');s.dimv(oy-30,oy+30,ox-60,ox-60,23,'60');s.dimv(oy-20,oy+20,ox+48,ox+48,178,'40');s.leader((ox+50,oy+23),(179,247),(193,247),'4 ×Ø10 THRU');s.leader((ox+7,oy+7),(152,224),(180,224),'Ø20 THRU');ox,oy=281,126;s.rect(ox-30,oy-8,60,8);s.rect(ox-30,oy-36,60,28)
for x in [-24,-16,16,24]:s.line(ox+x,oy-36,ox+x,oy-80)
for xa,xb in [(-24,-16),(16,24)]:
 s.line(ox+xa,oy-80,ox+xb,oy-80);s.line(ox+xa,oy-62,ox+xb,oy-62,.18,'center');s.line(ox+xa,oy-71,ox+xb,oy-71,.18,'hidden');s.line(ox+xa,oy-53,ox+xb,oy-53,.18,'hidden')
for z in [0,18]:s.line(ox-30,oy-z,ox+30,oy-z,.18,'hidden')
s.line(ox,oy+5,ox,oy-85,.18,'center');s.dimh(ox-24,ox-16,oy-80,oy-80,35,'8');s.dimh(ox-24,ox+24,oy-80,oy-80,28,'48');s.text(105,31,'FRONT',3,'center');s.text(105,168,'TOP',3,'center');s.text(281,38,'LEFT SIDE',3,'center')
s.notes(230,163,['PROPOSED NOMINAL FEATURES','Base t8; tapered body top z36.','Body half widths:38 atz8;30 atz36.','Two lugs:width36,t8,outerR18.','Lug midplanes y±20,bore axis z62.','Vertical holeØ20 at x0,y0.','Mounts:x±48,y±20.','Side notches:20 deep ×20 wide.','All holes and cut-outs through.','General Ra12.5;bores Ra3.2 proposed.'],2.7);s.rough(345,232,'12.5');s.frame(338,95,['∥','0.05','A']);s.leader((311,90),(328,98),(338,98),'');s.rect(238,130,6,6,w=.25);s.text(241,134.5,'A',3,'center');s.line(244,130,251,126,.25);s.text(230,242,'A: bottom mounting plane; top face parallel0.05/A.',2.6);s.finish()
# 1a: proposed mesh with explicit ambiguity notice.
s=Sheet('1a','Six view orthographic projection',status='PROVISIONAL RECONSTRUCTION - VERIFY AMBIGUOUS VARIANT 14 EDGES')
def clip_general(faces,n,d):
 result=[];cut=[];n=np.array(n,float)
 for face in faces:
  out=[]
  for p,q in zip(face,face[1:]+face[:1]):
   p=np.array(p,float);q=np.array(q,float);fp=p@n-d;fq=q@n-d
   if fp<=1e-8:out.append(p)
   if fp*fq<0:r=p+(q-p)*fp/(fp-fq);out.append(r);cut.append(r)
  if len(out)>=3:result.append(out)
 unique=[]
 for p in cut:
  if not any(np.linalg.norm(p-q)<1e-6 for q in unique):unique.append(p)
 if len(unique)>=3:
  center=np.mean(unique,axis=0);u=unique[0]-center;u/=np.linalg.norm(u);v=np.cross(n,u);v/=np.linalg.norm(v);unique.sort(key=lambda p:math.atan2((p-center)@v,(p-center)@u));result.append(unique)
 return result
cube=[[(0,0,0),(80,0,0),(80,80,0),(0,80,0)],[(0,0,80),(0,80,80),(80,80,80),(80,0,80)],[(0,0,0),(0,0,80),(80,0,80),(80,0,0)],[(0,80,0),(80,80,0),(80,80,80),(0,80,80)],[(0,0,0),(0,80,0),(0,80,80),(0,0,80)],[(80,0,0),(80,0,80),(80,80,80),(80,80,0)]];faces=clip_general(cube,(-1,-1,-1),-80);faces=clip_general(faces,(1,1,1),212)
def clip_poly(face,n,d):
 out=[];n=np.array(n,float)
 for p,q in zip(face,face[1:]+face[:1]):
  p=np.array(p,float);q=np.array(q,float);fp=p@n-d;fq=q@n-d
  if fp<=1e-8:out.append(p)
  if fp*fq<0:out.append(p+(q-p)*fp/(fp-fq))
 return out
outer=[]
for f in faces:
 for planes in [[((1,0,0),64)],[((-1,0,0),-64),((0,0,1),24)],[((-1,0,0),-64),((0,0,-1),-48)]]:
  ff=f
  for n,d in planes:ff=clip_poly(ff,n,d)
  if len(ff)>=3 and np.linalg.norm(np.cross(ff[1]-ff[0],ff[2]-ff[0]))>1e-8:outer.append(ff)
outer +=[[np.array(p,float) for p in f] for f in [[(64,0,24),(64,80,24),(64,80,48),(64,0,48)],[(64,0,24),(80,0,24),(80,80,24),(64,80,24)],[(64,0,48),(64,80,48),(80,80,48),(80,0,48)]]];planes={}
for f in outer:
 pts=np.array(f);n=np.cross(pts[1]-pts[0],pts[2]-pts[0]);n=n/np.linalg.norm(n)
 for z in n:
  if abs(z)>1e-6:
   if z<0:n=-n
   break
 d=n@pts[0];key=tuple(np.round(np.r_[n,d],5));planes.setdefault(key,[]).append(pts)
merged=[]
for key,fs in planes.items():
 n=np.array(key[:3]);origin=fs[0][0];u=fs[0][1]-origin;u/=np.linalg.norm(u);v=np.cross(n,u);polys=[Polygon(np.column_stack(((f-origin)@u,(f-origin)@v))) for f in fs];g=unary_union([p.buffer(0) for p in polys]);gs=[g] if g.geom_type=='Polygon' else list(g.geoms)
 for gg in gs:merged.append([origin+x*u+y*v for x,y in list(gg.exterior.coords)[:-1]])
views=[('RIGHT',((0,1,0),(0,0,1),(-1,0,0)),(29,190)),('FRONT',((1,0,0),(0,0,1),(0,-1,0)),(119,190)),('LEFT',((0,-1,0),(0,0,1),(1,0,0)),(209,190)),('REAR',((-1,0,0),(0,0,1),(0,1,0)),(299,190)),('BOTTOM',((1,0,0),(0,1,0),(0,0,-1)),(119,100)),('TOP',((1,0,0),(0,-1,0),(0,0,1)),(119,280))]
for name,proj,off in views:
 us=[np.dot(p,proj[0]) for f in merged for p in f];vs=[np.dot(p,proj[1]) for f in merged for p in f];projectmesh(s,merged,proj,(off[0]-min(us),off[1]+min(vs)));s.rect(off[0]-5,off[1]-85,90,90,w=.12);s.text(off[0]+40,off[1]-87,name,2.5,'center')
s.notes(233,47,['80 mm bounding cube; fields90×90.','First-angle layout; dashed hidden edges.','Proposed corner cut x+y+z ≥80;','rear top bevel x+y+z ≤212; side slot','x≥64, 24≤z≤48 through depth.','The source has ambiguous crossing edges.','Six views describe this defined model.','Verify reconstruction with instructor.'],2.5);s.finish()
# 6 full axial assembly. Larger two-sheet layout with BOM on separate A3 sheet later.
s=Sheet('6','Shaft bearing unit assembly');ox,oy=43,129;segs=[(0,22,50),(22,30,60),(30,91,55),(91,134,45),(134,169,40),(169,201,35)]
for a,b,d in segs:s.line(ox+a,oy-d/2,ox+b,oy-d/2);s.line(ox+a,oy+d/2,ox+b,oy+d/2)
for i,(a,b,d) in enumerate(segs):
 if i==0:s.line(ox+a,oy-d/2,ox+a,oy+d/2)
 if i==len(segs)-1:s.line(ox+b,oy-d/2,ox+b,oy+d/2)
 else:
  d2=segs[i+1][2];s.line(ox+b,oy-max(d,d2)/2,ox+b,oy-min(d,d2)/2);s.line(ox+b,oy+min(d,d2)/2,ox+b,oy+max(d,d2)/2)
s.line(ox-12,oy,ox+211,oy,.18,'center')
for xa,xb,inner in [(-12,24,45),(108,146,50)]:
 for sign in [-1,1]:s.sectionpoly([(ox+xa,oy+sign*inner),(ox+xb,oy+sign*inner),(ox+xb,oy+sign*80),(ox+xa,oy+sign*80)])
for xa,B,d,D in [(2,20,50,90),(109,25,45,100)]:
 dk=.3*(D-d);pitch=(D+d)/4;ring=.15*(D-d)
 for sign in [-1,1]:
  for rin,rout in [(d/2,d/2+ring),(D/2-ring,D/2)]:s.sectionpoly([(ox+xa,oy+sign*rin),(ox+xa+B,oy+sign*rin),(ox+xa+B,oy+sign*rout),(ox+xa,oy+sign*rout)],reverse=True)
  s.whitecircle(ox+xa+B/2,oy+sign*pitch,dk/2);s.circle(ox+xa+B/2,oy+sign*pitch,dk/2)
for sign in [-1,1]:
 s.sectionpoly([(ox+30,oy+sign*27.5),(ox+91,oy+sign*27.5),(ox+91,oy+sign*65),(ox+30,oy+sign*65)],reverse=True);s.line(ox+30,oy+sign*58,ox+91,oy+sign*58,.18)
s.white(ox+32.5,oy-31.5,56,10);s.rect(ox+32.5,oy-31.5,56,10,w=.5,r=3);s.line(ox+30,oy-27.5,ox+91,oy-27.5,.18,'hidden')
for sign in [-1,1]:s.sectionpoly([(ox+91,oy+sign*22.5),(ox+109,oy+sign*22.5),(ox+109,oy+sign*27.5),(ox+91,oy+sign*27.5)])
for sign in [-1,1]:
 left=[(-20,0),(-20,74),(-12,74),(-12,45),(2,45),(2,25),(-10,25),(-10,0)];right=[(134,22.5),(144,22.5),(144,31),(154,31),(154,74),(146,74),(146,50),(134,50)]
 for pp in [left,right]:s.sectionpoly([(ox+x,oy+sign*r) for x,r in pp],reverse=True)
 s.line(ox-12,oy+sign*45,ox-12,oy+sign*74,1);s.line(ox+146,oy+sign*50,ox+146,oy+sign*74,1);s.rect(ox+144,oy+min(sign*20,sign*31),10,11,w=.5);s.line(ox+144,oy+sign*20,ox+154,oy+sign*31,.18);s.line(ox+144,oy+sign*31,ox+154,oy+sign*20,.18)
for sign in [-1,1]:
 yy=oy+sign*62
 for headx,direction in [(ox-26,1),(ox+160,-1)]:
  start=headx+(6 if direction>0 else -6);end=start+direction*40;s.white(min(start,end),yy-5,40,10);s.rect(headx-4,yy-8,8,16);s.rect(headx+(4 if direction>0 else -6),yy-8,2,16)
  for off in [-5,5]:s.line(start,yy+off,end,yy+off);s.line(start,yy+off*.8,end,yy+off*.8,.18)
  s.line(end,yy-5,end,yy+5)
s.poly([(ox+199,oy-17.5),(ox+201,oy-15.5),(ox+201,oy+15.5),(ox+199,oy+17.5)]);s.rect(ox+173,oy-5,25,10,w=.5,r=5);s.dimh(ox-30,ox+201,oy-80,oy-17.5,37,'231 overall (rounded mm)');s.dimh(ox,ox+201,oy+25,oy+17.5,219,'201 shaft length');cx,cy=330,126
s.arc(cx,cy,74,-90,90);s.arc(cx,cy,50,-90,90);s.arc(cx,cy,62,-90,90,w=.18,style='center');s.line(cx,cy-75,cx,cy+75,.18,'center');s.line(cx-8,cy,cx+75,cy,.18,'center')
for a in [-90,-30,30,90]:
 x=cx+62*math.cos(math.radians(a));y=cy+62*math.sin(math.radians(a));s.poly([(x+8*math.cos(math.radians(t)),y+8*math.sin(math.radians(t))) for t in range(0,360,60)],True);s.center(x,y,10)
s.poly([(cx-2+1.5*math.sin(t*.5),cy+t) for t in np.linspace(-72,72,90)],w=.18);s.text(cx+25,43,'PARTIAL LEFT-SIDE VIEW',2.8,'center');s.text(cx+20,215,'6 ×M10×40 on PCD124',2.6,'center')
items=[(1,(ox-5,oy-79),(28,28)),(2,(ox+183,oy+17),(238,215)),(3,(ox+60,oy-60),(116,28)),(4,(ox-18,oy-34),(18,216)),(5,(ox+151,oy-44),(225,28)),(6,(ox+100,oy+25),(177,221)),(7,(ox-12,oy+52),(30,226)),(8,(ox+146,oy+53),(207,226)),(9,(ox+12,oy-35),(58,28)),(10,(ox+121,oy-36),(186,28)),(11,(ox+65,oy-32),(140,28)),(12,(ox+150,oy+23),(246,222)),(13,(ox+160,oy-62),(265,56)),(14,(ox+156,oy-55),(266,72))]
for num,p,end in items:s.poly([p,(end[0],end[1]+2),(end[0]+7,end[1]+2)],w=.18);s.line(end[0],end[1]+2,end[0]+7,end[1]+2,.7);s.text(end[0]+3.5,end[1],str(num),3,'center')
s.table(15,231,[10,33,9,139],[['IT','PART','QTY','MATERIAL / DRAWING'],['7','Gasket1','1','Fibre / 14.01.07'],['6','Spacer','1','C45 / 14.01.06'],['5','Cover2','1','EN-GJL-250 / 14.01.05'],['4','Cover1','1','EN-GJL-250 / 14.01.04'],['3','Gear','1','C45 / 14.01.03'],['2','Shaft','1','C45 / 14.01.02'],['1','Housing','1','EN-GJL-250 / 14.01.01']],height=4,size=2.2);s.table(217,231,[10,35,9,142],[['IT','PART','QTY','DESIGNATION'],['14','Spring washer','12','Z10.2'],['13','Hex head bolt','12','M10×40'],['12','Sealing ring','1','B40×62×10'],['11','Key A','1','16×10×56'],['10','Bearing L2','1','6309'],['9','Bearing L1','1','6210'],['8','Gasket2','1','Fibre / 14.01.08']],height=4,size=2.2);s.notes(18,271,['Gasket lines1 mm thick. 2×45° end chamfers.','Gear teeth schematic; initial-based drawing number pending.','12 bolts and12 spring washers total. Calculations attached.'],2.4);s.finish()
(OUT/'model_data.json').write_text(json.dumps({'sheets':META,'pyramid_section_xyz':sectiondata,'sphere_points':sphere_points,'shaft_ex5':sections,'assembly_ex6':segs,'provisional':['All unspecified detail dimensions proposed','Exercise1a reconstruction requires confirmation']},indent=2),encoding='utf8')
