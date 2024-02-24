import aspose.slides as slides
import aspose.pydrawing as drawing


def formatted_eclipse(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of ellipse type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 50, 150, 150, 50)

        # Apply some formatting to ellipse shape
        shape.fill_format.fill_type = slides.FillType.SOLID
        shape.fill_format.solid_fill_color.color = drawing.Color.chocolate

        # Apply some formatting to the line of Ellipse
        shape.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.black
        shape.line_format.width = 5

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_formatted_ellipse_out.pptx", slides.export.SaveFormat.PPTX)
