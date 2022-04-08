import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:AddRelativeScaleHeightPictureFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate presentation object
with slides.Presentation() as presentation:
    # Load Image to be added in presentaiton image collection
    img = drawing.Bitmap(dataDir + "image1.jpg")
    image = presentation.images.add_image(img)

    # Add picture frame to slide
    pf = presentation.slides[0].shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 50, 50, 100, 100, image)

    # Setting relative scale width and height
    pf.relative_scale_height = 0.8
    pf.relative_scale_width = 1.35

    # Save presentation
    presentation.save(outDir + "shapes_add_relative_scale_height_picture_frame_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddRelativeScaleHeightPictureFrame


