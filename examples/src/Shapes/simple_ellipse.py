import aspose.slides as slides


def simple_ellipse(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of ellipse type
        slide.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 50, 150, 150, 50)

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_add_ellipse_out.pptx", slides.export.SaveFormat.PPTX)
