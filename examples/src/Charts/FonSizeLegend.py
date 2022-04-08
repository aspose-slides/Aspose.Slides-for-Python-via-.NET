import aspose.slides as slides


def charts_font_size_legend():
	#ExStart:FontSizeLegend
	# The path to the documents directory.

	dataDir = "./examples/data/"
	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

		chart.legend.text_format.portion_format.font_height = 20
		chart.axes.vertical_axis.is_automatic_min_value = False
		chart.axes.vertical_axis.min_value = -5
		chart.axes.vertical_axis.is_automatic_max_value = False
		chart.axes.vertical_axis.max_value = 10
		pres.save(outDir + "charts_font_size_legend_out.pptx", slides.export.SaveFormat.PPTX)

	#ExEnd:FontSizeLegend