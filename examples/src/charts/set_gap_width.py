import aspose.slides as slides


def charts_set_gap_width(options):
    # Creating empty presentation
    with slides.Presentation() as presentation:
        # Access first slide
        slide = presentation.slides[0]

        # Add chart with default data
        chart = slide.shapes.add_chart(slides.charts.ChartType.STACKED_COLUMN, 0, 0, 500, 500)

        # Setting the index of chart data sheet
        default_worksheet_index = 0

        # Getting the chart data worksheet
        fact = chart.chart_data.chart_data_workbook

        # Add series
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 0, 1, "Series 1"), chart.type)
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 0, 2, "Series 2"), chart.type)

        # Add Categories
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 1, 0, "Caetegoty 1"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 2, 0, "Caetegoty 2"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 3, 0, "Caetegoty 3"))

        # Take second chart series
        series = chart.chart_data.series[1]

        # Now populating series data
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 1, 1, 20))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 2, 1, 50))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 3, 1, 30))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 1, 2, 30))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 2, 2, 10))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 3, 2, 60))

        # Set gap_width value
        series.parent_series_group.gap_width = 50

        # Save presentation with chart
        presentation.save(options.out_dir + "charts_set_gap_width_out.pptx", slides.export.SaveFormat.PPTX)
