import aspose.slides as slides


def fill_shapes_gradient(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of ellipse type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 50, 150, 75, 150)

        # Apply some gradiant formatting to ellipse shape
        shape.fill_format.fill_type = slides.FillType.GRADIENT
        shape.fill_format.gradient_format.gradient_shape = slides.GradientShape.LINEAR

        # Set the Gradient Direction
        shape.fill_format.gradient_format.gradient_direction = slides.GradientDirection.FROM_CORNER2

        # Add two Gradiant Stops
        shape.fill_format.gradient_format.gradient_stops.add(1.0, slides.PresetColor.PURPLE)
        shape.fill_format.gradient_format.gradient_stops.add(0, slides.PresetColor.RED)

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_fill_gradient_out.pptx", slides.export.SaveFormat.PPTX)
