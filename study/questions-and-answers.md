# Questions & answers · Variant 14

66 assessment questions paired with authored study explanations. These are not an official answer key. Original questions are attributed to the course instructions linked in each section.

## Exercise 1 — Flat component

[Original instructions](../source/instructions/Exercise_1_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_1_Variant_14.pdf)

### 1. How should component symmetry be used when dimensioning?

Draw the symmetry axis first and locate matching features relative to it. Specify a shared feature size once, with a quantity when useful, and use symmetric spacing or centre-to-centre dimensions instead of dimensioning both sides independently. Variant 14 has a vertical symmetry axis; its central square and paired side arcs should remain centred about that axis.

### 2. How should datums be selected for a component without an axis of symmetry?

Choose stable, clearly identifiable edges or surfaces as datums, then give feature positions from those references. Use a consistent baseline or coordinate system. Avoid making each feature depend on the position of the previous one, because that creates a long tolerance chain and makes the part harder to inspect.

### 3. How should holes, cut-outs and arcs be dimensioned?

Give every feature both a size and a position. Locate holes by their centres, dimension slots by their overall length and width, and define cut-outs with the dimensions needed to reproduce their boundaries. Specify arc radii and locate their centres when the remaining dimensions do not already determine them.

### 4. How should diameter, radius and sheet thickness be indicated?

Use Ø before a diameter, R before a radius, and a thickness note such as t = 4 mm for the sheet. A diameter refers to the full circle; a radius is half of it. A thickness note can avoid an extra edge view when the part has uniform thickness.

### 5. Why should dimensions not be repeated or arranged in a closed dimension chain?

Repeated dimensions can conflict if one is changed and another is missed. A closed dimension chain gives a redundant requirement and can make the tolerances inconsistent. Give the overall size and enough independent dimensions to determine the features, leaving one dependent interval undimensioned.

### 6. How does the drawing scale affect the drawing and the dimension values?

Scale changes the size of the geometry on paper, not the dimension values. At 2:1 a 20 mm feature is drawn 40 mm long but is still dimensioned 20. At 1:2 it is drawn 10 mm long and remains dimensioned 20. Print the supplied A3 PDFs at actual size to preserve their stated scale.

## Exercise 1a — Six-view orthographic projection

[Original instructions](../source/instructions/Exercise_1a_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_1a_Variant_14.pdf)

### 1. How are the six views arranged in the European (first-angle) projection method?

In first-angle projection, place the top view below the front and the bottom view above it. The right-side view goes to the left of the front; the left-side view goes to its right. In the supplied developed-cube layout, the rear view is farther to the right. Each field is 90 × 90 mm around an 80 mm bounding cube.

### 2. Which dimensions are common to particular pairs of views?

Width is shared by the front, rear, top and bottom views. Height is shared by the front, rear, left and right views. Depth is shared by the top, bottom, left and right views. Check that corresponding features transfer along projection lines without changing the relevant coordinate.

### 3. How is depth transferred to a side view?

Transfer depth from the top or bottom view to the side view using a 45° transfer line or rotation arcs. Transfer height directly from the front view. Their intersections locate the side-view points. Do not estimate the side view independently, because the three views must describe the same solid.

### 4. How is edge visibility determined for a given viewing direction?

Look along the selected viewing direction and determine which surface is encountered first. Draw visible outlines and sharp edges with thick continuous lines; use thin dashed lines for necessary hidden edges. Reassess visibility in every view: an edge visible from the front may be hidden from the rear.

### 5. How can an object edge be distinguished from a construction line?

An object edge represents a real outline or sharp change of surface and remains in the final drawing with the appropriate visible or hidden line type. A construction line only transfers a coordinate or defines a field and stays thin. A smooth tangent transition is not automatically a sharp edge. The variant 14 reconstruction still needs confirmation from a clearer source.

## Exercise 2 — Rotational component

[Original instructions](../source/instructions/Exercise_2_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_2_Variant_14.pdf)

### 1. How can the shape of a solid be reconstructed from a flat figure and an axis of rotation?

Revolve the entire area enclosed by the profile about the indicated axis. A line parallel to the axis generates a cylinder; an inclined line generates a cone; a radial step generates an annular face. A gap between the profile and the axis generates an internal cavity. For this exercise, the adopted overall length is 150 mm and maximum diameter is 110 mm.

### 2. How are a half view and a half section created, and which areas should be hatched?

An axial cutting plane passes through the rotation axis. One half shows the external view, while the other shows the section, separated by the centre line. Hatch only the material actually cut; leave holes and other voids empty. Keep the exterior and interior features consistent between both halves.

### 3. How can a through hole be distinguished from a blind hole?

A through hole connects two openings or passes completely through the relevant material. A blind hole terminates inside it, so the drawing must define its depth and end shape. In a drilled blind hole, distinguish the useful cylindrical depth from the conical drill point when that distinction matters.

### 4. How should diameters, steps, grooves and hole depths be dimensioned?

Use diameter dimensions for cylindrical features and lengths from clear axial datums for steps, grooves and depths. Define groove width and root diameter, and give radii or chamfers where present. Place internal dimensions on the section side. Do not dimension the drawn half-height as though it were a full diameter.

### 5. How should general and local surface roughness indications be interpreted?

A general roughness indication applies to surfaces unless a local indication specifies a different requirement. Local symbols must be associated with the surfaces they control. Ra describes surface texture and is normally expressed in micrometres; it is separate from a dimensional or geometrical tolerance. The proposed Ra values in this project require instructor agreement.

### 6. What does a geometrical tolerance frame specify, and what is the purpose of a datum?

A feature-control frame identifies a geometrical characteristic, its tolerance value and any required datum references. A datum supplies the reference plane, axis or other theoretically exact geometry for orientation or location. Flatness does not require a datum, whereas run-out needs a reference axis. The project's proposed run-out is 0.05 mm relative to datum A.

## Exercise 2a — Pyramid section

[Original instructions](../source/instructions/Exercise_2a_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_2a_Variant_14.pdf)

### 1. Why is the cutting plane represented by a straight line in the front view?

The plane is perpendicular to the frontal projection plane, so it is seen edge-on in the front view and projects as a line. For task 14 that line is inclined 50° to the horizontal and passes through the pyramid axis at h/2 = 45 mm, because h = 90 mm.

### 2. How is an intersection point transferred to the remaining views?

Find the point where the cutting line meets an actual edge in the front view. Transfer that point to the projection of the same spatial edge in the top and side views, preserving its coordinates. Points that coincide in one projection may separate in another; label them consistently.

### 3. Which points may be connected to form a side of the section?

Connect section points that lie on the boundary of the same face, in order around the solid. Each section side lies in one original face. Do not simply connect points in numerical order or assume that the section is quadrilateral. The proposed task 14 model produces a five-sided section.

### 4. When does the plane also intersect the base of the solid?

It also intersects the base when the cutting-plane trace crosses the base polygon. In the adopted model the plane is z = 45 + x tan 50°; setting z = 0 gives the base trace. Include intersections with base edges as well as lateral edges when forming the section boundary.

### 5. How is visibility determined after removal of the upper part?

Remove the upper part conceptually and look at the retained base-connected solid from each view direction. The new cut face may be visible and hatched, while original edges above the plane are only construction references. Determine hidden edges again after cutting; their visibility can change.

## Exercise 3 — Housing bracket

[Original instructions](../source/instructions/Exercise_3_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_3_Variant_14.pdf)

### 1. How should the number and arrangement of views be selected?

Choose the smallest set of views that defines the housing unambiguously, using first-angle placement. The assigned variant 14 requires front, top and left-side views. Select a front direction that shows the main form and leaves useful space for dimensions and the other projections.

### 2. How can the consistency of a detail in different views be checked?

Track the same feature centre, width, height and depth through the views. A hole centre in one view must align with its axis or projected boundaries in the others. Check that through holes continue through the correct material and that overall dimensions and step positions agree.

### 3. How can symmetry be used when dimensioning a housing?

Mark the applicable axes and place symmetric feature locations relative to them. Give a shared hole size with its quantity and use centre spacing where appropriate. For the proposed bracket, the mounting holes are at x = ±48 and y = ±20 mm, so their spacing is 96 × 40 mm.

### 4. When should a line at the transition between surfaces not be drawn?

Omit a fictitious sharp edge where two surfaces meet smoothly and tangentially. A fillet or rounded transition does not create the same line as an abrupt shoulder. Still draw any true visible outline of that surface from the chosen viewing direction.

### 5. How should dimensions be specified from datums without closing a dimension chain?

Select stable mounting faces or edges as datums, then use baseline or combined dimensioning for feature locations. Provide the overall sizes and only the independent dimensions needed to define each feature. Leave one dependent interval out of a chain rather than specifying every interval and the total.

### 6. How should surface roughness and tolerances be assigned to surfaces?

Associate each roughness symbol with the actual surface it controls, and connect geometrical tolerance frames to the controlled surface or feature. Identify the required datums. Choose values according to function and manufacturing needs, with instructor agreement; do not copy the example's values as though they were assigned to every variant.

## Exercise 3a — Cylinder intersection

[Original instructions](../source/instructions/Exercise_3a_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_3a_Variant_14.pdf)

### 1. Why is the sphere centre located at the intersection of the axes?

A sphere centred at the intersection of the cylinder axes has its centre on both axes. It cuts each cylinder in circles whose planes are perpendicular to that cylinder's axis. In the front view these circles project as line segments, making common points easier to construct.

### 2. How should the radius of a sphere intersecting both cylinders be selected?

The sphere radius must be at least the larger cylinder radius; equality can give tangency. It must also produce intersection-circle segments that share real points, not merely intersect each cylinder separately. For task 14 the cylinder radii are 40 and 37.5 mm, and the proposed construction uses sphere radii 41, 44 and 48 mm.

### 3. How can common points of the cylinders be determined from their intersections with a sphere?

Construct the sphere's intersection circles on both cylinders. In the front view, intersect their corresponding projected segments and retain only points lying on both segments. Transfer each common point to the other views and check that it belongs to both cylindrical surfaces.

### 4. How should points that overlap in one view be distinguished?

Give the coincident projections separate spatial point labels and use the other views to determine their different depths. Coincidence in one view does not prove that the points are the same in space. Keep the same labels as you transfer them between the front, top and side views.

### 5. How is visibility determined, and how can the case d1 = d2 be recognized?

Determine which surface is nearest the viewer for each portion of the curve. Draw visible parts continuously and hidden parts dashed. In the equal-diameter special case, the branch projections in the front view of this construction are straight-line segments; other views can remain curved. Task 14 has unequal diameters, 80 and 75 mm, so that special case does not apply.

## Exercise 4 — Threaded connection

[Original instructions](../source/instructions/Exercise_4_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_4_Variant_14.pdf)

### 1. How are external and internal threads represented?

For an external thread, draw the major diameter thick and the minor diameter thin. For an internal thread, the minor-diameter boundary is thick and the nominal major-diameter line is thin. In end views, the thin thread circle is approximately three-quarters of a circle. In a threaded engagement, the external-thread representation takes precedence.

### 2. What is the difference between detailed and simplified representation?

Detailed representation includes the prescribed thread lines, head features, chamfers and other relevant details. Simplified representation uses agreed conventional outlines with fewer details. Both must show the same connection, component order and engagement. Neither requires drawing every helical thread turn in a 2D assembly section.

### 3. Which components are not hatched in a longitudinal section?

Do not hatch bolts, screws, studs, nuts or washers when a longitudinal section passes through their axes, following the exercise convention. Hatch the joined components and distinguish adjacent parts by direction or spacing. Do not confuse an unhatched fastener with an empty hole.

### 4. How should the thread and the bottom of a blind hole be shown?

Distinguish the fastener tip, the end of full thread, thread run-out and the bottom of the drilled hole. Leave enough space for the fastener and manufacturing allowances. The proposed M12 connection has 22 mm of full thread and a cylindrical drill depth of 25 mm plus its point; the screw tip stops before the hole bottom.

### 5. How are component proportions selected for a given thread diameter?

Read the specified proportions as multiples of the thread diameter d. Here d = 12 mm. For example, a head diameter of 1.5d is 18 mm. At scale 2:1 it occupies 36 mm on the sheet, while the thread designation stays M12 and all dimension values remain actual sizes.

### 6. What are the functions of washers, a castellated nut and a split pin?

A flat washer distributes load and protects the bearing surface. A spring washer is a locking element in the course's connection convention; it should not be treated as a guarantee against loosening in every real application. A castellated nut and split pin provide a positive locking arrangement. Variant 14 uses components 3 and 11, so it does not require the castellated nut or pin.

## Exercise 4a — Axisymmetric section

[Original instructions](../source/instructions/Exercise_4a_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_4a_Variant_14.pdf)

### 1. How can surfaces and holes of the solid be identified from the profile?

Follow the whole closed contour as it revolves. Segments parallel to the axis generate cylindrical surfaces, inclined segments generate cones, and steps create faces or grooves. A profile offset from the axis creates a hole or recess. Keep the axis at the height shown in the source.

### 2. Why is the distance from the axis a radius?

A profile point travels on a circle centred on the rotation axis. Its distance to that axis is therefore the circle's radius. Double it to obtain the diameter: a maximum radius of 65 mm gives the required maximum diameter of 130 mm.

### 3. What separates the half view from the half section?

The axis of symmetry separates the half view from the half section. It remains a thin centre line, rather than a thick object edge. Show the external shape above the horizontal axis and the axial section below it, as required by the instruction.

### 4. Which areas of a section should be hatched?

Hatch only material intersected by the cutting plane. Leave cavities, holes and recesses unhatched. Use consistent hatch direction and spacing within the same part, and keep the hatching thin enough that outlines and dimensions remain clear.

### 5. Why can the left-side and right-side views differ?

Different ends can have different holes, recesses and diameter steps, and nearer surfaces can obscure farther circular edges. Determine visibility separately from each end instead of copying every concentric circle into both views. Partial-view limits reduce the displayed extent, not the real diameters.

## Exercise 5 — Stepped shaft

[Original instructions](../source/instructions/Exercise_5_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_5_Variant_14.pdf)

### 1. How are the diameters and lengths of bearing journals selected?

Use the assigned bearing bore to select the seat diameter and a compatible bearing series to obtain its width B. A seat without a retaining-ring groove must be at least B long. A grooved seat also needs the groove width and a sufficient end distance. The proposed choices are 6215 for the 75 mm L1 seat and 6213 for the 65 mm L2 seat.

### 2. How are a key and a retaining-ring groove selected?

Select key width, height and shaft keyway depth from the journal diameter, then choose an allowed key length. Make the hub seat 5–10 mm longer than the key. Select the retaining-ring root diameter, groove width and minimum end distance from the shaft-diameter table. For the 75 mm L1 seat, the proposed root diameter is 72 mm and groove width is 2.65 mm.

### 3. How is the C2 length calculated and a broken shaft dimensioned?

Subtract the lengths of all other sections from the required total: LC2 = 320 − (28 + 7 + 70 + 33 + 27 + 60) = 95 mm. The break displays C2 as only 35 mm, giving a plotted shaft length of 260 mm. Label C2 as 95 and the total as 320; the break does not shorten the real shaft.

### 4. What do k6, p6 and N9 mean?

The letters identify the position of the tolerance zone and the numbers its grade. In this exercise k6 is required on bearing seats, p6 on the keyed hub seats, and N9 on shaft keyway widths. Lowercase k and p apply to shaft dimensions; N9 here applies to the internal width of a keyway. The numerical deviations depend on the nominal size.

### 5. How are deviations converted from µm to mm?

Divide micrometres by 1000 to obtain millimetres. For example, +21 µm is +0.021 mm and −43 µm is −0.043 mm. Keep the sign and write both upper and lower deviations. The proposed 65 and 75 mm k6 seats use +0.021 / +0.002 mm.

### 6. How can the assembly sequence of components on the shaft be justified?

Check that every component can reach its seat without passing over a larger obstructing shoulder, and then check its axial stop and retention. In the proposed shaft, the 85 mm hub can enter from the left over the 65 and 80 mm sections before the left bearing is fitted. The 75 mm right bearing enters over the 60 and 65 mm end sections and stops against the 80 mm shoulder; install its retaining ring afterwards.

## Exercise 5a — Housing section

[Original instructions](../source/instructions/Exercise_5a_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_5a_Variant_14.pdf)

### 1. How does a section differ from a view, and how should A–A be marked?

A view shows the part from a direction without removing material. A section shows the part after an imagined cut, revealing the interior. Mark the cutting-plane position and viewing arrows on the related view, label the ends A, and identify the resulting section as A–A.

### 2. When should a rib remain unhatched in a section?

Leave a rib unhatched when the cutting plane runs along its length, following the conventional longitudinal-rib exception. Material of the surrounding housing or bosses remains hatched. A rib cut transversely is hatched normally. Holes and voids are never hatched as material.

### 3. How should dimensions be applied from datums without closing a dimension chain?

Choose reference planes, axes or edges, then locate features from those datums using baseline or combined dimensions. Include the overall size, wall and base thicknesses, hole sizes, depths, centre positions and other independent features. Avoid repeated values and a chain that specifies every interval plus the overall total.

### 4. How should H6, H7, and H8 deviations be read and converted from µm to mm?

For an H hole, the lower deviation is zero and the upper deviation is positive. Read the grade and the correct nominal-diameter interval before taking the value. Divide micrometres by 1000. In the adopted housing, Ø20 H7 is 20.000–20.021 mm and Ø40 H8 is 40.000–40.039 mm.

### 5. How should a geometrical tolerance and surface roughness be associated with a surface?

Connect a tolerance frame to the particular surface or feature being controlled and identify any required datum. Place a local roughness symbol on the relevant surface or its extension. A general roughness note covers remaining surfaces. Roughness, dimensional tolerance and geometrical tolerance describe different requirements and cannot replace one another.

## Exercise 6 — Shaft bearing assembly

[Original instructions](../source/instructions/Exercise_6_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_6_Variant_14.pdf)

### 1. How should the journals be selected for the bearings, key and seal?

The assigned bearing bores set L1 and L2 journal diameters: 50 mm for 6210 and 45 mm for 6309. Key width 16 mm allows a WP journal over 50 up to 58 mm; the proposal uses 55 mm, larger than L2. Select the PU seal from its shaft diameter and housing bore, and select the RW keyway from its journal diameter. The proposal uses a B40 × 62 × 10 seal and a 35 mm RW journal.

### 2. How can assembly feasibility and axial location of the parts be checked?

Check radial clearances, passage over shoulders, fits, spacer lengths and the assembly order. Confirm that the appropriate ring or hub meets its axial stop and that covers and retention locate the parts without unintended interference. The proposed L2 seat contains an 18 mm spacer plus the 25 mm bearing, giving 43 mm; the complete shaft is 201 mm long.

### 3. How should adjacent parts and bearing rings be hatched?

Distinguish adjacent components by reversing the hatch direction or changing the spacing. Treat the bearing inner and outer rings as separate components. Do not hatch rolling elements or a shaft cut longitudinally under the assembly convention. Make material boundaries readable without adding imaginary edges.

### 4. How should a threaded connection and a gasket be represented?

Represent the cover fasteners with the detailed thread convention, preserving the component order and engagement. Include six M10 × 40 bolts and six spring washers on each cover. Draw the gasket between the cover and housing as the specified 1 mm thick section line; this is a drawing convention for the task, not a blanket requirement that every real gasket be 1 mm thick.

### 5. How should the parts list and item callouts be prepared?

Give every component a consistent item number and use that same number in the parts list. The exercise places the list above the title block, with numbers increasing upwards; split it into adjacent blocks if necessary. Give quantities, non-standard-part materials and drawing numbers, and standard-part designations without materials. The bolt and washer quantities are 12 each.

### 6. What information should an assembly drawing contain?

Show how the parts fit and function together, using the necessary sectional and partial views, overall and interface dimensions, item callouts and a complete parts list. Include the assembly identification and title block. The source uses surname and first-name initials in drawing numbers; this project keeps a provisional 14 prefix until those details are confirmed. The gear teeth in the viewer are illustrative.

## Exercise 6a — Housing section and thread

[Original instructions](../source/instructions/Exercise_6a_English.docx) · [Drawing PDF](../drawings/number-14/pdf/Exercise_6a_Variant_14.pdf)

### 1. How is an internal thread represented in section and in end view?

In axial section, show the internal minor-diameter boundary thick and the nominal major-diameter line thin. Hatch material up to the nominal thread line, while keeping the hole empty. In the end view, use a full thick minor-diameter circle and a thin nominal-diameter circle over about three-quarters of the circumference.

### 2. What is the difference between the thread diameter and the tap-drill diameter?

The nominal diameter is the size used in the thread designation; the tap-drill diameter is the smaller hole prepared before tapping. They are not interchangeable dimensions. For the proposed coarse M24 thread, the nominal diameter is 24 mm and the selected counterdrill is 21 mm, following the supplied table.

### 3. How is thread depth specified in a blind hole?

Give the required usable thread depth separately from the drilling or counterdrilling depth. Allow for run-out and the hole-end geometry where applicable. In the proposed stepped housing bore, the full M24 thread is 18 mm deep and the Ø21 counterdrill is 24 mm deep from the same opening, with a smaller through passage beyond it.

### 4. When should a detail, broken-out section, or partial view be used?

Use an enlarged detail when a small feature cannot be read clearly at the main scale; identify the same area on the main view. A broken-out section exposes a local interior, while a partial view limits the drawn extent. The proposal shows root fillet R3 in detail B at 2:1; the dimension remains R3 rather than becoming R6.

### 5. How should tolerancing of a plain hole be separated from thread specification?

Specify a plain bore with its diameter and hole tolerance, such as Ø20 H7. Specify a threaded feature with its M designation and the relevant thread tolerance class, such as M24–6H. Do not put H7 or H8 on a thread as though it were a plain hole. Keep the plain-hole deviation table separate from the thread designation.
