import aspose.slides as slides


def shadow_effects(global_opts):
    # Instantiate a PPTX class
    with slides.Presentation() as pres:
        # Get reference of the slide
        slide = pres.slides[0]

        # Add an AutoShape of Rectangle type
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 150, 50)

        # Add TextFrame to the Rectangle
        auto_shape.add_text_frame("Aspose TextBox")

        # Disable shape fill in case we want to get shadow of text
        auto_shape.fill_format.fill_type = slides.FillType.NO_FILL

        # Add outer shadow and set all necessary parameters
        auto_shape.effect_format.enable_outer_shadow_effect()
        shadow = auto_shape.effect_format.outer_shadow_effect
        shadow.blur_radius = 4.0
        shadow.direction = 45
        shadow.distance = 3
        shadow.rectangle_align = slides.RectangleAlignment.TOP_LEFT
        shadow.shadow_color.preset_color = slides.PresetColor.BLACK

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "text_ShadowEffects_out.pptx", slides.export.SaveFormat.PPTX)
