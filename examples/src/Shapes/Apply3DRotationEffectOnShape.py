import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:Apply3DRotationEffecrOnShapes
# The path to the documents directory.                    
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation() as pres:
    autoShape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 30, 30, 200, 200)

    autoShape.three_dformat.depth = 6
    autoShape.three_dformat.camera.set_rotation(40, 35, 20)
    autoShape.three_dformat.camera.camera_type = slides.CameraPresetType.ISOMETRIC_LEFT_UP
    autoShape.three_dformat.light_rig.light_type = slides.LightRigPresetType.BALANCED

    autoShape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.LINE, 30, 300, 200, 200)
    autoShape.three_dformat.depth = 6
    autoShape.three_dformat.camera.set_rotation(0, 35, 20)
    autoShape.three_dformat.camera.camera_type = slides.CameraPresetType.ISOMETRIC_LEFT_UP
    autoShape.three_dformat.light_rig.light_type = slides.LightRigPresetType.BALANCED


    pres.save(outDir + "shapes_apply_3d_rotation_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:Apply3DRotationEffecrOnShapes
