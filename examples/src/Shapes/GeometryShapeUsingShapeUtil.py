
import aspose.pydrawing as drawing
import aspose.slides as slides

"""
The example demonstrates using of ShapeUtil for editing shape geometry as System.Drawing.Drawing2D.GrpahicsPath object.
"""

outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Create new shape
    shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 100)

    # Get geometry path of the shape
    originalPath = shape.get_geometry_paths()[0]
    originalPath.fill_mode = slides.PathFillModeType.NONE

    # Create new graphics path with text
    graphicsPath = drawing.drawing2d.GraphicsPath()
    graphicsPath.add_string("Text in shape", drawing.FontFamily("Arial"), 1, 40, drawing.PointF(10, 10), drawing.StringFormat.generic_default)

    # Convert graphics path to geometry path
    textPath = slides.util.ShapeUtil.graphics_path_to_geometry_path(graphicsPath)
    textPath.fill_mode = slides.PathFillModeType.NORMAL

    # Set combination of new geometry path and origin geometry path to the shape
    shape.set_geometry_paths( [originalPath, textPath] )

    # Save the presentation
    pres.save(outDir + "shapes_set_geometry_path_with_util_out.pptx", slides.export.SaveFormat.PPTX)
