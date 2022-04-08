import aspose.slides as slides


#ExStart:AddEmbeddedFonts
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load presentation
with slides.Presentation(dataDir + "text_fonts.pptx") as presentation:

    # Load source font to be replaced
    sourceFont = slides.FontData("Arial")


    allFonts = presentation.fonts_manager.get_fonts()
    embeddedFonts = presentation.fonts_manager.get_embedded_fonts()
    for font in allFonts:
        if font not in embeddedFonts:
            presentation.fonts_manager.add_embedded_font(font, slides.export.EmbedFontCharacters.ALL)

    # Save the presentation
    presentation.save(outDir + "text_add_embedded_font_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddEmbeddedFonts