import aspose.slides as slides


def solid_fill_scheme_color_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "FillColor.pptx") as pres:
        for shape in pres.slides[0].shapes:
            if type(shape) is slides.AutoShape:
                fill_format = shape.text_frame.paragraphs[0].portions[0].portion_format.fill_format.get_effective()
                print(f"Fill color: {fill_format.solid_fill_color}")
                print(f"Fill scheme color: {fill_format.solid_fill_color}")
