import aspose.slides as slides
import aspose.pydrawing as drawing


def shapes_add_arrow_shaped_line(global_opts):
    # Instantiate Presentation class that represents the PPTX file
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add an autoshape of type line
        shape = slide.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)

        # Apply some formatting on the line
        shape.line_format.style = slides.LineStyle.THICK_BETWEEN_THIN
        shape.line_format.width = 10

        shape.line_format.dash_style = slides.LineDashStyle.DASH_DOT

        shape.line_format.begin_arrowhead_length = slides.LineArrowheadLength.SHORT
        shape.line_format.begin_arrowhead_style = slides.LineArrowheadStyle.OVAL

        shape.line_format.end_arrowhead_length = slides.LineArrowheadLength.LONG
        shape.line_format.end_arrowhead_style = slides.LineArrowheadStyle.TRIANGLE

        shape.line_format.fill_format.fill_type = slides.FillType.SOLID
        shape.line_format.fill_format.solid_fill_color.color = drawing.Color.maroon

        # Write the PPTX to Disk
        pres.save(global_opts.out_dir + "shapes_add_arrow_shaped_line_out.pptx", slides.export.SaveFormat.PPTX)
