import aspose.slides as slides


def geometry_shape_composite_objects(global_opts):
    """The example demonstrates creation a composite custom shape from two GeometryPath objects."""
    with slides.Presentation() as pres:
        # Create new shape
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 200, 100)

        # Create first geometry path
        geometry_path0 = slides.GeometryPath()
        geometry_path0.move_to(0, 0)
        geometry_path0.line_to(shape.width, 0)
        geometry_path0.line_to(shape.width, shape.height / 3)
        geometry_path0.line_to(0, shape.height / 3)
        geometry_path0.close_figure()

        # Create second geometry path
        geometry_path1 = slides.GeometryPath()
        geometry_path1.move_to(0, shape.height / 3 * 2)
        geometry_path1.line_to(shape.width, shape.height / 3 * 2)
        geometry_path1.line_to(shape.width, shape.height)
        geometry_path1.line_to(0, shape.height)
        geometry_path1.close_figure()

        # Set shape geometry as composition of two geometry path
        shape.set_geometry_paths([geometry_path0, geometry_path1])

        # Save the presentation
        pres.save(global_opts.out_dir + "shapes_create_geometry_path_out.pptx", slides.export.SaveFormat.PPTX)
