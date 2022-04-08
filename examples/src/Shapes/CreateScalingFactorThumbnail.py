import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:CreateScalingFactorThumbnail
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as p:
    # Create a full scale image
    with p.slides[0].shapes[0].get_thumbnail(slides.ShapeThumbnailBounds.SHAPE, 2, 2) as bitmap:
        # Save the image to disk in PNG format
        bitmap.save(outDir + "shapes_create_scaling_thumbnail_out.png", drawing.imaging.ImageFormat.png)
#ExEnd:CreateScalingFactorThumbnail



