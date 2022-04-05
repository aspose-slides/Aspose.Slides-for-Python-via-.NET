import aspose.slides as slides
import aspose.pydrawing as drawing

def rendering_3d():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 150, 200, 200)
        shape.text_frame.text = "3D"
        shape.text_frame.paragraphs[0].paragraph_format.default_portion_format.font_height = 64
        
        shape.three_dformat.camera.camera_type = slides.CameraPresetType.ORTHOGRAPHIC_FRONT
        shape.three_dformat.camera.set_rotation(20, 30, 40)
        shape.three_dformat.light_rig.light_type = slides.light_rigPresetType.FLAT
        shape.three_dformat.light_rig.direction = slides.LightingDirection.TOP
        shape.three_dformat.material = slides.MaterialPresetType.FLAT 
        shape.three_dformat.extrusion_height = 100
        shape.three_dformat.extrusion_color.color = drawing.Color.blue
        
        pres.slides[0].get_thumbnail(2, 2).save(outDir + "sample_3d.png")
        pres.save(outDir + "sandbox_3d.pptx", slides.export.SaveFormat.PPTX)


