import aspose.slides as slides


def sketched_shapes(global_opts):
    """
    The example below demonstrates how to set sketchy type for a shape.
    Please pay attention that not all versions of PowerPoint can display sketched shapes.
    """
    with slides.Presentation() as pres:
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 20, 20, 300, 150)
        shape.fill_format.fill_type = slides.FillType.NO_FILL

        # Transform shape to sketch of a freehand style
        shape.line_format.sketch_format.sketch_type = slides.LineSketchType.SCRIBBLE

        pres.slides[0].get_image(4 / 3, 4 / 3).save(global_opts.out_dir + "shapes_sketch_format_out.png",
                                                        slides.ImageFormat.PNG)
        pres.save(global_opts.out_dir + "shapes_sketch_format_out.pptx", slides.export.SaveFormat.PPTX)
