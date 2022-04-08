import aspose.slides as slides

def rendering_emoji():
	#ExStart:RenderingEmoji
	dataDir = "./examples/data/"
	outDir = "./examples/out/"

	with slides.Presentation(dataDir + "rendering_emoji.pptx") as pres:
		pres.save(outDir + "rendering_emoji_out.pdf", slides.export.SaveFormat.PDF)
	#ExEnd:RenderingEmoji
