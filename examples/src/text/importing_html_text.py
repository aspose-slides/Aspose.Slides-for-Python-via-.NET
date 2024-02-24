import aspose.slides as slides


def importing_html_text(global_opts):
    # Create Empty presentation instance
    with slides.Presentation() as pres:
        # Access the default first slide of presentation
        slide = pres.slides[0]

        # Adding the AutoShape to accomodate the HTML content
        auto_shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 10, 10, pres.slide_size.size.width - 20, pres.slide_size.size.height - 10)

        auto_shape.fill_format.fill_type = slides.FillType.NO_FILL

        # Adding text frame to the shape
        auto_shape.add_text_frame("")

        # Clearing all paragraphs in added text frame
        auto_shape.text_frame.paragraphs.clear()

        # Loading the HTML file using stream reader
        with open(global_opts.data_dir + "file.html", "rt") as stream:
            data = stream.read()

        # Adding text from HTML stream reader in text frame
        auto_shape.text_frame.paragraphs.add_from_html(data)

        # Saving Presentation
        pres.save(global_opts.out_dir + "text_import_from_html_out.pptx", slides.export.SaveFormat.PPTX)
