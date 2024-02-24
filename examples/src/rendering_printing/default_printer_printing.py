import aspose.slides as slides


def printing_default_settings(global_opts):
    # Load the presentation
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Call the print method to print whole presentation to the default printer
        presentation.print()
