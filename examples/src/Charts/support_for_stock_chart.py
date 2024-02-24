import aspose.slides as slides


def charts_stock_chart(options):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.OPEN_HIGH_LOW_CLOSE, 50, 50, 600, 400, False)

		chart.chart_data.series.clear()
		chart.chart_data.categories.clear()

		wb = chart.chart_data.chart_data_workbook

		chart.chart_data.categories.add(wb.get_cell(0, 1, 0, "A"))
		chart.chart_data.categories.add(wb.get_cell(0, 2, 0, "B"))
		chart.chart_data.categories.add(wb.get_cell(0, 3, 0, "C"))

		chart.chart_data.series.add(wb.get_cell(0, 0, 1, "Open"), chart.type)
		chart.chart_data.series.add(wb.get_cell(0, 0, 2, "High"), chart.type)
		chart.chart_data.series.add(wb.get_cell(0, 0, 3, "Low"), chart.type)
		chart.chart_data.series.add(wb.get_cell(0, 0, 4, "Close"), chart.type)

		series = chart.chart_data.series[0]

		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 1, 1, 72))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 2, 1, 25))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 3, 1, 38))

		series = chart.chart_data.series[1]
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 1, 2, 172))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 2, 2, 57))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 3, 2, 57))

		series = chart.chart_data.series[2]
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 1, 3, 12))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 2, 3, 12))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 3, 3, 13))

		series = chart.chart_data.series[3]
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 1, 4, 25))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 2, 4, 38))
		series.data_points.add_data_point_for_stock_series(wb.get_cell(0, 3, 4, 50))

		chart.chart_data.series_groups[0].up_down_bars.has_up_down_bars = True
		chart.chart_data.series_groups[0].hi_low_lines_format.line.fill_format.fill_type = slides.FillType.SOLID

		for ser in chart.chart_data.series:
			ser.format.line.fill_format.fill_type = slides.FillType.NO_FILL

		pres.save(options.out_dir + "charts_stock_chart_out.pptx", slides.export.SaveFormat.PPTX)
