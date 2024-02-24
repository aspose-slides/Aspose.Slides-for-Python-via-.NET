import aspose.pydrawing as drawing
import aspose.slides as slides


def fill_shapes_with_solid_color(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        # Get the first slide
        slide = presentation.slides[0]

        # Add autoshape of rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

        # Set the fill type to Solid
        shape.fill_format.fill_type = slides.FillType.SOLID

        # Set the color of the rectangle
        shape.fill_format.solid_fill_color.color = drawing.Color.yellow

        # Write the PPTX file to disk
        presentation.save(global_opts.out_dir + "shapes_filltype_solid_out.pptx", slides.export.SaveFormat.PPTX)
