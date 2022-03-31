import aspose.slides as slides

def charts_setting_rotation_angle():
	#ExStart:SettingRotationAngle
	# The path to the documents directory.
	outDir = "./examples/out/"
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 450, 300)
		chart.axes.vertical_axis.has_title = True
		chart.axes.vertical_axis.title.text_format.text_block_format.rotation_angle = 90

		pres.save(outDir + "charts_setting_rotation_angle_out.pptx", slides.export.SaveFormat.PPTX)
	#ExEnd:SettingRotationAngle
