import aspose.slides as slides
import aspose.pydrawing as drawing


def fill_shapes_pattern(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

        # Set the fill type to Pattern
        shape.fill_format.fill_type = slides.FillType.PATTERN

        # Set the pattern style
        shape.fill_format.pattern_format.pattern_style = slides.PatternStyle.TRELLIS

        # Set the pattern back and fore colors
        shape.fill_format.pattern_format.back_color.color = drawing.Color.light_gray
        shape.fill_format.pattern_format.fore_color.color = drawing.Color.yellow

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_filltype_pattern_out.pptx", slides.export.SaveFormat.PPTX)
