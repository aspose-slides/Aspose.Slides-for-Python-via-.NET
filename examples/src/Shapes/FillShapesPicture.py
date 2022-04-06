import aspose.slides as slides
import aspose.pydrawing as drawing

#ExStart:FillShapesPicture
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Add autoshape of rectangle type
    shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)


    # Set the fill type to Picture
    shp.fill_format.fill_type = slides.FillType.PICTURE

    # Set the picture fill mode
    shp.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.TILE

    # Set the picture
    img = drawing.Bitmap(dataDir + "image2.jpg")
    imgx = pres.images.add_image(img)
    shp.fill_format.picture_fill_format.picture.image = imgx

    #Write the PPTX file to disk
    pres.save(outDir + "shapes_filltype_picture_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:FillShapesPicture