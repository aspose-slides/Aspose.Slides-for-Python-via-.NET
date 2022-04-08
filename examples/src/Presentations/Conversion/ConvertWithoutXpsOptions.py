import aspose.slides as slides

def convert_to_xps():
    #ExStart:ConvertWithoutXpsOptions
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        # Saving the presentation to XPS document
        pres.save(outDir + "convert_to_xps_out.xps", slides.export.SaveFormat.XPS)
    #ExEnd:ConvertWithoutXpsOptions