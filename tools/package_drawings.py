from pathlib import Path
import math,json,zipfile,textwrap,re
import numpy as np
import fitz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'drawings'/'number-14';data=json.loads((OUT/'model_data.json').read_text());from drawing_fonts import register_drawing_font
register_drawing_font()
c=canvas.Canvas(str(OUT/'Variant_14_Calculations_and_Assumptions.pdf'),pagesize=(210*mm,297*mm));c.setTitle('Variant 14 calculations and proposed dimensions');page_no=0

def page(title,paragraphs):
 global page_no
 page_no+=1;c.setFont('Arial',15);c.drawString(17*mm,279*mm,title);y=266
 for para in paragraphs:
  para=re.sub(r'\b(Exercise|exercise|task|variant|width|height|depth|length|thickness|diameter|diameters|bearing|bearings|counterbore|counterdrill|radius|radii|square|Square|seat|Seat|key|Key|keyway|Keyway|inspection|dimension|journal|Journal|face|surface|general|General|point|points|pairs|fibre|drawing|root|groove|material|type|scale|through|at|to|from|over|within|is|and|the|by|of|as|with|than|before|after|using|lengths)(?=\d)',r'\1 ',para)
  para=para.replace('SchemeII','Scheme II').replace('Scheme2','Scheme 2');para=re.sub(r'Ra(?=\d)','Ra ',para)
  if not para:y-=3;continue
  words=para.split();lines=[];line=''
  for word in words:
   test=(line+' '+word).strip()
   if pdfmetrics.stringWidth(test,'Arial',9)>176*mm:lines.append(line);line=word
   else:line=test
  if line:lines.append(line)
  c.setFont('Arial',9)
  for line in lines:c.drawString(17*mm,y*mm,line);y-=4.7
  y-=1.5
 if y<24:raise RuntimeError(f'Notes page {page_no} overflow {y}')
 c.setFont('Arial',8);c.drawString(17*mm,14*mm,'Student 14 / Proposed details for instructor review / 17 November 2026');c.drawRightString(193*mm,14*mm,str(page_no));c.showPage()
page('Variant 14 drawing set',[
'Twelve A3 drawing sheets are supplied as individual PDFs and editable SVGs. The combined PDF follows exercise order 1, 1a, 2, 2a, 3, 3a, 4, 4a, 5, 5a, 6, 6a.',
'Print the A3 PDFs at actual size / 100 percent. Exercise 4 uses 2:1. Other main drawings use 1:1. Exercise 5 cross-sections use 3:5 and detail B uses 4:1; Exercise 6a detail B uses 2:1. Dimension values always describe actual millimetres.',
'',
'Status: proposed drawings for review',
'The supplied instructions leave many feature sizes, roughness values and geometrical tolerances for agreement with the instructor. Those unassigned values have been selected here as proposals. They are not claimed to be instructor-approved data.',
'Exercise 1a is provisional: its pictorial source has ambiguous crossing edges. The six projections are consistent with an explicitly defined proposed solid, but that solid still needs to be checked against a clearer original or instructor explanation.',
'Full student name and initials were not supplied. Title blocks use Student 14. Replace the provisional drawing-number prefix with surname and first-name initials where required by the assembly assignment.',
'',
'Assigned data transcribed from Section 6',
'1: variant14, sheet thickness4, bounding rectangle160 ×120.',
'1a: variant14, bounding cube80, six projection fields90 ×90, first-angle arrangement.',
'2: profile14, length150, maximum diameter110.',
'2a: task14, SchemeII, a110, h90, cutting angle50° through the axis at h/2.',
'3: variant14, width120, height80, depth60. All holes and cut-outs through.',
'3a: task14, cylinder diameters80 and75, included axis angle70°.',
'4: variant14, diagramF, components3 and11, M12 thread, scale2:1.',
'4a: profile14, length150, maximum diameter130.',
'5: variant14, Scheme2, length320, L1 diameter75 with RO, L2 diameter65, CG thread on C2.',
'5a and6a: variant14, overall width120, height150, depth80.',
'6: variant14, bearings6210 and6309, parallel key typeA16 ×10 ×56.',
'',
'Sources: the twelve supplied English exercise instructions. Original files were not modified. Exercise 3a media and text were recovered from the damaged DOCX archive for inspection.'
])
page('Exercise 5 shaft calculations',[
'Scheme2, left to right: L2 – shoulder – R2 – C2 – L1 – C1 – R1.',
'L2: diameter65 k6, length28. Shoulder: diameter80, length7. R2: diameter85 p6, length70. C2: M80 ×1.5–6g, length95. L1: diameter75 k6, length33. C1: diameter65, length27. R1: diameter60 p6, length60.',
'Length balance: 28 +7 +70 +95 +33 +27 +60 =320 mm. C2 is displayed as35 mm, so the plotted shaft length is260 mm. The dimension95 at C2 and the overall320 are actual dimensions.',
'L1 bearing: 6215, bore75, outside diameter130, width25. Groove values from the supplied table: root diameter72, width2.65, minimum end distance4.5. Adopted journal33 gives h =33 −25 −2.65 =5.35 mm, meeting the minimum.',
'L2 bearing: 6213, bore65, outside diameter120, width23. Its28 mm seat exceeds the bearing width.',
'R2 at diameter85 uses key A22 ×14 ×63. The assigned key table includes diameter85 in the range over75 up to85. Shaft keyway depth9; inspection dimension85 −9 =76. Seat70 =key63 +7, centred with3.5 mm at each end.',
'R1 at diameter60 uses key A18 ×11 ×50. Shaft keyway depth7; inspection dimension60 −7 =53. Seat60 =key50 +10, centred with5 mm at each end.',
'C2: proposed M80 ×1.5 external fine thread, full-thread length90 within the95 mm journal. Allow5 mm for run-out before the L1 shoulder. Agree the selected thread with the instructor.',
'Assembly sequence: R2 hub can enter from the left over diameters65 and80 before fitting the left bearing. L1 bearing enters from the right over diameters60 and65 and seats against the diameter80 shoulder. A retaining ring sits at the free end of the75 mm journal.',
'Adjacent journal diameter differences are15,5,5,5,10 and5 mm, within the required5–20 mm range. End chamfers2 ×45°. Bearing seatsRa0.8, keyed seatsRa1.6, generalRa3.2 proposed.',
'',
'Numerical deviations in millimetres',
'Diameters65 and75 k6: upper +0.021, lower +0.002. Diameter60 p6: upper +0.051, lower +0.032. Diameter85 p6: upper +0.059, lower +0.037.',
'Keyway18 N9: upper0, lower−0.043. Keyway22 N9: upper0, lower−0.052. The0.03 circular run-out relative to the L1 datum axis is proposed.',
'Bearing and groove dimensions come from the supplied Exercise5 tables. External tolerance references are listed on the final notes page.'
])
page('Exercise 6 assembly calculations',[
'Assigned bearing L1:6210, d50, D90, B20. Assigned bearing L2:6309, d45, D100, B25. Use these dimensions for the bearing ring envelopes.',
'WP key A16 ×10 ×56 requires a journal diameter over50 to58. Select55, greater than the45 mm L2 bearing seat. WP length61 =key56 +5.',
'Shaft sections, left to right: L1 diameter50 ×22; shoulder diameter60 ×8; WP diameter55 ×61; L2 diameter45 ×43; PU diameter40 ×35; RW diameter35 ×32. Total22 +8 +61 +43 +35 +32 =201 mm.',
'Axial coordinates are measured from the shaft left end. L1 bearing lies at2…22. Shoulder22…30. Gear30…91. Spacer91…109. L2 bearing109…134. Seal journal134…169. End journal169…201.',
'The43 mm L2 seat contains an18 mm spacer and a25 mm bearing. The proposed B40 ×62 ×10 sealing ring lies at144…154, in the right cover. PU40 <L2 diameter45 and RW35 <PU40.',
'RW diameter35: keyway10 wide,25 long, depth5; inspection dimension30. Its32 mm journal allows25 +5 +2 mm for the keyway, edge allowance and chamfer.',
'Each cover carries six M10 ×40 hex-head bolts with six spring washers. Twelve of each are listed. The proposed pitch circle is124 and cover outside diameter148. Gasket section lines are1 mm thick.',
'The plotted overall axial dimension is231 mm after rounding to a whole millimetre. End chamfers are2 ×45°. Gear teeth are schematic because tooth count and module are not assigned.',
'',
'Complete parts list',
'1 Housing, quantity1, EN-GJL-250, drawing14.01.01. 2 Shaft, quantity1, C45, drawing14.01.02. 3 Gear, quantity1, C45, drawing14.01.03.',
'4 Bearing cover1, quantity1, EN-GJL-250, drawing14.01.04. 5 Bearing cover2, quantity1, EN-GJL-250, drawing14.01.05. 6 Spacer, quantity1, C45, drawing14.01.06.',
'7 Gasket1 and8 Gasket2, one each, gasket fibre, drawings14.01.07 and14.01.08.',
'9 Bearing6210, quantity1. 10 Bearing6309, quantity1. 11 Parallel key A16 ×10 ×56, quantity1. 12 Seal B40 ×62 ×10, quantity1. 13 Bolt M10 ×40, quantity12. 14 Spring washer Z10.2, quantity12.',
'Standard parts have no material designation. Item numbers in each parts-list block increase upwards. Prefix14 is provisional; use the required student initials for the final assembly number and non-standard-part drawing numbers.',
'Final instructor review should confirm bearing retention, fits, clearance around the gear, and any additional gear geometry required by the course.'
])
profile=[(0,32),(44,43),(44,55),(68,55),(68,51),(76,51),(76,55),(135,55),(150,49),(150,27),(125,27),(58,20),(58,0),(46,0),(20,20),(0,20)]
page('Proposed feature geometry',[
'Exercise1: coordinate origin at the square centre, vertical symmetry axis x0. Overall x±80; upper flat y60 over x±40; shoulders x±80,y49. Concave side arcs radius40 centred at (±92,0). Lower shoulders x±80,y−49; tips x±40,y−60; lower notch x±40,y−52. Square diagonal88, rotated45°. Thickness4.',
'Exercises2 and4a: use the following closed profile in (axial x, radius r), in order: '+', '.join(f'({x},{r})' for x,r in profile)+'. Close the contour to the first vertex.',
'Exercise2 uses these radii directly. Exercise4a multiplies every radius by130/110; axial coordinates stay unchanged. Maximum diameters are therefore110 and130, with length150 in each case. The left cavity reachesx46; the right cavity ends atx58. The12 mm interval46…58 is solid on the axis.',
'Exercise3: x across width120, y across depth60, z up to80. Base thickness8. Tapered body half-width38 atz8 and30 atz36. Underside saddle radius18, through depth. Four mounting holes diameter10 atx±48,y±20. Both side notches extend20 in fromx±60 and have20 mm width across y.',
'Exercise3 lugs: x±18, midplanes y±20, thickness8; bore axis z62; outer top radius18 and hole diameter18. A central diameter20 vertical hole intersects the saddle. All holes and cut-outs through.',
'Exercises5a and6a: plate120 ×150 ×20 with outer cornerR18. Rear pocket100 ×130 ×10, cornerR8, centred. Bosses share x0 and their z coordinates are45 and112, giving67 between centres.',
'Lower boss: outside diameter50, projects from depth20 to80. Through bore20 H7, with diameter40 H8 counterbore30 deep from the front. Upper boss: outside diameter36 atdepth20, tapering to32 atdepth50.',
'Exercise5a upper bore: diameter16 H7 through, with diameter22 counterbore10 deep. Exercise6a upper bore: diameter16 through, diameter21 counterdrill24 deep from the front, and M24–6H thread18 deep. The drilling allowance extends6 mm beyond the full thread.',
'Both housings have an8 mm longitudinal rib between bosses; it remains unhatched in axial section. Exercise6a adds the actual root filletR3 shown in detailB at2:1. GeneralRa6.3, local boreRa3.2 and face parallelism0.05/A are proposed.',
'Exercise4: upper plate20 thick, lower member32 thick. Counterbore diameter22, depth14.4. Head diameter18 ×12, with socket10 A/F; spring washer thickness2.4. Under-head bolt length28 reaches20 mm below the joint. Full M12 thread22 deep, drill diameter10.2 to25 plus a3 mm conical point;4 mm of material remains below the point.'
])
page('Geometric checks and references',[
'Exercise2a: SchemeII reconstruction uses base A(−55,−8,0), B(−32,42,0), C(55,25,0), D(15,−52,0) and apex(0,0,90). The horizontal base span is110. These additional base coordinates are proposed from the scheme proportions.',
'Cut plane: z =45 + x tan50°. Retain points satisfying z ≤45 + x tan50°. The section has'+str(len(data['pyramid_section_xyz']))+' vertices, including intersections with the base. Every computed section point is checked against the plane equation. Full coordinates are retained in model_data.json.',
'Exercise3a: the main cylinder satisfies y² +z² =40². The inclined cylinder satisfies y² +(x sin70° −z cos70°)² =37.5². The curve is calculated from both equations and plotted in three orthographic views.',
'Three common-centre auxiliary spheres use radii41,44 and48. Circle-pair intersections give the labelled pairs5/6,7/8 and9/10. Points1–4 are characteristic outline and depth-extreme points. Numerical residuals are checked against both cylinders and each sphere.',
'Exercise1a proposed solid: begin with the80 mm cube; retain x+y+z ≥80 and x+y+z ≤212, then remove x≥64 with24≤z≤48 through the depth. All six views are projected from that one model with sampled edge visibility. This reconstruction remains an open verification item.',
'',
'References for numerical tolerance values',
'Sheng Fong Precision manufacturer charts: k6 and p6 shaft tolerances, sizes50–80 and80–120. Values were converted directly in millimetres.',
'https://sfp.tw/en/tol/shaft/k6.html',
'https://sfp.tw/en/tol/shaft/p6.html',
'Rollco Standard tolerances keyways, P0000-2ENTI, October2022: the18 N9 width uses upper0 and lower−0.043.',
'Industrial Press, Machinery’s Handbook31st edition errata, September2021, corrected keyway table:22 N9 uses upper0 and lower−0.052.',
'Links to the two PDF references are provided in README.md. Bearing dimensions, hole-H tolerances, key sizes, retaining-ring grooves and tap-drill data otherwise come from the supplied course instructions.',
'',
'Checks before final submission',
'Confirm the Exercise1a solid from a clearer source; agree the unassigned dimensions and proposed annotations; add the student full name and required initials. The set is a review draft and does not represent instructor approval.',
'For editing, open SVG files in a vector or drawing editor and preserve the420 ×297 mm page size. SVG is an editable vector format, not a parametric3D model. Any exported PDF must retain its original scale.'
])
c.save()
# Numeric verification of geometric models.
checks=[]
def check(name,ok,detail=''):
 checks.append({'check':name,'passed':bool(ok),'detail':detail})
 if not ok:raise AssertionError(name+': '+detail)
check('Twelve exercise sheets',len(data['sheets'])==12)
check('Shaft actual total320',sum(s[2] for s in data['shaft_ex5'])==320)
check('Shaft displayed total260',sum(s[3] for s in data['shaft_ex5'])==260)
check('Assembly shaft total201',data['assembly_ex6'][-1][1]==201)
check('L1 groove end allowance',33-25-2.65>=4.5)
maxres=0
for p in data['pyramid_section_xyz']:maxres=max(maxres,abs(p[2]-45-math.tan(math.radians(50))*p[0]))
check('Pyramid section residual',maxres<1e-8,str(maxres))
maxres=0
for R,p in data['sphere_points']:
 x,y,z=p;maxres=max(maxres,abs(y*y+z*z-1600),abs(y*y+(x*math.sin(math.radians(70))-z*math.cos(math.radians(70)))**2-37.5**2),abs(x*x+y*y+z*z-R*R))
check('Sphere points satisfy both cylinders and sphere',maxres<1e-8,str(maxres))
order=['1','1a','2','2a','3','3a','4','4a','5','5a','6','6a'];combo=fitz.open()
for ex in order:
 f=OUT/'pdf'/f'Exercise_{ex}_Variant_14.pdf';d=fitz.open(f);page0=d[0];check('A3 page '+ex,abs(page0.rect.width-420*mm)<.1 and abs(page0.rect.height-297*mm)<.1)
 txt=page0.get_text();check('Variant title '+ex,'VARIANT 14' in txt)
 # No replacement squares or unsupported glyphs in final text.
 check('No missing-glyph box '+ex,'\u25a0' not in txt and '\ufffd' not in txt)
 page0.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(OUT/'qa'/f'Exercise_{ex}_Variant_14.png');combo.insert_pdf(d);d.close()
combo.save(OUT/'Variant_14_All_12_Drawings.pdf');combo.close()
d=fitz.open(OUT/'Variant_14_Calculations_and_Assumptions.pdf')
for i,p in enumerate(d):p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(OUT/'qa'/f'Notes_{i+1}.png')
check('Notes page count',len(d)==5)
(OUT/'validation.json').write_text(json.dumps({'checks':checks,'open_items':['Exercise1a reconstruction unverified','Instructor approval of proposed dimensions and annotations pending','Student name and initials pending'],'visual_review':'See QA page renders; final visual review performed separately'},indent=2),encoding='utf8')
readme='''# Variant 14 technical drawing review set

Contains twelve A3 drawing sheets, individual PDFs, editable SVGs, a combined PDF, and five pages of calculations and proposed dimensions.

**Review draft.** Exercise 1a uses a provisional reconstruction of an ambiguous source. Other detail dimensions, roughness and geometrical tolerance values left unspecified by the instructions are proposals for instructor agreement. Add your full name and required initials before submission.

Print at 100% / actual size on A3. Exercise 4 is drawn 2:1; other main views are 1:1. Local detail scales are labelled. Dimensions always indicate actual millimetres.

Open SVGs in a vector/drawing editor. Keep the 420 by 297 mm page size. These are editable 2D vectors, not parametric CAD solids.

The source Word/PDF instructions were not modified. Numeric geometry and checks are in model_data.json and validation.json. Generation scripts are supplied in ../../tools for reproducibility; dependencies are Python 3, reportlab, numpy, shapely and PyMuPDF. Set DRAWING_FONT to a Unicode TrueType font if needed.

## External references

- [Sheng Fong Precision k6](https://sfp.tw/en/tol/shaft/k6.html)
- [Sheng Fong Precision p6](https://sfp.tw/en/tol/shaft/p6.html)
- [Rollco normal keyway tolerances](https://www.rollco.eu/storage/ECE2BCAD53C0FA33F7C1A1F6D37A80AA8791664C0C449D9C5565041FF94166CB/ab6f42aee7664d3c911ace67fb7b19f5/pdf/media/620675c68cce473cadb1b93935cab105/Standard_tolerances_keyways_P0000-2ENTI.pdf)
- [Industrial Press Machinery's Handbook31 errata](https://dhjhkxawhe8q4.cloudfront.net/industrialpress-wp/wp-content/uploads/2021/10/05102216/MH31-Errata-9-2021-web.pdf)

Course instruction tables supply the assigned sizes and other selection data. Read the calculations PDF for the adopted geometry and open review items.
'''
(OUT/'README.md').write_text(readme,encoding='utf8')
print('Generated combined PDF, notes and validation:',len(checks),'checks; all passed.')
