import aspose.slides as slides


def line_spacing(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "text_fonts.pptx") as presentation:
        # Obtain a slide's reference by its index
        slide = presentation.slides[0]

        # Access the TextFrame
        tf1 = slide.shapes[0].text_frame

        # Access the Paragraph
        para1 = tf1.paragraphs[0]

        # Set properties of Paragraph
        para1.paragraph_format.space_within = 80
        para1.paragraph_format.space_before = 40
        para1.paragraph_format.space_after = 40

        # Save Presentation
        presentation.save(global_opts.out_dir + "text_line_spacing_out.pptx", slides.export.SaveFormat.PPTX)
