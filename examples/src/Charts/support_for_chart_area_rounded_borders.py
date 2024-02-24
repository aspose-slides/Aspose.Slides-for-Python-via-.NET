import aspose.slides as slides


def charts_chart_area_rounded_borders(options):
	with slides.Presentation() as presentation:
		slide = presentation.slides[0]
		chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 100, 600, 400)
		chart.line_format.fill_format.fill_type = slides.FillType.SOLID
		chart.line_format.style = slides.LineStyle.SINGLE
		chart.has_rounded_corners = True

		presentation.save(options.out_dir + "charts_chart_area_rounded_borders_out.pptx", slides.export.SaveFormat.PPTX)
