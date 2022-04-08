import aspose.slides as slides
import aspose.pydrawing as drawing

def charts_font_properties_for_invidual_legend():
	#ExStart:FontPropertiesForInvidualLegend
	dataDir = "./examples/data/"
	outDir = "./examples/out/"

	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

		tf = chart.legend.entries[1].text_format
		tf.portion_format.font_bold = 1
		tf.portion_format.font_height = 20
		tf.portion_format.font_italic = 1
		tf.portion_format.fill_format.fill_type = slides.FillType.SOLID 
		tf.portion_format.fill_format.solid_fill_color.color = drawing.Color.blue

		pres.save(outDir + "charts_font_properties_for_invidual_legend_out.pptx", slides.export.SaveFormat.PPTX)

	#ExEnd:FontPropertiesForInvidualLegend
