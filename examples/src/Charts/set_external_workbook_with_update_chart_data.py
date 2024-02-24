import aspose.slides as slides


def charts_set_external_workbook_with_update_chart_data(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, True)
        chart_data = chart.chart_data
        chart_data.set_external_workbook("http:#path/doesnt/exists", False)

        pres.save(options.out_dir + "charts_set_external_workbook_with_update_chart_data_out.pptx", slides.export.SaveFormat.PPTX)
