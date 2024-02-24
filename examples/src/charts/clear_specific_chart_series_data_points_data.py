import aspose.slides as slides


def charts_clear_specific_chart_series_datapoints_data(options):
    with slides.Presentation(options.data_dir + "charts_with_chart.pptx") as pres:
        sl = pres.slides[0]

        chart = sl.shapes[0]

        for dataPoint in chart.chart_data.series[0].data_points:
            dataPoint.x_value.as_cell.value = None
            dataPoint.y_value.as_cell.value = None

        chart.chart_data.series[0].data_points.clear()

        pres.save(options.out_dir + "charts_clear_specific_chart_series_datapoints_data_out.pptx", slides.export.SaveFormat.PPTX)
