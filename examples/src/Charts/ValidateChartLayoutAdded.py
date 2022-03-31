import aspose.slides as slides
import aspose.pydrawing as drawing

def charts_validate_chart_layout():
    #ExStart:ValidateChartLayoutAdded
    # The path to the documents directory.
    outDir = "./examples/out/"
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 350)
        chart.validate_chart_layout()
        x = chart.plot_area.actual_x
        y = chart.plot_area.actual_y
        w = chart.plot_area.actual_width
        h = chart.plot_area.actual_height

        # Saving presentation
        pres.save(outDir + "charts_validate_chart_layout_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:ValidateChartLayoutAdded