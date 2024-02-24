import aspose.pydrawing as drawing
import aspose.slides as slides


def charts_map_chart(global_opts):
    with slides.Presentation() as presentation:
        # Create empty chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.MAP, 50, 50, 500, 400, False)
        wb = chart.chart_data.chart_data_workbook

        # Add series and few data points
        series = chart.chart_data.series.add(slides.charts.ChartType.MAP)
        series.data_points.add_data_point_for_map_series(wb.get_cell(0, "B2", 5))
        series.data_points.add_data_point_for_map_series(wb.get_cell(0, "B3", 1))
        series.data_points.add_data_point_for_map_series(wb.get_cell(0, "B4", 10))

        # Add categories
        chart.chart_data.categories.add(wb.get_cell(0, "A2", "United States"))
        chart.chart_data.categories.add(wb.get_cell(0, "A3", "Mexico"))
        chart.chart_data.categories.add(wb.get_cell(0, "A4", "Brazil"))

        # Change data point value
        data_point = series.data_points[1]
        data_point.color_value.as_cell.value = "15"

        # Set data point appearance
        data_point.format.fill.fill_type = slides.FillType.SOLID
        data_point.format.fill.solid_fill_color.color = drawing.Color.green

        presentation.save(global_opts.out_dir + "charts_map_chart_out.pptx", slides.export.SaveFormat.PPTX)
