import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:AddStretchOffsetForImageFill
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Prseetation class that represents the PPTX
with slides.Presentation() as pres:
    # Get the first slide
    sld = pres.slides[0]

    # Instantiate the Image class
    img = drawing.Bitmap(dataDir+ "image1.jpg")
    imgx = pres.images.add_image(img)

    # Add Picture Frame with height and width equivalent of Picture
    sld.shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 50, 150, imgx.width, imgx.height, imgx)

    #Write the PPTX file to disk
    pres.save(outDir + "shapes_add_stretch_offset_out.pptx", slides.export.SaveFormat.PPTX)

#ExEnd:AddStretchOffsetForImageFill
