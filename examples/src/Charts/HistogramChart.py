import aspose.slides as slides

def charts_histogram_chart():
	#ExStart:HistogramChart
	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.HISTOGRAM, 50, 50, 500, 400)
		chart.chart_data.categories.clear()
		chart.chart_data.series.clear()

		wb = chart.chart_data.chart_data_workbook

		wb.clear(0)

		series = chart.chart_data.series.add(slides.charts.ChartType.HISTOGRAM)
		series.data_points.add_data_point_for_histogram_series(wb.get_cell(0, "A1", 15))
		series.data_points.add_data_point_for_histogram_series(wb.get_cell(0, "A2", -41))
		series.data_points.add_data_point_for_histogram_series(wb.get_cell(0, "A3", 16))
		series.data_points.add_data_point_for_histogram_series(wb.get_cell(0, "A4", 10))
		series.data_points.add_data_point_for_histogram_series(wb.get_cell(0, "A5", -23))
		series.data_points.add_data_point_for_histogram_series(wb.get_cell(0, "A6", 16))

		chart.axes.horizontal_axis.aggregation_type = slides.charts.AxisAggregationType.AUTOMATIC

		pres.save(outDir + "charts_histogram_chart_out.pptx", slides.export.SaveFormat.PPTX)
	#ExEnd:HistogramChart
