import aspose.slides as slides


def export_shape_to_svg(global_opts):
	with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
		with open(global_opts.out_dir + "export_shape_to_svg_out.svg", "wb") as stream:
			pres.slides[0].shapes[0].write_as_svg(stream)
