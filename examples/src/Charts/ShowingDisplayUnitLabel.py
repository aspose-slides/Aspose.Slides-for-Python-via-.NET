import aspose.slides as slides

def charts_showing_display_unit_label():
	#ExStart:ShowingDisplayUnitLabel
	outDir = "./examples/out/"
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 450, 300)
		chart.axes.vertical_axis.display_unit = slides.charts.DisplayUnitType.MILLIONS
		pres.save(outDir + "charts_showing_display_unit_label_out.pptx", slides.export.SaveFormat.PPTX)

	#ExEnd:ShowingDisplayUnitLabel