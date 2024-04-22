import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_get_chart_image(global_opts):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)
		img = chart.get_image()
		img.save(global_opts.out_dir + "charts_get_chart_image_out.png", slides.ImageFormat.PNG)
