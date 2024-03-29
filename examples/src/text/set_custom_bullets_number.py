﻿import aspose.slides as slides


def set_custom_bullets_number(global_opts):
    with slides.Presentation() as presentation:
        shape = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 200, 400, 200)

        # Accessing the text frame of created autoshape
        text_frame = shape.text_frame

        # Removing the default existing paragraph
        text_frame.paragraphs.remove_at(0)

        # First list
        paragraph1 = slides.Paragraph()
        paragraph1.text = "bullet 2"
        paragraph1.paragraph_format.depth = 4
        paragraph1.paragraph_format.bullet.numbered_bullet_start_with = 2
        paragraph1.paragraph_format.bullet.type = slides.BulletType.NUMBERED
        text_frame.paragraphs.add(paragraph1)

        paragraph2 = slides.Paragraph()
        paragraph2.text = "bullet 3"
        paragraph2.paragraph_format.depth = 4
        paragraph2.paragraph_format.bullet.numbered_bullet_start_with = 3
        paragraph2.paragraph_format.bullet.type = slides.BulletType.NUMBERED
        text_frame.paragraphs.add(paragraph2)

        paragraph5 = slides.Paragraph()
        paragraph5.text = "bullet 7"
        paragraph5.paragraph_format.depth = 4
        paragraph5.paragraph_format.bullet.numbered_bullet_start_with = 7
        paragraph5.paragraph_format.bullet.type = slides.BulletType.NUMBERED
        text_frame.paragraphs.add(paragraph5)

        presentation.save(global_opts.out_dir + "text_set_custom_bullets_number_out.pptx",
                          slides.export.SaveFormat.PPTX)
