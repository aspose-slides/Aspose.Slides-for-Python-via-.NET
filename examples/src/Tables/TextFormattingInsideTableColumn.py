import aspose.pydrawing as drawing
import aspose.slides as slides


# ExStart:TextFormattingInsideTableColumn
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "tables.pptx") as pres:
    slide = pres.slides[0]

    someTable = pres.slides[0].shapes[0] # let's say that the first shape on the first slide is a table

    # setting first column cells' font height
    portionFormat = slides.PortionFormat()
    portionFormat.font_height = 25
    someTable.columns[0].set_text_format(portionFormat)

    # setting first column cells' text alignment and right margin in one call
    paragraphFormat = slides.ParagraphFormat()
    paragraphFormat.alignment = slides.TextAlignment.RIGHT
    paragraphFormat.margin_right = 20
    someTable.columns[0].set_text_format(paragraphFormat)

    # setting second column cells' text vertical type
    textFrameFormat = slides.TextFrameFormat()
    textFrameFormat.text_vertical_type = slides.TextVerticalType.VERTICAL
    someTable.columns[1].set_text_format(textFrameFormat)

    pres.save(outDir + "tables_text_format_inside_column_out.pptx", slides.export.SaveFormat.PPTX)

# ExEnd:TextFormattingInsideTableColumn

