import aspose.slides as slides

def charts_set_external_workbook():
    #ExStart:set_external_workbook
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, False)
        chartData = chart.chart_data
                        
        chartData.set_external_workbook(dataDir + "charts_external_workbook.xlsx")

        chartData.series.add(chartData.chart_data_workbook.get_cell(0, "B1"), slides.charts.ChartType.PIE)
        chartData.series[0].data_points.add_data_point_for_pie_series(chartData.chart_data_workbook.get_cell(0, "B2"))
        chartData.series[0].data_points.add_data_point_for_pie_series(chartData.chart_data_workbook.get_cell(0, "B3"))
        chartData.series[0].data_points.add_data_point_for_pie_series(chartData.chart_data_workbook.get_cell(0, "B4"))

        chartData.categories.add(chartData.chart_data_workbook.get_cell(0, "A2"))
        chartData.categories.add(chartData.chart_data_workbook.get_cell(0, "A3"))
        chartData.categories.add(chartData.chart_data_workbook.get_cell(0, "A4"))
        pres.save(outDir + "charts_set_external_workbook_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:set_external_workbook

