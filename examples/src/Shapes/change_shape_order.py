import aspose.slides as slides


def change_shape_order(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        slide = presentation.slides[0]
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 365, 400, 150)
        shape.fill_format.fill_type = slides.FillType.NO_FILL
        shape.add_text_frame(" ")

        text_frame = shape.text_frame
        para = text_frame.paragraphs[0]
        portion = para.portions[0]
        portion.text = "Watermark Text Watermark Text Watermark Text"
        shape = slide.shapes.add_auto_shape(slides.ShapeType.TRIANGLE, 200, 365, 400, 150)
        slide.shapes.reorder(2, shape)

        presentation.save(global_opts.out_dir + "shapes_reorder_out.pptx", slides.export.SaveFormat.PPTX)
