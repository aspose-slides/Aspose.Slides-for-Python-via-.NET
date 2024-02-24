import aspose.slides as slides


def charts_setting_position_axis(options):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 450, 300)
		chart.axes.horizontal_axis.axis_between_categories = True

		pres.save(options.out_dir + "charts_setting_position_axis_out.pptx", slides.export.SaveFormat.PPTX)
