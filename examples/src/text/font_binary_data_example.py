import aspose.slides as slides
import aspose.pydrawing as drawing


def font_binary_data_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "Presentation.pptx") as pres:
        # Retrieve all fonts used in the presentation
        fonts = pres.fonts_manager.get_fonts()

        # Get the byte array representing the regular style of the first font in the presentation
        font_bytes = pres.fonts_manager.get_font_bytes(fonts[0], drawing.FontStyle.REGULAR)

        # Save font
        with open(global_opts.out_dir + fonts[0].font_name + ".ttf", "wb") as f:
            f.write(font_bytes)
