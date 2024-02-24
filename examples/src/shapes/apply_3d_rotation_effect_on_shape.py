import aspose.slides as slides


def apply_3d_rotation_effect_on_shape(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as pres:
        auto_shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 30, 30, 200, 200)

        auto_shape.three_d_format.depth = 6
        auto_shape.three_d_format.camera.set_rotation(40, 35, 20)
        auto_shape.three_d_format.camera.camera_type = slides.CameraPresetType.ISOMETRIC_LEFT_UP
        auto_shape.three_d_format.light_rig.light_type = slides.LightRigPresetType.BALANCED

        auto_shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.LINE, 30, 300, 200, 200)
        auto_shape.three_d_format.depth = 6
        auto_shape.three_d_format.camera.set_rotation(0, 35, 20)
        auto_shape.three_d_format.camera.camera_type = slides.CameraPresetType.ISOMETRIC_LEFT_UP
        auto_shape.three_d_format.light_rig.light_type = slides.LightRigPresetType.BALANCED

        pres.save(global_opts.out_dir + "shapes_apply_3d_rotation_out.pptx", slides.export.SaveFormat.PPTX)
