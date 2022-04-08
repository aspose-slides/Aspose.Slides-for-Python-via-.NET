import aspose.slides as slides
import aspose.pydrawing as drawing

def charts_get_chart_image():
	#ExStart:GetChartImage
	# The path to the documents directory.
	dataDir = "./examples/data/"
	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)
		img = chart.get_thumbnail()
		img.save(outDir + "charts_get_chart_image_out.png", drawing.imaging.ImageFormat.png)

	#ExEnd:GetChartImage

