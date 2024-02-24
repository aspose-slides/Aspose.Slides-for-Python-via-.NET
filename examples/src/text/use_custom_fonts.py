import aspose.slides as slides


def use_custom_fonts(global_opts):
    # folders to seek fonts
    folders = [global_opts.data_dir]

    # Load the custom font directory fonts
    slides.FontsLoader.load_external_fonts(folders)

    # Do Some work and perform presentation/slides rendering
    with slides.Presentation(global_opts.data_dir + "text_default_fonts.pptx") as presentation:
        presentation.save(global_opts.out_dir + "text_load_external_fonts_out.pptx", slides.export.SaveFormat.PPTX)

    # Clear Font Cache
    slides.FontsLoader.clear_cache()
