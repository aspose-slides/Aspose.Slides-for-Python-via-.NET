import aspose.pydrawing as drawing
import aspose.slides as slides


def geometry_shape_using_shape_util(global_opts):
    """The example demonstrates using of ShapeUtil for editing shape geometry as
    System.Drawing.Drawing2D.GraphicsPath object."""
    with slides.Presentation() as pres:
        # Create new shape
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 100)

        # Get geometry path of the shape
        original_path = shape.get_geometry_paths()[0]
        original_path.fill_mode = slides.PathFillModeType.NONE

        # Create new graphics path with text
        graphics_path = drawing.drawing2d.GraphicsPath()
        graphics_path.add_string("Text in shape", drawing.FontFamily("Arial"), 1, 40.0, drawing.PointF(10, 10),
                                 drawing.StringFormat.generic_default)

        # Convert graphics path to geometry path
        text_path = slides.util.ShapeUtil.graphics_path_to_geometry_path(graphics_path)
        text_path.fill_mode = slides.PathFillModeType.NORMAL

        # Set combination of new geometry path and origin geometry path to the shape
        shape.set_geometry_paths([original_path, text_path])

        # Save the presentation
        pres.save(global_opts.out_dir + "shapes_set_geometry_path_with_util_out.pptx", slides.export.SaveFormat.PPTX)
