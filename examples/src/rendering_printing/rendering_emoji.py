import aspose.slides as slides


def rendering_emoji(global_opts):
	with slides.Presentation(global_opts.data_dir + "rendering_emoji.pptx") as pres:
		pres.save(global_opts.out_dir + "rendering_emoji_out.pdf", slides.export.SaveFormat.PDF)
