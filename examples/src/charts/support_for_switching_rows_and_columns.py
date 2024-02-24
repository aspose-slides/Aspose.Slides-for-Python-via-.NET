import aspose.slides as slides


def charts_switching_rows_and_columns(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 400, 300)

		categories_cells = []

		for i in range(len(chart.chart_data.categories)):
			categories_cells.append(chart.chart_data.categories[i].as_cell)

		series_cells = []
		for i in range(len(chart.chart_data.series)):
			series_cells.append(chart.chart_data.series[i].name.as_cells[0])

		chart.chart_data.switch_row_column()

		pres.save(global_opts.out_dir + "charts_switching_rows_and_columns_out.pptx", slides.export.SaveFormat.PPTX)
