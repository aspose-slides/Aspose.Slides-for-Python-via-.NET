import aspose.pydrawing as drawing
import aspose.slides as slides


def charts_automatic_chart_series_color(options):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        # Access first slide
        slide = presentation.slides[0]

        # Add chart with default data
        chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 0, 0, 500, 500)

        # Set first series to Show Values
        chart.chart_data.series[0].labels.default_data_label_format.show_value = True

        # Setting the index of chart data sheet
        default_worksheet_index = 0

        # Getting the chart data worksheet
        fact = chart.chart_data.chart_data_workbook

        # Delete default generated series and categories
        chart.chart_data.series.clear()
        chart.chart_data.categories.clear()
        s = len(chart.chart_data.series)
        s = len(chart.chart_data.categories)

        # Adding new series
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 0, 1, "Series 1"), chart.type)
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 0, 2, "Series 2"), chart.type)

        # Adding new categories
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 1, 0, "Caetegoty 1"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 2, 0, "Caetegoty 2"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 3, 0, "Caetegoty 3"))

        # Take first chart series
        series = chart.chart_data.series[0]

        # Now populating series data
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 1, 1, 20))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 2, 1, 50))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 3, 1, 30))

        # Setting automatic fill color for series
        series.format.fill.fill_type = slides.FillType.NOT_DEFINED

        # Take second chart series
        series = chart.chart_data.series[1]

        # Now populating series data
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 1, 2, 30))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 2, 2, 10))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(default_worksheet_index, 3, 2, 60))

        # Setting fill color for series
        series.format.fill.fill_type = slides.FillType.SOLID
        series.format.fill.solid_fill_color.color = drawing.Color.gray

        # Save presentation with chart
        presentation.save(options.out_dir + "charts_automatic_chart_series_color_out.pptx", slides.export.SaveFormat.PPTX)
