import aspose.slides as slides
import aspose.pydrawing as drawing

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def find_and_replace_text():
    presentation_name = dataDir + "TextReplaceExample.pptx"
    out_path = outDir + "TextReplaceExample-out.pptx"
    
    with slides.Presentation(presentation_name) as pres:
        format = slides.PortionFormat()
        format.font_height = 24
        format.font_italic = slides.NullableBool.TRUE
        format.fill_format.fill_type = slides.FillType.SOLID
        format.fill_format.solid_fill_color.color = drawing.Color.red

        slides.util.SlideUtil.find_and_replace_text(pres, True, "[this block] ", "my text", format)
        pres.save(out_path, slides.export.SaveFormat.PPTX)
