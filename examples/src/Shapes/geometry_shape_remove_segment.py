import aspose.slides as slides


def geometry_shape_remove_segment(global_opts):
    """This example demonstrates removing a segment from the existing geometry shape."""
    with slides.Presentation() as pres:
        # Create new shape
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.HEART, 100, 100, 300, 300)

        # Get geometry path of the shape
        path = shape.get_geometry_paths()[0]

        # remove segment
        path.remove_at(2)

        # set new geometry path
        shape.set_geometry_path(path)

        # Save the presentation
        pres.save(global_opts.out_dir + "shapes_geometry_path_remove_at_out.pptx", slides.export.SaveFormat.PPTX)
