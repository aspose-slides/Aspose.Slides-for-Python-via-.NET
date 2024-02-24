import aspose.slides as slides


def number_lines_in_paragraph():
    with slides.Presentation() as presentation:
        slide = presentation.slides[0]
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 150, 75, 150, 50)
        para = auto_shape.text_frame.paragraphs[0]
        portion = para.portions[0]
        portion.text = "Aspose Paragraph GetLinesCount() Example"
        
        print("Lines Count =", para.get_lines_count())
        
        # Change shape width
        auto_shape.width = 250
        print("Lines Count after changing shape width =", para.get_lines_count())
