import aspose.slides as slides


def charts_box_chart(options):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BOX_AND_WHISKER, 50, 50, 500, 400)
		chart.chart_data.categories.clear()
		chart.chart_data.series.clear()

		wb = chart.chart_data.chart_data_workbook
		wb.clear(0)

		chart.chart_data.categories.add(wb.get_cell(0, "A1", "Category 1"))
		chart.chart_data.categories.add(wb.get_cell(0, "A2", "Category 1"))
		chart.chart_data.categories.add(wb.get_cell(0, "A3", "Category 1"))
		chart.chart_data.categories.add(wb.get_cell(0, "A4", "Category 1"))
		chart.chart_data.categories.add(wb.get_cell(0, "A5", "Category 1"))
		chart.chart_data.categories.add(wb.get_cell(0, "A6", "Category 1"))

		series = chart.chart_data.series.add(slides.charts.ChartType.BOX_AND_WHISKER)

		series.quartile_method = slides.charts.QuartileMethodType.EXCLUSIVE
		series.show_mean_line = True
		series.show_mean_markers = True
		series.show_inner_points = True
		series.show_outlier_points = True

		series.data_points.add_data_point_for_box_and_whisker_series(wb.get_cell(0, "B1", 15))
		series.data_points.add_data_point_for_box_and_whisker_series(wb.get_cell(0, "B2", 41))
		series.data_points.add_data_point_for_box_and_whisker_series(wb.get_cell(0, "B3", 16))
		series.data_points.add_data_point_for_box_and_whisker_series(wb.get_cell(0, "B4", 10))
		series.data_points.add_data_point_for_box_and_whisker_series(wb.get_cell(0, "B5", 23))
		series.data_points.add_data_point_for_box_and_whisker_series(wb.get_cell(0, "B6", 16))

		pres.save(options.out_dir + "charts_box_chart_out.pptx", slides.export.SaveFormat.PPTX)
