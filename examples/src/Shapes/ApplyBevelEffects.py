import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:ApplyBevelEffects
# The path to the documents directory.                    
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation() as pres:
    slide = pres.slides[0]

    # Add a shape on slide
    shape = slide.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 30, 30, 100, 100)
    shape.fill_format.fill_type = slides.FillType.SOLID
    shape.fill_format.solid_fill_color.color = drawing.Color.green
    format = shape.line_format.fill_format
    format.fill_type = slides.FillType.SOLID
    format.solid_fill_color.color = drawing.Color.orange
    shape.line_format.width = 2.0

    # Set three_dformat properties of shape
    shape.three_dformat.depth = 4
    shape.three_dformat.bevel_top.bevel_type = slides.BevelPresetType.CIRCLE
    shape.three_dformat.bevel_top.height = 6
    shape.three_dformat.bevel_top.width = 6
    shape.three_dformat.camera.camera_type = slides.CameraPresetType.ORTHOGRAPHIC_FRONT
    shape.three_dformat.light_rig.light_type = slides.LightRigPresetType.THREE_PT
    shape.three_dformat.light_rig.direction = slides.LightingDirection.TOP

    # Write the presentation as a PPTX file
    pres.save(outDir + "shapes_apply_bevel_effects_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ApplyBevelEffects
