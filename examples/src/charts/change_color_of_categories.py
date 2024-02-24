import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_change_color_of_categories(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

		point = chart.chart_data.series[0].data_points[0]
		point.format.fill.fill_type = slides.FillType.SOLID
		point.format.fill.solid_fill_color.color = drawing.Color.blue

		pres.save(global_opts.out_dir + "charts_change_color_of_categories.pptx", slides.export.SaveFormat.PPTX)
