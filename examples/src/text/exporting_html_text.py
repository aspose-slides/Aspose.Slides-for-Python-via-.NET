import aspose.slides as slides


def exporting_html_text(global_opts):
    # Load the presentation file
    with slides.Presentation(global_opts.data_dir + "text_export_text_frame_to_html.pptx") as pres:
        # Access the default first slide of presentation
        slide = pres.slides[0]

        # Desired index
        index = 0

        # Accessing the added shape
        auto_shape = slide.shapes[index]

        with open(global_opts.out_dir + "text_export_text_frame_to_html_out.html", "wt") as sw:
            data = auto_shape.text_frame.paragraphs.export_to_html(0, auto_shape.text_frame.paragraphs.count, None)
            sw.write(data)
