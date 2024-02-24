import aspose.slides as slides


def get_camera_effective_data(global_opts):
    with slides.Presentation(global_opts.data_dir + "shapes_3d_effective.pptx") as pres:
        three_d_effective_data = pres.slides[0].shapes[0].three_d_format.get_effective()
        print("= Effective camera properties =")
        print("Type: " + str(three_d_effective_data.camera.camera_type))
        print("Field of view: " + str(three_d_effective_data.camera.field_of_view_angle))
        print("Zoom: " + str(three_d_effective_data.camera.zoom))
