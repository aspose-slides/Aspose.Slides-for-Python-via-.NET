import aspose.slides as slides


def paragraph_indent(global_opts):
    # Instantiate Presentation Class
    with slides.Presentation() as pres:
        # Get first slide
        slide = pres.slides[0]

        # Add a Rectangle Shape
        rect = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 500, 150)

        # Add TextFrame to the Rectangle
        tf = rect.add_text_frame("This is first line \rThis is second line \rThis is third line")

        # Set the text to fit the shape
        tf.text_frame_format.autofit_type = slides.TextAutofitType.SHAPE

        # Hide the lines of the Rectangle
        rect.line_format.fill_format.fill_type = slides.FillType.SOLID

        # Get first Paragraph in the TextFrame and set its Indent
        para1 = tf.paragraphs[0]

        # Setting paragraph bullet style and symbol
        para1.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para1.paragraph_format.bullet.char = chr(8226)
        para1.paragraph_format.alignment = slides.TextAlignment.LEFT

        para1.paragraph_format.depth = 2
        para1.paragraph_format.indent = 30

        # Get second Paragraph in the TextFrame and set its Indent
        para2 = tf.paragraphs[1]
        para2.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para2.paragraph_format.bullet.char = chr(8226)
        para2.paragraph_format.alignment = slides.TextAlignment.LEFT
        para2.paragraph_format.depth = 2
        para2.paragraph_format.indent = 40

        # Get third Paragraph in the TextFrame and set its Indent
        para3 = tf.paragraphs[2]
        para3.paragraph_format.bullet.type = slides.BulletType.SYMBOL
        para3.paragraph_format.bullet.char = chr(8226)
        para3.paragraph_format.alignment = slides.TextAlignment.LEFT
        para3.paragraph_format.depth = 2
        para3.paragraph_format.indent = 50

        # Write the Presentation to disk
        pres.save(global_opts.out_dir + "text_paragraph_indent_out.pptx", slides.export.SaveFormat.PPTX)
