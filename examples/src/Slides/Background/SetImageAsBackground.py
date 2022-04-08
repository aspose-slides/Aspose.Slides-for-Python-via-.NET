import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:SetImageAsBackground
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate the Presentation class that represents the presentation file
with slides.Presentation() as pres:
    # Set the background with Image
    pres.slides[0].background.type = slides.BackgroundType.OWN_BACKGROUND
    pres.slides[0].background.fill_format.fill_type = slides.FillType.PICTURE
    pres.slides[0].background.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH

    # Set the picture
    img = drawing.Bitmap(dataDir + "image1.jpg")

    # Add image to presentation's images collection
    imgx = pres.images.add_image(img)

    pres.slides[0].background.fill_format.picture_fill_format.picture.image = imgx

    # Write the presentation to disk
    pres.save(outDir + "background_picture_fill_format_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:SetImageAsBackground