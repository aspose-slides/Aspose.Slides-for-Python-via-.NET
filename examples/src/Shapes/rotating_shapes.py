import aspose.slides as slides


def rotating_shapes_example(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

        # Rotate the shape to 90 degree
        shape.rotation = 90

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_rotate_out.pptx", slides.export.SaveFormat.PPTX)
