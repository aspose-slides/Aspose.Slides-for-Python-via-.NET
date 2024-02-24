import aspose.slides as slides


def add_embedded_fonts(global_opts):
    # Load presentation
    with slides.Presentation(global_opts.data_dir + "text_fonts.pptx") as presentation:
        # Load source font to be replaced
        source_font = slides.FontData("Arial")

        all_fonts = presentation.fonts_manager.get_fonts()
        embedded_fonts = presentation.fonts_manager.get_embedded_fonts()
        for font in all_fonts:
            if font not in embedded_fonts:
                presentation.fonts_manager.add_embedded_font(font, slides.export.EmbedFontCharacters.ALL)

        # Save the presentation
        presentation.save(global_opts.out_dir + "text_add_embedded_font_out.pptx", slides.export.SaveFormat.PPTX)
