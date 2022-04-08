import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:ManageEmbeddedFonts
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a presentation file
with slides.Presentation(dataDir + "text_embedded_fonts.pptx") as presentation:
    # render a slide that contains a text frame that uses embedded "FunSized"
    presentation.slides[0].get_thumbnail(drawing.Size(960, 720)).save(outDir + "text_embedded_fonts_1_out.png", drawing.imaging.ImageFormat.png)

    fontsManager = presentation.fonts_manager

    # get all embedded fonts
    embeddedFonts = fontsManager.get_embedded_fonts()

    # find "Calibri" font
    funSizedEmbeddedFont = [font for font in embeddedFonts if font.font_name == "Calibri"][0]

    # remove "Calibri" font
    fontsManager.remove_embedded_font(funSizedEmbeddedFont)

    # render the presentation removed "Calibri" font is replaced to an existing one
    presentation.slides[0].get_thumbnail(drawing.Size(960, 720)).save(outDir + "text_embedded_fonts_2_out.png", drawing.imaging.ImageFormat.png)

    # save the presentation without embedded "Calibri" font
    presentation.save(outDir + "text_embedded_fonts_out.ppt", slides.export.SaveFormat.PPT)
#ExEnd:ManageEmbeddedFonts