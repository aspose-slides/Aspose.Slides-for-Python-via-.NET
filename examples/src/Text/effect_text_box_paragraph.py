import aspose.slides as slides


def effect_text_box_paragraph(global_opts):
	with slides.Presentation(global_opts.data_dir + "text_add_animation_effect.pptx") as pres:
		sequence = pres.slides[0].timeline.main_sequence
		for auto_shape in pres.slides[0].shapes:
			for paragraph in auto_shape.text_frame.paragraphs:
				effects = sequence.get_effects_by_paragraph(paragraph)

				if len(effects) > 0:
					print("Paragraph \"" + paragraph.text + "\" has " + str(effects[0].type) + " effect.")
