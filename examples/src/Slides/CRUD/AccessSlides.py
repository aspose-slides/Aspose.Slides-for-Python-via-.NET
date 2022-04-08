import aspose.slides as slides

#ExStart:AccessSlides
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create an instance of Presentation class
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Accessing a slide using its slide index
    slide = pres.slides[0]
    print("Slide Number: " + str(slide.slide_number))
#ExEnd:AccessSlides