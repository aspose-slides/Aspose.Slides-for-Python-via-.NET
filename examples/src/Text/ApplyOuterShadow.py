import aspose.slides as slides

#ExStart:ApplyOuterShadow
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"
# Create an instance of Presentation class
with slides.Presentation() as presentation:

    # Get reference of a slide
    slide = presentation.slides[0]

    # Add an AutoShape of Rectangle type
    ashp = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 400, 300)
    ashp.fill_format.fill_type = slides.FillType.NO_FILL

    # Add TextFrame to the Rectangle
    ashp.add_text_frame("Aspose TextBox")
    port = ashp.text_frame.paragraphs[0].portions[0]
    pf = port.portion_format
    pf.font_height = 50

    # Enable InnerShadowEffect    
    ef = pf.effect_format
    ef.enable_inner_shadow_effect()

    # Set all necessary parameters
    ef.inner_shadow_effect.blur_radius = 8.0
    ef.inner_shadow_effect.direction = 90.0
    ef.inner_shadow_effect.distance = 6.0
    ef.inner_shadow_effect.shadow_color.b = 189

    # Set ColorType as Scheme
    ef.inner_shadow_effect.shadow_color.color_type = slides.ColorType.SCHEME

    # Set Scheme Color
    ef.inner_shadow_effect.shadow_color.scheme_color = slides.SchemeColor.ACCENT1

    # Save Presentation
    presentation.save(outDir + "text_apply_inner_shadow_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ApplyOuterShadow