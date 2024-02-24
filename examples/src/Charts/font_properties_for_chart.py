import aspose.slides as slides


def charts_font_properties_for_chart(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 400)
        chart.text_format.portion_format.font_height = 20
        chart.chart_data.series[0].labels.default_data_label_format.show_value = True
        pres.save(options.out_dir + "charts_font_properties_for_chart_out.pptx", slides.export.SaveFormat.PPTX)
