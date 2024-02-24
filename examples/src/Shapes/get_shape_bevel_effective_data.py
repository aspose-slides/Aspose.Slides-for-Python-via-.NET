import aspose.slides as slides


def get_shape_bevel_effective_data(global_opts):
    with slides.Presentation(global_opts.data_dir + "shapes_3d_effective.pptx") as pres:
        three_d_effective_data = pres.slides[0].shapes[0].three_d_format.get_effective()

        print("= Effective shape's top face relief properties =")
        print("Type: " + str(three_d_effective_data.bevel_top.bevel_type))
        print("Width: " + str(three_d_effective_data.bevel_top.width))
        print("Height: " + str(three_d_effective_data.bevel_top.height))
