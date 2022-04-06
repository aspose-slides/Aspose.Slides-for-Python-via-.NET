import aspose.slides as slides


#ExStart:AccessSmartArtShape
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load the desired the presentation
with slides.Presentation(dataDir + "smart_art_access.pptx") as pres:
    # Traverse through every shape inside first slide
    for shape in pres.slides[0].shapes:
        # Check if shape is of SmartArt type
        if type(shape) is slides.smartart.SmartArt:
            # Typecast shape to SmartArt
            print("Shape Name:" + shape.name)
#ExEnd:AccessSmartArtShape