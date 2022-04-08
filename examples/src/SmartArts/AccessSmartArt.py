import aspose.slides as slides

#ExStart:AccessSmartArt
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
            smart = shape

            # Traverse through all nodes inside SmartArt
            for node in smart.all_nodes:
                # Printing the SmartArt node parameters
                outString = "Text = {0},  Level = {1}, Position = {2}".format(node.text_frame.text, node.level, node.position)
                print(outString)
#ExEnd:AccessSmartArt