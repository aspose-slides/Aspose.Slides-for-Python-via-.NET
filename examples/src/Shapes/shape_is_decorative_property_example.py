import aspose.slides as slides


def shape_is_decorative_property_example(global_opts):
    with slides.Presentation() as pres:
        # Create new shape
        shape1 = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 10, 10, 100, 100)
        
        # Set shape as “decorative” object
        shape1.is_decorative = True
        
        # Save result
        pres.save(global_opts.out_dir + "DecorativeDemo.pptx", slides.export.SaveFormat.PPTX)
