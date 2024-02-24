import aspose.slides as slides
import aspose.pydrawing as drawing


def set_hyperlink_color(global_opts):
    with slides.Presentation() as presentation:
        shape1 = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 450, 50, False)
        shape1.add_text_frame("This is a sample of colored hyperlink.")
        shape1.text_frame.paragraphs[0].portions[0].portion_format.hyperlink_click = slides.Hyperlink(
            "https:#www.aspose.com/")
        shape1.text_frame.paragraphs[0].portions[
            0].portion_format.hyperlink_click.color_source = slides.HyperlinkColorSource.PORTION_FORMAT
        shape1.text_frame.paragraphs[0].portions[0].portion_format.fill_format.fill_type = slides.FillType.SOLID
        shape1.text_frame.paragraphs[0].portions[
            0].portion_format.fill_format.solid_fill_color.color = drawing.Color.red

        shape2 = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 200, 450, 50, False)
        shape2.add_text_frame("This is a sample of usual hyperlink.")
        shape2.text_frame.paragraphs[0].portions[0].portion_format.hyperlink_click = slides.Hyperlink(
            "https:#www.aspose.com/")

        presentation.save(global_opts.out_dir + "hyperlink_set_color_out.pptx", slides.export.SaveFormat.PPTX)
