import aspose.slides as slides


def simple_rectangle(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 150, 50)

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_add_rectangle_out.pptx", slides.export.SaveFormat.PPTX)
