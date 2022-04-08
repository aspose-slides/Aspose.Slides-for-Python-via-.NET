import aspose.slides as slides


#ExStart:AccessSlidebyIndex
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    # Obtain a slide's reference by its index
    slide = presentation.slides[0]
#ExEnd:AccessSlidebyIndex           