import aspose.slides as slides


def add_columns_in_text_frame(global_opts):
    with slides.Presentation() as pres:
        shape1 = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)
        text_frame_format = shape1.text_frame.text_frame_format

        text_frame_format.column_count = 2
        shape1.text_frame.text = "All these columns are limited to be within a single text container -- " + \
                                 "you can add or delete text and the new or remaining text automatically adjusts " + \
                                 "itself to flow within the container. You cannot have text flow from one container " + \
                                 "to other though -- we told you PowerPoint's column options for text are limited!"
        pres.save(global_opts.out_dir + "text_add_columns_out.pptx", slides.export.SaveFormat.PPTX)
