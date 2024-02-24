import aspose.slides as slides


def set_first_row_as_header(global_opts):
    # Instantiate Presentation class that represents PPTX
    with slides.Presentation(global_opts.data_dir + "tables.pptx") as pres:
        # Access the first slide
        slide = pres.slides[0]

        # Iterate through the shapes and set a reference to the table found
        for shape in slide.shapes:
            if type(shape) is slides.Table:
                # Set the first row of a table as header with a special formatting.
                shape.first_row = True

        pres.save(global_opts.out_dir + "tables_first_row_as_header_out.pptx", slides.export.SaveFormat.PPTX)
