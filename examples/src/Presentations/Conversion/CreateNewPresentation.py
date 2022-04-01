import aspose.slides as slides

def create_new_presentation():
    #ExStart:CreateNewPresentation
    # The path to the documents directory.
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation() as presentation:
        # Get the first slide
        slide = presentation.slides[0]

        # Add an autoshape of type line
        slide.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)
        presentation.save(outDir + "create_new_presentation_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:CreateNewPresentation

 