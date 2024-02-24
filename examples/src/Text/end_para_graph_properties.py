import aspose.slides as slides


def end_para_graph_properties(global_opts):
    with slides.Presentation() as pres:
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 10, 10, 200, 250)

        para1 = slides.Paragraph()
        para1.portions.add(slides.Portion("Sample text"))

        para2 = slides.Paragraph()
        para2.portions.add(slides.Portion("Sample text 2"))

        end_paragraph_portion_format = slides.PortionFormat()
        end_paragraph_portion_format.font_height = 48
        end_paragraph_portion_format.latin_font = slides.FontData("Times New Roman")
        para2.end_paragraph_portion_format = end_paragraph_portion_format

        shape.text_frame.paragraphs.add(para1)
        shape.text_frame.paragraphs.add(para2)

        pres.save(global_opts.out_dir + "text_set_end_paragraph_portion_format_out.pptx", slides.export.SaveFormat.PPTX)
