import aspose.slides as slides


def charts_support_for_bubble_chart_scaling(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 100, 100, 400, 300)
		chart.chart_data.series_groups[0].bubble_size_scale = 150
		pres.save(global_opts.out_dir + "charts_support_for_bubble_chart_scaling_out.pptx",slides.export.SaveFormat.PPTX)
