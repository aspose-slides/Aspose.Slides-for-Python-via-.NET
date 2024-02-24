import aspose.pydrawing as drawing
import aspose.slides as slides


def format_lines(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 150, 75)

        # Set the fill color of the rectangle shape
        shape.fill_format.fill_type = slides.FillType.SOLID
        shape.fill_format.solid_fill_color.color = drawing.Color.white

        # Apply some formatting on the line of the rectangle
        shape.line_format.style = slides.LineStyle.THICK_THIN
        shape.line_format.width = 7
        shape.line_format.dash_style = slides.LineDashStyle.DASH

        # Set the color of the line of rectangle
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.blue

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_format_lines_out.pptx", slides.export.SaveFormat.PPTX)
