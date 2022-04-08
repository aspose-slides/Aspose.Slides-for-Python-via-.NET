import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:ThumbnailFromSlide
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
    # Access the first slide
    sld = pres.slides[0]

    # Create a full scale image
    bmp = sld.get_thumbnail(1, 1)

    # Save the image to disk in JPEG format
    bmp.save(outDir + "thumbnail_from_slide_out.jpg", drawing.imaging.ImageFormat.jpeg)
#ExEnd:ThumbnailFromSlide