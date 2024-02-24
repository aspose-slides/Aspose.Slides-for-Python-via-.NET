import aspose.slides as slides


def add_column_in_text_boxes(global_opts):
    with slides.Presentation() as presentation:
        # Get the first slide of presentation
        slide = presentation.slides[0]

        # Add an AutoShape of Rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)

        # Add TextFrame to the Rectangle
        shape.add_text_frame("All these columns are limited to be within a single text container -- " +
        "you can add or delete text and the new or remaining text automatically adjusts " +
        "itself to flow within the container. You cannot have text flow from one container " +
        "to other though -- we told you PowerPoint's column options for text are limited!")

        # Get text format of TextFrame
        text_frame_format = shape.text_frame.text_frame_format

        # Specify number of columns in TextFrame
        text_frame_format.column_count = 3

        # Specify spacing between columns
        text_frame_format.column_spacing = 10

        # Save created presentation
        presentation.save(global_opts.out_dir + "text_add_text_frame_out.pptx", slides.export.SaveFormat.PPTX)
