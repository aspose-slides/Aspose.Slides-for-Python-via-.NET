import aspose.slides as slides

def charts_switching_rows_and_columns():
	#ExStart:SupportForSwitchingRowsAndColumns

	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 400, 300)

		categoriesCells = []

		for i in range(len(chart.chart_data.categories)):
			categoriesCells.append(chart.chart_data.categories[i].as_cell)

		seriesCells =[]
		for i in range(len(chart.chart_data.series)):
			seriesCells.append(chart.chart_data.series[i].name.as_cells[0])

		chart.chart_data.switch_row_column()

		pres.save(outDir + "charts_switching_rows_and_columns_out.pptx", slides.export.SaveFormat.PPTX)
	#ExEnd:SupportForSwitchingRowsAndColumns
