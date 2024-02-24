import aspose.slides as slides


def apply_inner_shadow(global_opts):
    # Instantiate Presentation
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add an AutoShape of Rectangle type
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 150, 50)

        # Add TextFrame to the Rectangle
        auto_shape.add_text_frame(" ")

        # Accessing the text frame
        text_frame = auto_shape.text_frame

        # Create the Paragraph object for text frame
        para = text_frame.paragraphs[0]

        # Create Portion object for paragraph
        portion = para.portions[0]

        # Set Text
        portion.text = "Aspose TextBox"

        # Save the presentation to disk
        pres.save(global_opts.out_dir + "text_add_textbox_out.pptx", slides.export.SaveFormat.PPTX)
