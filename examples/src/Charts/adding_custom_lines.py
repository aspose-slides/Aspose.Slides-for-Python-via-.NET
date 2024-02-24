import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_adding_custom_lines(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 400)
        shape = chart.user_shapes.shapes.add_auto_shape(slides.ShapeType.LINE, 0, chart.height / 2, chart.width, 0)
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.red
        pres.save(options.out_dir + "charts_adding_custom_lines_out.pptx", slides.export.SaveFormat.PPTX)
