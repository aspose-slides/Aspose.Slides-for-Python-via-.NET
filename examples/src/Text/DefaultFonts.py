import aspose.slides as slides
import aspose.pydrawing as drawing


#ExStart:DefaultFonts
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Use load options to define the default regualr and asian fonts# Use load options to define the default regualr and asian fonts
loadOptions = slides.LoadOptions(slides.LoadFormat.AUTO)
loadOptions.default_regular_font = "Wingdings"
loadOptions.default_asian_font = "Wingdings"

# Load the presentation
with slides.Presentation(dataDir + "text_default_fonts.pptx", loadOptions) as pptx:
    # Generate slide thumbnail
    pptx.slides[0].get_thumbnail(1, 1).save(outDir + "text_default_fonts_out.png", drawing.imaging.ImageFormat.png)

    # Generate PDF
    pptx.save(outDir + "text_default_fonts_out.pdf", slides.export.SaveFormat.PDF)

    # Generate XPS
    pptx.save(outDir + "text_default_fonts_out.xps", slides.export.SaveFormat.XPS)
#ExEnd:DefaultFonts