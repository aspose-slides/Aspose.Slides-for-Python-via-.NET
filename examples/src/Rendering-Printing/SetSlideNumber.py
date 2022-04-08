import aspose.slides as slides

def rendering_set_slide_number():
    #ExStart:SetSlideNumber
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        # Get the slide number
        firstSlideNumber = presentation.first_slide_number

        # Set the slide number
        presentation.first_slide_number=10

        presentation.save(outDir + "rendering_set_slide_number_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:SetSlideNumber
