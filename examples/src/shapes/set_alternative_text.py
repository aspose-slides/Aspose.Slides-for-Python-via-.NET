import aspose.pydrawing as drawing
import aspose.slides as slides


def set_alternative_text(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape1 = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 40, 150, 50)
        shape2 = slide.shapes.add_auto_shape(slides.ShapeType.MOON, 160, 40, 150, 50)
        shape2.fill_format.fill_type = slides.FillType.SOLID
        shape2.fill_format.solid_fill_color.color = drawing.Color.gray

        for shape in slide.shapes:
            if shape is slides.AutoShape:
                shape.alternative_text = "User Defined"

        # Save presentation to disk
        pres.save(global_opts.out_dir + "shapes_set_alternative_text_out.pptx", slides.export.SaveFormat.PPTX)
