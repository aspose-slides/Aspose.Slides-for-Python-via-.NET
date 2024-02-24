import aspose.slides as slides


def charts_setting_font_properties(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

		chart.has_data_table = True

		chart.chart_data_table.text_format.portion_format.font_bold = slides.NullableBool.TRUE
		chart.chart_data_table.text_format.portion_format.font_height = 20

		pres.save(global_opts.out_dir + "charts_setting_font_properties_out.pptx", slides.export.SaveFormat.PPTX)
