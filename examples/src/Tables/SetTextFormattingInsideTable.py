import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:SetTextFormattingInsideTable
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"
# Create an instance of Presentation class
with slides.Presentation(dataDir + "tables.pptx") as presentation:
    slide = presentation.slides[0]

    someTable = presentation.slides[0].shapes[0] # let's say that the first shape on the first slide is a table

    # setting table cells' font height
    portionFormat = slides.PortionFormat()
    portionFormat.font_height = 25
    someTable.set_text_format(portionFormat)

    # setting table cells' text alignment and right margin in one call
    paragraphFormat = slides.ParagraphFormat()
    paragraphFormat.alignment = slides.TextAlignment.RIGHT
    paragraphFormat.margin_right = 20
    someTable.set_text_format(paragraphFormat)

    # setting table cells' text vertical type
    textFrameFormat = slides.TextFrameFormat()
    textFrameFormat.text_vertical_type = slides.TextVerticalType.VERTICAL
    someTable.set_text_format(textFrameFormat)


    presentation.save(outDir + "tables_set_text_format_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetTextFormattingInsideTable

