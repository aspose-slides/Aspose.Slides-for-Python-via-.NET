import aspose.pydrawing as drawing
import aspose.slides as slides

#ExStart:StretchOffsetLeftForPictureFrame
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    slide = pres.slides[0]

    # Instantiate the Image class
    img = drawing.Bitmap(dataDir + "image1.jpg")
    imgEx = pres.images.add_image(img)

    # Add an AutoShape of Rectangle type
    aShape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)

    # Set shape's fill type
    aShape.fill_format.fill_type = slides.FillType.PICTURE

    # Set shape's picture fill mode
    aShape.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH

    # Set image to fill the shape
    aShape.fill_format.picture_fill_format.picture.image = imgEx

    # Specify image offsets from the corresponding edge of the shape's bounding box
    aShape.fill_format.picture_fill_format.stretch_offset_left = 25
    aShape.fill_format.picture_fill_format.stretch_offset_right = 25
    aShape.fill_format.picture_fill_format.stretch_offset_top = -20
    aShape.fill_format.picture_fill_format.stretch_offset_bottom = -10


    #Write the PPTX file to disk
    pres.save(outDir + "shapes_stretch_offset_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:StretchOffsetLeftForPictureFrame
