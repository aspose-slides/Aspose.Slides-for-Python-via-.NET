import aspose.slides as slides

def charts_doughnut_chart_hole():
    #ExStart:DoughnutChartHole
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Create an instance of Presentation class
    with slides.Presentation() as presentation:

        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.DOUGHNUT, 50, 50, 400, 400)
        chart.chart_data.series_groups[0].doughnut_hole_size = 90

    # Write presentation to disk
    presentation.save(outDir + "charts_doughnut_chart_hole_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:DoughnutChartHole