import aspose.slides as slides


def get_rectangular_coordinates_of_paragraph(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "open_shapes.pptx") as presentation:
        shape = presentation.slides[0].shapes[0]
        text_frame = shape.text_frame
        rect = text_frame.paragraphs[0].get_rect()
        return rect
