import aspose.slides as slides


def render_paragraph_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "HelloWorld.pptx") as pres:
        slide = pres.slides[0]

        shape_index = 0
        for shape in slide.shapes:
            shape_index += 1

            if not isinstance(shape, slides.AutoShape) or shape.text_frame is None:
                continue

            paragraph_index = 0
            for paragraph in shape.text_frame.paragraphs:
                paragraph_index += 1
                out_file_name = global_opts.out_dir + "shape{0}_paragraph{1}.png".format(shape_index, paragraph_index)

                # Render the paragraph as an image with 2x scaling
                with paragraph.get_image(2, 2) as paragraph_image:
                    if paragraph_image is not None:
                        paragraph_image.save(out_file_name)
