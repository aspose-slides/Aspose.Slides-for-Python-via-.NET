import aspose.pydrawing as drawing
import aspose.slides as slides


def format_join_styles(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add three autoshapes of rectangle type
        shape1 = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 100, 150, 75)
        shape2 = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 300, 100, 150, 75)
        shape3 = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 250, 150, 75)

        # Set the fill color of the rectangle shape
        shape1.fill_format.fill_type = slides.FillType.SOLID
        shape1.fill_format.solid_fill_color.color = drawing.Color.black
        shape2.fill_format.fill_type = slides.FillType.SOLID
        shape2.fill_format.solid_fill_color.color = drawing.Color.black
        shape3.fill_format.fill_type = slides.FillType.SOLID
        shape3.fill_format.solid_fill_color.color = drawing.Color.black

        # Set the line width
        shape1.line_format.width = 15
        shape2.line_format.width = 15
        shape3.line_format.width = 15

        # Set the color of the line of rectangle
        shape1.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape1.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
        shape2.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape2.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
        shape3.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape3.line_format.fill_format.solid_fill_color.color = drawing.Color.blue

        # Set the Join Style
        shape1.line_format.join_style = slides.LineJoinStyle.MITER
        shape2.line_format.join_style = slides.LineJoinStyle.BEVEL
        shape3.line_format.join_style = slides.LineJoinStyle.ROUND

        # Add text to each rectangle
        shape1.text_frame.text = "This is Miter Join Style"
        shape2.text_frame.text = "This is Bevel Join Style"
        shape3.text_frame.text = "This is Round Join Style"

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_line_format_out.pptx", slides.export.SaveFormat.PPTX)
