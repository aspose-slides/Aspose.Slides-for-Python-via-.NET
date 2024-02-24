import aspose.pydrawing as drawing
import aspose.slides as slides


def charts_set_invert_fill_color_chart(options):
    invert_color = drawing.Color.red
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 400, 300)
        workbook = chart.chart_data.chart_data_workbook

        chart.chart_data.series.clear()
        chart.chart_data.categories.clear()

        # Adding new series and categories
        chart.chart_data.series.add(workbook.get_cell(0, 0, 1, "Series 1"), chart.type)
        chart.chart_data.categories.add(workbook.get_cell(0, 1, 0, "Category 1"))
        chart.chart_data.categories.add(workbook.get_cell(0, 2, 0, "Category 2"))
        chart.chart_data.categories.add(workbook.get_cell(0, 3, 0, "Category 3"))

        # Take first chart series and populating series data.
        series = chart.chart_data.series[0]
        series.data_points.add_data_point_for_bar_series(workbook.get_cell(0, 1, 1, -20))
        series.data_points.add_data_point_for_bar_series(workbook.get_cell(0, 2, 1, 50))
        series.data_points.add_data_point_for_bar_series(workbook.get_cell(0, 3, 1, -30))
        series_color = series.get_automatic_series_color()
        series.invert_if_negative = True
        series.format.fill.fill_type = slides.FillType.SOLID
        series.format.fill.solid_fill_color.color = series_color
        series.inverted_solid_fill_color.color = invert_color
        pres.save(options.out_dir + "charts_set_invert_fill_color_chart_out.pptx", slides.export.SaveFormat.PPTX)
