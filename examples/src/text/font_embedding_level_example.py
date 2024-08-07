import aspose.slides as slides
import aspose.pydrawing as drawing


def font_embedding_level_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "Presentation.pptx") as pres:
        # Retrieve all fonts used in the presentation
        fonts = pres.fonts_manager.get_fonts()

        # Get the byte array representing the regular style of the first font in the presentation
        font_bytes = pres.fonts_manager.get_font_bytes(fonts[0], drawing.FontStyle.REGULAR)

        # Determine the embedding level of the font
        embedding_level = pres.fonts_manager.get_font_embedding_level(font_bytes, fonts[0].font_name)

        # Print embedding level to console
        print("Font", fonts[0].font_name, "has", embedding_level, "embedding level")
