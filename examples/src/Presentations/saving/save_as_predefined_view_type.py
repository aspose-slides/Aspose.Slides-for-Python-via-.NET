import aspose.slides as slides


def save_as_predefined_view_type(global_opts):
    # Opening the presentation file
    with slides.Presentation() as presentation:
        # Setting view type 
        presentation.view_properties.last_view = slides.ViewType.SLIDE_MASTER_VIEW

        # Saving presentation
        presentation.save(global_opts.out_dir + "save_as_predefined_view_type_out.pptx", slides.export.SaveFormat.PPTX)
