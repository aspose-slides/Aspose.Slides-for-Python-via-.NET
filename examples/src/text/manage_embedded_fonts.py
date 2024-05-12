import aspose.pydrawing as drawing
import aspose.slides as slides


def manage_embedded_fonts(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "text_embedded_fonts.pptx") as presentation:
        # render a slide that contains a text frame that uses embedded "FunSized"
        presentation.slides[0].get_image(drawing.Size(960, 720)).save(
            global_opts.out_dir + "text_embedded_fonts_1_out.png", slides.ImageFormat.PNG)

        fonts_manager = presentation.fonts_manager

        # get all embedded fonts
        embedded_fonts = fonts_manager.get_embedded_fonts()

        # find "Calibri" font
        calibri_font = [font for font in embedded_fonts if font.font_name == "Calibri"][0]

        # remove "Calibri" font
        fonts_manager.remove_embedded_font(calibri_font)

        # render the presentation removed "Calibri" font is replaced to an existing one
        presentation.slides[0].get_image(drawing.Size(960, 720)).save(
            global_opts.out_dir + "text_embedded_fonts_2_out.png", slides.ImageFormat.PNG)

        # save the presentation without embedded "Calibri" font
        presentation.save(global_opts.out_dir + "text_embedded_fonts_out.ppt", slides.export.SaveFormat.PPT)
