import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:EndParaGraphProperties
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 10, 10, 200, 250)

    para1 = slides.Paragraph()
    para1.portions.add(slides.Portion("Sample text"))

    para2 = slides.Paragraph()
    para2.portions.add(slides.Portion("Sample text 2"))
    endParagraphPortionFormat = slides.PortionFormat()
    endParagraphPortionFormat.font_height = 48
    endParagraphPortionFormat.latin_font = slides.FontData("Times New Roman")
    para2.end_paragraph_portion_format = endParagraphPortionFormat

    shape.text_frame.paragraphs.add(para1)
    shape.text_frame.paragraphs.add(para2)

    pres.save(outDir + "text_set_end_paragraph_portion_format_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:EndParaGraphProperties
