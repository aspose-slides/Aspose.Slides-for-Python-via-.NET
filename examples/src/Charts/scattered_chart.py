import aspose.slides as slides


def charts_scattered_chart(options):
    with slides.Presentation() as pres:
        slide = pres.slides[0]

        # Creating the default chart
        chart = slide.shapes.add_chart(slides.charts.ChartType.SCATTER_WITH_SMOOTH_LINES, 0, 0, 400, 400)

        # Getting the default chart data worksheet index
        default_worksheet_index = 0

        # Getting the chart data worksheet
        fact = chart.chart_data.chart_data_workbook

        # Delete demo series
        chart.chart_data.series.clear()

        # Add new series
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 1, 1, "Series 1"), chart.type)
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 1, 3, "Series 2"), chart.type)

        # Take first chart series
        series = chart.chart_data.series[0]

        # Add new point (1:3) there.
        series.data_points.add_data_point_for_scatter_series(fact.get_cell(default_worksheet_index, 2, 1, 1), fact.get_cell(default_worksheet_index, 2, 2, 3))

        # Add new point (2:10)
        series.data_points.add_data_point_for_scatter_series(fact.get_cell(default_worksheet_index, 3, 1, 2), fact.get_cell(default_worksheet_index, 3, 2, 10))

        # Edit the type of series
        series.type = slides.charts.ChartType.SCATTER_WITH_STRAIGHT_LINES_AND_MARKERS

        # Changing the chart series marker
        series.marker.size = 10
        series.marker.symbol = slides.charts.MarkerStyleType.STAR

        # Take second chart series
        series = chart.chart_data.series[1]

        # Add new point (5:2) there.
        series.data_points.add_data_point_for_scatter_series(fact.get_cell(default_worksheet_index, 2, 3, 5), fact.get_cell(default_worksheet_index, 2, 4, 2))

        # Add new point (3:1)
        series.data_points.add_data_point_for_scatter_series(fact.get_cell(default_worksheet_index, 3, 3, 3), fact.get_cell(default_worksheet_index, 3, 4, 1))

        # Add new point (2:2)
        series.data_points.add_data_point_for_scatter_series(fact.get_cell(default_worksheet_index, 4, 3, 2), fact.get_cell(default_worksheet_index, 4, 4, 2))

        # Add new point (5:1)
        series.data_points.add_data_point_for_scatter_series(fact.get_cell(default_worksheet_index, 5, 3, 5), fact.get_cell(default_worksheet_index, 5, 4, 1))

        # Changing the chart series marker
        series.marker.size = 10
        series.marker.symbol = slides.charts.MarkerStyleType.CIRCLE

        pres.save(options.out_dir + "charts_scattered_chart_out.pptx", slides.export.SaveFormat.PPTX)
