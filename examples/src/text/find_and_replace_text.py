import aspose.slides as slides
import aspose.pydrawing as drawing


def find_and_replace_text(global_opts):
    with slides.Presentation(global_opts.data_dir + "TextReplaceExample.pptx") as pres:
        portion_format = slides.PortionFormat()
        portion_format.font_height = 24
        portion_format.font_italic = slides.NullableBool.TRUE
        portion_format.fill_format.fill_type = slides.FillType.SOLID
        portion_format.fill_format.solid_fill_color.color = drawing.Color.red

        slides.util.SlideUtil.find_and_replace_text(pres, True, "[this block] ", "my text", portion_format)
        pres.save(global_opts.out_dir + "TextReplaceExample-out.pptx", slides.export.SaveFormat.PPTX)
