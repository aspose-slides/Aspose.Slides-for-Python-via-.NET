import aspose.slides as slides


def charts_organization_chart(global_opts):
	with slides.Presentation() as pres:
		smart_art = pres.slides[0].shapes.add_smart_art(0, 0, 400, 400, slides.smartart.SmartArtLayoutType.PICTURE_ORGANIZATION_CHART)
		pres.save(global_opts.out_dir + "charts_organization_chart_out.pptx", slides.export.SaveFormat.PPTX)
