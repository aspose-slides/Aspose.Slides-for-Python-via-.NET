import aspose.slides as slides


def add_hyperlink(global_opts):
    with slides.Presentation() as presentation:
        shape1 = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 600, 50, False)
        shape1.add_text_frame("Aspose: File Format APIs")
        shape1.text_frame.paragraphs[0].portions[0].portion_format.hyperlink_click = slides.Hyperlink(
            "https:#www.aspose.com/")
        shape1.text_frame.paragraphs[0].portions[
            0].portion_format.hyperlink_click.tooltip = "More than 70% Fortune 100 companies trust Aspose APIs"
        shape1.text_frame.paragraphs[0].portions[0].portion_format.font_height = 32

        presentation.save(global_opts.out_dir + "hyperlink_add_hyperlink_out.pptx", slides.export.SaveFormat.PPTX)
