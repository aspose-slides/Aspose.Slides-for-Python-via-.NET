import aspose.slides as slides


#ExStart:ReplaceFontsExplicitly
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load presentation
with slides.Presentation(dataDir + "text_fonts.pptx") as presentation:
    # Load source font to be replaced
    sourceFont = slides.FontData("Arial")

    # Load the replacing font
    destFont = slides.FontData("Times New Roman")

    # Replace the fonts
    presentation.fonts_manager.replace_font(sourceFont, destFont)

    # Save the presentation
    presentation.save(outDir + "text_updated_font_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ReplaceFontsExplicitly