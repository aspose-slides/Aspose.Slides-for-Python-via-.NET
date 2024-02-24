import aspose.slides as slides


def adding_superscript_and_subscript_text_in_text_frame(global_opts):
    with slides.Presentation() as presentation:
        # Get slide
        slide = presentation.slides[0]

        # Create text box
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 200, 100)
        text_frame = shape.text_frame
        text_frame.paragraphs.clear()

        # Create paragraph for superscript text
        super_para = slides.Paragraph()

        # Create portion with usual text
        portion1 = slides.Portion()
        portion1.text = "SlideTitle"
        super_para.portions.add(portion1)

        # Create portion with superscript text
        super_portion = slides.Portion()
        super_portion.portion_format.escapement = 30
        super_portion.text = "TM"
        super_para.portions.add(super_portion)

        # Create paragraph for subscript text
        paragraph2 = slides.Paragraph()

        # Create portion with usual text
        portion2 = slides.Portion()
        portion2.text = "a"
        paragraph2.portions.add(portion2)

        # Create portion with subscript text
        sub_portion = slides.Portion()
        sub_portion.portion_format.escapement = -25
        sub_portion.text = "i"
        paragraph2.portions.add(sub_portion)

        # Add paragraphs to text box
        text_frame.paragraphs.add(super_para)
        text_frame.paragraphs.add(paragraph2)

        presentation.save(global_opts.out_dir + "text_add_superscript_and_subscript_out.pptx", slides.export.SaveFormat.PPTX)
