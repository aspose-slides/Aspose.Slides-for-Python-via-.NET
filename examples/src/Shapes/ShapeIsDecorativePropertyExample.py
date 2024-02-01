import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def shape_is_decorative_property_example():
    with slides.Presentation() as pres:
        # Create new shape
        shape1 = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 10, 10, 100, 100)
        
        # Set shape as “decorative” object
        shape1.is_decorative = True
        
        # Save result
        pres.save(outDir + "DecorativeDemo.pptx", slides.export.SaveFormat.PPTX)
