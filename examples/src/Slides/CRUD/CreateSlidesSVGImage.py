import aspose.slides as slides


#ExStart:CreateSlidesSVGImage
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file

with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Access the first slide
    sld = pres.slides[0]

    # Create a memory stream object
    with open(outDir + "crud_save_as_svg_out.svg", "wb") as stream:
        sld.write_as_svg(stream)
#ExEnd:CreateSlidesSVGImage