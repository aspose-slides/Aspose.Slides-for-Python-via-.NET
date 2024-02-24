import aspose.slides as slides


def geometry_shape_add_segment(global_opts):
    """This example demonstrates adding new segment to the existing geometry shape."""
    with slides.Presentation() as pres:
        # Create new shape
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 200, 100)
        # Get geometry path of the shape
        geometry_path = shape.get_geometry_paths()[0]

        # Add two lines to geometry path
        geometry_path.line_to(100, 50, 1)
        geometry_path.line_to(100, 50, 4)

        # Assign edited geometry path to the shape
        shape.set_geometry_path(geometry_path)

        # Save the presentation
        pres.save(global_opts.out_dir + "shapes_add_segment_to_geometry_path_out.pptx", slides.export.SaveFormat.PPTX)
