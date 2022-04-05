import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:CreateBoundsShapeThumbnail
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation class that represents the presentation file
with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
    # Create a Appearance bound shape image
    with presentation.slides[0].shapes[0].get_thumbnail(slides.ShapeThumbnailBounds.APPEARANCE, 1, 1) as bitmap:
        # Save the image to disk in PNG format
        bitmap.save(outDir + "shapes_get_thumbnail_bound_shape_out.png", drawing.imaging.ImageFormat.png)
#ExEnd:CreateBoundsShapeThumbnail