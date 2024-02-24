import aspose.slides as slides
import aspose.pydrawing as drawing


def formatted_rectangle(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 150, 50)

        # Apply some formatting to rectangle shape
        shape.fill_format.fill_type = slides.FillType.SOLID
        shape.fill_format.solid_fill_color.color = drawing.Color.chocolate

        # Apply some formatting to the line of rectangle
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.black
        shape.line_format.width = 5

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_formatted_rectangle_out.pptx", slides.export.SaveFormat.PPTX)
