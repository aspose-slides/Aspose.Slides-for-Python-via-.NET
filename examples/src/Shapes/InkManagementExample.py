import aspose.slides as slides
import aspose.pydrawing as drawing

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def ink_management_example():
    with slides.Presentation(dataDir + "SimpleInk.pptx") as presentation:
        # Get Ink shape
        ink_shape = presentation.slides[0].shapes[0]
        
        if ink_shape is not None:
            print("Width of the Ink shape =", ink_shape.width)
            print("Height of the Ink shape =", ink_shape.height)
            print("Brush height of the trace =", ink_shape.traces[0].brush.size.width)
            print("Brush color of the trace =", ink_shape.traces[0].brush.color.name)
            
            # Change color and size of the brush
            ink_shape.traces[0].brush.color = drawing.Color.red
            ink_shape.traces[0].brush.size = drawing.SizeF(10, 5)
        
        # Save presentation
        presentation.save(outDir + "SimpleInk_out.pptx", slides.export.SaveFormat.PPTX)
