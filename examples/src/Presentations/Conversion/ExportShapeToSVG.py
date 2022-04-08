import aspose.slides as slides

def export_shape_to_svg():
	#ExStart:ExportShapeToSVG
	dataDir = "./examples/data/"
	outDir = "./examples/out/"

	with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
		with open(outDir + "export_shape_to_svg_out.svg", "xb") as stream:
			pres.slides[0].shapes[0].write_as_svg(stream)
	#ExEnd:ExportShapeToSVG
