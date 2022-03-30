import aspose.slides as slides

def charts_clear_specific_chart_series_datapoints_data():
    #ExStart:ClearSpecificChartSeriesDataPointsData

    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "charts_with_chart.pptx") as pres:
        sl = pres.slides[0]

        chart = sl.shapes[0]

        for dataPoint in chart.chart_data.series[0].data_points:
            dataPoint.xvalue.as_cell.value = None
            dataPoint.yvalue.as_cell.value = None

        chart.chart_data.series[0].data_points.clear()

        pres.save(outDir + "charts_ClearSpecificChartSeriesDataPointsData_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:ClearSpecificChartSeriesDataPointsData
