import aspose.slides as slides


def add_plain_line_to_slide(global_opts):
    # Instantiate Presentation class that represents the PPTX file
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add an autoshape of type line
        slide.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)

        # Write the PPTX to Disk
        pres.save(global_opts.out_dir + "shapes_add_plain_line_out.pptx", slides.export.SaveFormat.PPTX)
