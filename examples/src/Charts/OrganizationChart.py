import aspose.slides as slides

def charts_organization_chart():
	#ExStart:OrganizationChart
	# The path to the documents directory.
	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		smartArt = pres.slides[0].shapes.add_smart_art(0, 0, 400, 400, slides.smartart.SmartArtLayoutType.PICTURE_ORGANIZATION_CHART)

		pres.save(outDir+"charts_organization_chart_out.pptx", slides.export.SaveFormat.PPTX)
	#ExEnd:OrganizationChart
