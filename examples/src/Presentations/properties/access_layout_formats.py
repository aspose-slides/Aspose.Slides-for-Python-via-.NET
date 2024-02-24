import aspose.slides as slides


def props_access_layout_formats(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        for layout_slide in pres.layout_slides:
            fill_formats = list(map(lambda shape: shape.fill_format, layout_slide.shapes))
            line_formats = list(map(lambda shape: shape.line_format, layout_slide.shapes))
