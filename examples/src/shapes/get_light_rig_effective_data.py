import aspose.slides as slides


def get_light_rig_effective_data(global_opts):
    with slides.Presentation(global_opts.data_dir + "shapes_3d_effective.pptx") as pres:
        three_d_effective_data = pres.slides[0].shapes[0].three_d_format.get_effective()

        print("= Effective light rig properties =")
        print("Type: " + str(three_d_effective_data.light_rig.light_type))
        print("Direction: " + str(three_d_effective_data.light_rig.direction))
