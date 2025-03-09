import aspose.slides as slides


def split_text_by_columns_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "MultiColumnText.pptx") as pres:
        # Get the first shape on the slide
        shape = pres.slides[0].shapes[0]
        # Get textFrame
        text_frame = shape.text_frame
        # Split the text frame content into columns
        columns_text = text_frame.split_text_by_columns()
        # Print each column's text to the console
        for column in columns_text:
            print(column)
