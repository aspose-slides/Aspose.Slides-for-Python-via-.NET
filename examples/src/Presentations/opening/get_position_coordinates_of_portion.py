import aspose.slides as slides


def get_position_coordinates_of_portion(global_opts):
    with slides.Presentation(global_opts.data_dir + "open_shapes.pptx") as presentation:
        shape = presentation.slides[0].shapes[0]
        text_frame = shape.text_frame

        for paragraph in text_frame.paragraphs:
            for portion in paragraph.portions:
                point = portion.get_coordinates()
                print("Coordinates X = {0} Y = {1}".format(point.x, point.y))
