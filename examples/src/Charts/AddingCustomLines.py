import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_adding_custom_lines():
    #ExStart:AddingCustomLines
    # The path to the documents directory.
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 400)
        shape = chart.user_shapes.shapes.add_auto_shape(slides.ShapeType.LINE, 0, chart.height / 2, chart.width, 0)
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.red
        pres.save(outDir + "charts_AddCustomLines.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:AddingCustomLines

