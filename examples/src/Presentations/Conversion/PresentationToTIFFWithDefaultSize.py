import aspose.slides as slides

def convert_to_tiff():
    #ExStart:PresentationToTIFFWithDefaultSize
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        # Saving the presentation to TIFF document
        presentation.save(outDir + "convert_to_tiff_out.tiff", slides.export.SaveFormat.TIFF)
    #ExEnd:PresentationToTIFFWithDefaultSize
