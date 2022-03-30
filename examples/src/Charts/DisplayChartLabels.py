import aspose.slides as slides

def charts_display_chart_labels():
    #ExStart:DisplayChartLabels
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as presentation:
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 500, 400)
        chart.chart_data.series[0].labels.default_data_label_format.show_value = True
        chart.chart_data.series[0].labels.default_data_label_format.show_label_as_data_callout = True
        chart.chart_data.series[0].labels[2].data_label_format.show_label_as_data_callout = False
        presentation.save(outDir + "charts_display_chart_labels_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:DisplayChartLabels