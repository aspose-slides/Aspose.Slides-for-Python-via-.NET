import aspose.slides as slides

def charts_set_external_workbook_with_update_chart_data():
    #ExStart:SetExternalWorkbookWithUpdateChartData

    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, True)
        chartData = chart.chart_data

        chartData.set_external_workbook("http:#path/doesnt/exists", False)

        pres.save(outDir + "charts_set_external_workbook_with_update_chart_data_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:SetExternalWorkbookWithUpdateChartData
