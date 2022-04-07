import aspose.slides as slides
import aspose.pydrawing as drawing


#ExStart:HighlightTextUsingRegx
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_default_fonts.pptx") as presentation:
    options = slides.TextHighlightingOptions()
    presentation.slides[0].shapes[0].text_frame.highlight_regex(".*", drawing.Color.blue, options) # highlighting all words with 10 symbols or longer
    presentation.save(outDir+ "text_highlight_regex_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:HighlightTextUsingRegx
