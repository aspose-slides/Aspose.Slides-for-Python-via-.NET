import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:ManageParagraphPictureBulletsInPPT
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:

    # Accessing the first slide
    slide = presentation.slides[0]

    # Instantiate the image for bullets
    image = drawing.Bitmap(dataDir + "bullets.png")
    ippxImage = presentation.images.add_image(image)

    # Adding and accessing Autoshape
    autoShape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 400, 200)

    # Accessing the text frame of created autoshape
    textFrame = autoShape.text_frame

    # Removing the default exisiting paragraph
    textFrame.paragraphs.remove_at(0)

    # Creating new paragraph
    paragraph = slides.Paragraph()
    paragraph.text = "Welcome to Aspose.Slides"

    # Setting paragraph bullet style and image
    paragraph.paragraph_format.bullet.type = slides.BulletType.PICTURE
    paragraph.paragraph_format.bullet.picture.image = ippxImage

    # Setting Bullet Height
    paragraph.paragraph_format.bullet.height = 100

    # Adding Paragraph to text frame
    textFrame.paragraphs.add(paragraph)

    # Writing the presentation as a PPTX file
    presentation.save(outDir + "text_picture_bullets_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ManageParagraphPictureBulletsInPPT