import aspose.slides as slides


def charts_precision_of_data(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.LINE, 50, 50, 450, 300)
		chart.has_data_table = True
		chart.chart_data.series[0].number_format_of_values = "#,##0.00"

		pres.save(global_opts.out_dir + "charts_precision_of_data_out.pptx", slides.export.SaveFormat.PPTX)
