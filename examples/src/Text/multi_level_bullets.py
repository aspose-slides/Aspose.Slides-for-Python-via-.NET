import aspose.pydrawing as drawing
import aspose.slides as slides


def multi_level_bullets(global_opts):
    # Creating a presentation instance
    with slides.Presentation() as pres:
        # Accessing the first slide
        slide = pres.slides[0]
    
        # Adding and accessing Autoshape
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 400, 200)

        # Accessing the text frame of created autoshape
        text = auto_shape.add_text_frame("")
    
        # clearing default paragraph
        text.paragraphs.clear()

        # Adding first paragraph
        para1 = slides.Paragraph()
        para1.text = "Content"
        para1.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para1.paragraph_format.bullet.char = chr(8226)
        para1.paragraph_format.default_portion_format.fill_format.fill_type = slides.FillType.SOLID
        para1.paragraph_format.default_portion_format.fill_format.solid_fill_color.color = drawing.Color.black

        # Setting bullet level
        para1.paragraph_format.depth = 0

        # Adding second paragraph
        para2 = slides.Paragraph()
        para2.text = "Second Level"
        para2.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para2.paragraph_format.bullet.char = '-'
        para2.paragraph_format.default_portion_format.fill_format.fill_type = slides.FillType.SOLID
        para2.paragraph_format.default_portion_format.fill_format.solid_fill_color.color = drawing.Color.black

        # Setting bullet level
        para2.paragraph_format.depth = 1

        # Adding third paragraph
        para3 = slides.Paragraph()
        para3.text = "Third Level"
        para3.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para3.paragraph_format.bullet.char = chr(8226)
        para3.paragraph_format.default_portion_format.fill_format.fill_type = slides.FillType.SOLID
        para3.paragraph_format.default_portion_format.fill_format.solid_fill_color.color = drawing.Color.black

        # Setting bullet level
        para3.paragraph_format.depth = 2

        # Adding fourth paragraph
        para4 = slides.Paragraph()
        para4.text = "Fourth Level"
        para4.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para4.paragraph_format.bullet.char = '-'
        para4.paragraph_format.default_portion_format.fill_format.fill_type = slides.FillType.SOLID
        para4.paragraph_format.default_portion_format.fill_format.solid_fill_color.color = drawing.Color.black

        # Setting bullet level
        para4.paragraph_format.depth = 3

        # Adding paragraphs to collection
        text.paragraphs.add(para1)
        text.paragraphs.add(para2)
        text.paragraphs.add(para3)
        text.paragraphs.add(para4)

        # Writing the presentation as a PPTX file
        pres.save(global_opts.out_dir + "text_multilevel_bullet_out.pptx", slides.export.SaveFormat.PPTX)
