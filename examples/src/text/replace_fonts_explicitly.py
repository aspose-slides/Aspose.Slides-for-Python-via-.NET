import aspose.slides as slides


def replace_fonts_explicitly(global_opts):
    # Load presentation
    with slides.Presentation(global_opts.data_dir + "text_fonts.pptx") as presentation:
        # Load source font to be replaced
        source_font = slides.FontData("Arial")

        # Load the replacing font
        dest_font = slides.FontData("Times New Roman")

        # Replace the fonts
        presentation.fonts_manager.replace_font(source_font, dest_font)

        # Save the presentation
        presentation.save(global_opts.out_dir + "text_updated_font_out.pptx", slides.export.SaveFormat.PPTX)
