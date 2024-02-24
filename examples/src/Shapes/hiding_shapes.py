import aspose.slides as slides
            

def hiding_shapes(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape1 = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 40, 150, 50)
        shape2 = slide.shapes.add_auto_shape(slides.ShapeType.MOON, 160, 40, 150, 50)
        alt_text = "User Defined"

        for shape in slide.shapes:
            if shape.alternative_text == alt_text:
                shape.hidden = True

        # Save presentation to disk
        pres.save(global_opts.out_dir + "shapes_hide_shape_out.pptx", slides.export.SaveFormat.PPTX)
