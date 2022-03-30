import aspose.slides as slides

def charts_font_properties_for_chart():
    #ExStart:FontPropertiesForChart
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 400)
        chart.text_format.portion_format.font_height = 20
        chart.chart_data.series[0].labels.default_data_label_format.show_value = True
        pres.save(outDir + "charts_font_properties_for_chart_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:FontPropertiesForChart
