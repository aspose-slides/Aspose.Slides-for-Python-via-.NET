import aspose.slides as slides


def rendering_set_zoom(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation() as presentation:
        # Setting View Properties of Presentation

        # Zoom value in percentages for slide view
        presentation.view_properties.slide_view_properties.scale = 100
        # Zoom value in percentages for notes view
        presentation.view_properties.notes_view_properties.scale = 100

        presentation.save(global_opts.out_dir + "rendering_set_zoom_out.pptx", slides.export.SaveFormat.PPTX)
