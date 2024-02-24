import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_changing_series_color(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 600, 400)
		point = chart.chart_data.series[0].data_points[1]
		point.explosion = 30
		point.format.fill.fill_type = slides.FillType.SOLID
		point.format.fill.solid_fill_color.color = drawing.Color.blue

		pres.save(global_opts.out_dir + "charts_changing_series_color_out.pptx", slides.export.SaveFormat.PPTX)
