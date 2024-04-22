import aspose.slides as slides
import aspose.pydrawing as drawing


def rendering_3d(global_opts):
    with slides.Presentation() as pres:
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 150, 200, 200)
        shape.text_frame.text = "3D"
        shape.text_frame.paragraphs[0].paragraph_format.default_portion_format.font_height = 64
        
        shape.three_d_format.camera.camera_type = slides.CameraPresetType.ORTHOGRAPHIC_FRONT
        shape.three_d_format.camera.set_rotation(20, 30, 40)
        shape.three_d_format.light_rig.light_type = slides.LightRigPresetType.FLAT
        shape.three_d_format.light_rig.direction = slides.LightingDirection.TOP
        shape.three_d_format.material = slides.MaterialPresetType.FLAT
        shape.three_d_format.extrusion_height = 100
        shape.three_d_format.extrusion_color.color = drawing.Color.blue
        
        pres.slides[0].get_image(2, 2).save(global_opts.out_dir + "sample_3d.png")
        pres.save(global_opts.out_dir + "rendering_3d_out.pptx", slides.export.SaveFormat.PPTX)
