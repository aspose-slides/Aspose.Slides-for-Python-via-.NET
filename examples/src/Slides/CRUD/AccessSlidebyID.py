import aspose.slides as slides

#ExStart:AccessSlidebyID
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:

    # Getting Slide ID
    id = presentation.slides[0].slide_id

    # Accessing Slide by ID
    slide = presentation.get_slide_by_id(id)
#ExEnd:AccessSlidebyID