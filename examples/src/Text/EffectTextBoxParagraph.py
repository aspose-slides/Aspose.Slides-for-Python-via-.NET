import aspose.slides as slides


#ExStart:EffectTextBoxParagraph
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_add_animation_effect.pptx") as pres:
	sequence = pres.slides[0].timeline.main_sequence
	for autoShape in pres.slides[0].shapes:
		for paragraph in autoShape.text_frame.paragraphs:
			effects = sequence.get_effects_by_paragraph(paragraph)

			if len(effects) > 0:
				print("Paragraph \"" + paragraph.text + "\" has " + str(effects[0].type) + " effect.")
#ExEnd:EffectTextBoxParagraph
