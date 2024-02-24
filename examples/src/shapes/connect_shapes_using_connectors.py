import aspose.slides as slides


def connect_shapes_using_connectors(global_opts):
    # Instantiate Presentation class that represents the PPTX file
    with slides.Presentation() as pres:
        # Accessing shapes collection for selected slide
        shapes = pres.slides[0].shapes

        # Add autoshape Ellipse
        ellipse = shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 0, 100, 100, 100)

        # Add autoshape Rectangle
        rectangle = shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 300, 100, 100)

        # Adding connector shape to slide shape collection
        connector = shapes.add_connector(slides.ShapeType.BENT_CONNECTOR2, 0, 0, 10, 10)

        # Joining Shapes to connectors
        connector.start_shape_connected_to = ellipse
        connector.end_shape_connected_to = rectangle

        # Call reroute to set the automatic shortest path between shapes
        connector.reroute()

        # Saving presenation
        pres.save(global_opts.out_dir + "shapes_connect_shapes_using_connectors_out.pptx", slides.export.SaveFormat.PPTX)
