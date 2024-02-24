import aspose.pydrawing as drawing
import aspose.slides as slides


def manage_paragraph_picture_bullets_in_ppt(global_opts):
    with slides.Presentation() as presentation:
        # Accessing the first slide
        slide = presentation.slides[0]

        # Instantiate the image for bullets
        image = drawing.Bitmap(global_opts.data_dir + "bullets.png")
        ippx_image = presentation.images.add_image(image)

        # Adding and accessing Autoshape
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 400, 200)

        # Accessing the text frame of created autoshape
        text_frame = auto_shape.text_frame

        # Removing the default existing paragraph
        text_frame.paragraphs.remove_at(0)

        # Creating new paragraph
        paragraph = slides.Paragraph()
        paragraph.text = "Welcome to Aspose.Slides"

        # Setting paragraph bullet style and image
        paragraph.paragraph_format.bullet.type = slides.BulletType.PICTURE
        paragraph.paragraph_format.bullet.picture.image = ippx_image

        # Setting Bullet Height
        paragraph.paragraph_format.bullet.height = 100

        # Adding Paragraph to text frame
        text_frame.paragraphs.add(paragraph)

        # Writing the presentation as a PPTX file
        presentation.save(global_opts.out_dir + "text_picture_bullets_out.pptx", slides.export.SaveFormat.PPTX)
