import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:ThumbnailWithUserDefinedDimensions
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:

    # Access the first slide
    sld = pres.slides[0]

    # User defined dimension
    desiredX = 1200
    desiredY = 800

    # Getting scaled value  of X and Y
    ScaleX = (1.0 / pres.slide_size.size.width) * desiredX
    ScaleY = (1.0 / pres.slide_size.size.height) * desiredY


    # Create a full scale image
    bmp = sld.get_thumbnail(ScaleX, ScaleY)

    # Save the image to disk in JPEG format
    bmp.save(outDir + "thumbnail_user_defined_dimensions_out.jpg", drawing.imaging.ImageFormat.jpeg)
#ExEnd:ThumbnailWithUserDefinedDimensions