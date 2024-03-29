﻿import aspose.slides as slides


def connect_shape_using_connection_site(global_opts):
    # Instantiate Presentation class that represents the PPTX file
    with slides.Presentation() as presentation:
        # Accessing shapes collection for selected slide
        shapes = presentation.slides[0].shapes

        # Adding connector shape to slide shape collection
        connector = shapes.add_connector(slides.ShapeType.BENT_CONNECTOR3, 0, 0, 10, 10)

        # Add autoshape Ellipse
        ellipse = shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 0, 100, 100, 100)

        # Add autoshape Rectangle
        rectangle = shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 200, 100, 100)

        # Joining shapes to connectors
        connector.start_shape_connected_to = ellipse
        connector.end_shape_connected_to = rectangle

        # Setting the desired connection site index of Ellipse shape for connector to get connected
        wanted_index = 6

        # Checking if desired index is less than maximum site index count
        if ellipse.connection_site_count > wanted_index:
            # Setting the desired connection site for connector on Ellipse
            connector.start_shape_connection_site_index = wanted_index

        # save presentation
        presentation.save(global_opts.out_dir + "shapes_connect_shape_using_connection_site_out.pptx",
                          slides.export.SaveFormat.PPTX)
