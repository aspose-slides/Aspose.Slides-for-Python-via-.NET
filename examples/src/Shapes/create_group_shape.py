import aspose.slides as slides


def create_group_shape(global_opts):
    # Instantiate Presentation class
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Accessing the shape collection of slides
        shapes = slide.shapes

        # Adding a group shape to the slide
        group_shape = shapes.add_group_shape()

        # Adding shapes inside added group shape
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 100, 100, 100)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 500, 100, 100, 100)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 300, 100, 100)
        group_shape.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 500, 300, 100, 100)

        # Adding group shape frame
        group_shape.frame = slides.ShapeFrame(100, 300, 500, 40, slides.NullableBool.TRUE,
                                              slides.NullableBool.TRUE, 0)

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_create_group_shape_out.pptx", slides.export.SaveFormat.PPTX)
