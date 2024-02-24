import aspose.slides as slides


def charts_series_invert_if_negative(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400, True)
		series = chart.chart_data.series
		chart.chart_data.series.clear()

		series.add(chart.chart_data.chart_data_workbook.get_cell(0, "B1"), chart.type)
		series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B2", -5))
		series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B3", 3))
		series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B4", -2))
		series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B5", 1))

		series[0].invert_if_negative = False

		series[0].data_points[2].invert_if_negative = True

		pres.save(global_opts.out_dir + "charts_series_invert_if_negative_out.pptx", slides.export.SaveFormat.PPTX)
