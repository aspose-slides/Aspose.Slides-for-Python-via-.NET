import aspose.slides as slides

def props_access_layout_formats():
    #ExStart:AccessLayoutFormats

    # The path to the documents directory.
    dataDir = "./examples/data/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        for layoutSlide in pres.layout_slides:
            fillFormats = list(map(lambda shape: shape.fill_format, layoutSlide.shapes))
            lineFormats = list(map(lambda shape: shape.line_format, layoutSlide.shapes))
    #ExEnd:AccessLayoutFormats
