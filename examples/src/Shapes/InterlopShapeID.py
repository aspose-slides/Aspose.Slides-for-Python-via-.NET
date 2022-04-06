import aspose.slides as slides

#ExStart:InterlopShapeID
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    # Getting unique shape identifier in slide scope
    print(str(presentation.slides[0].shapes[0].office_interop_shape_id))

#ExEnd:InterlopShapeID
