import aspose.pydrawing as drawing
import aspose.slides as slides


def paragraph_bullets(global_opts):
    # Creating a presentation instance
    with slides.Presentation() as pres:
        # Accessing the first slide
        slide = pres.slides[0]

        # Adding and accessing Autoshape
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 400, 200)

        # Accessing the text frame of created autoshape
        text_frame = auto_shape.text_frame

        # Removing the default existing paragraph
        text_frame.paragraphs.remove_at(0)

        # Creating a paragraph
        para = slides.Paragraph()

        # Setting paragraph bullet style and symbol
        para.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para.paragraph_format.bullet.char = chr(8226)

        # Setting paragraph text
        para.text = "Welcome to Aspose.Slides"

        # Setting bullet indent
        para.paragraph_format.indent = 25

        # Setting bullet color
        para.paragraph_format.bullet.color.color_type = slides.ColorType.RGB
        para.paragraph_format.bullet.color.color = drawing.Color.black
        # set is_bullet_hard_color to True to use own bullet color
        para.paragraph_format.bullet.is_bullet_hard_color = slides.NullableBool.TRUE

        # Setting Bullet Height
        para.paragraph_format.bullet.height = 100

        # Adding Paragraph to text frame
        text_frame.paragraphs.add(para)

        # Creating second paragraph
        para2 = slides.Paragraph()

        # Setting paragraph bullet type and style
        para2.paragraph_format.bullet.type = slides.BulletType.NUMBERED
        para2.paragraph_format.bullet.numbered_bullet_style = slides.NumberedBulletStyle.BULLET_CIRCLE_NUM_WD_BLACK_PLAIN

        # Adding paragraph text
        para2.text = "This is numbered bullet"

        # Setting bullet indent
        para2.paragraph_format.indent = 25

        para2.paragraph_format.bullet.color.color_type = slides.ColorType.RGB
        para2.paragraph_format.bullet.color.color = drawing.Color.black
        # set is_bullet_hard_color to True to use own bullet color
        para2.paragraph_format.bullet.is_bullet_hard_color = slides.NullableBool.TRUE

        # Setting Bullet Height
        para2.paragraph_format.bullet.height = 100

        # Adding Paragraph to text frame
        text_frame.paragraphs.add(para2)

        # Writing the presentation as a PPTX file
        pres.save(global_opts.out_dir + "text_paragraph_bullets_out.pptx", slides.export.SaveFormat.PPTX)
