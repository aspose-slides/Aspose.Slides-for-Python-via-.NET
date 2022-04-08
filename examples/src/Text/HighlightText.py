import aspose.slides as slides
import aspose.pydrawing as drawing


#ExStart:HighlightText
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_default_fonts.pptx") as presentation:

    textOptions = slides.TextHighlightingOptions()
    textOptions.whole_words_only = True
    
    presentation.slides[0].shapes[0].text_frame.highlight_text("title", drawing.Color.light_blue) 
    presentation.slides[0].shapes[0].text_frame.highlight_text("to", drawing.Color.violet, textOptions)

    presentation.save(outDir+ "text_highlight_text_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:HighlightText
