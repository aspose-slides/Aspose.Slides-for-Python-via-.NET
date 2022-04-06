import aspose.slides as slides

#ExStart:AccessSmartArtParticularLayout
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "smart_art_access_shape.pptx") as presentation:
    # Traverse through every shape inside first slide
    for shape in presentation.slides[0].shapes:
        # Check if shape is of SmartArt type
        if type(shape) is slides.smartart.SmartArt:
            # Typecast shape to SmartArt
            if shape.layout == slides.smartart.SmartArtLayoutType.BASIC_BLOCK_LIST:
                print("Do some thing here....")
#ExEnd:AccessSmartArtParticularLayout
