import aspose.slides as slides


def table_from_scratch(global_opts):
    # Instantiate Presentation class that represents PPTX
    with slides.Presentation(global_opts.data_dir + "tables_update.pptx") as presentation:
        # Access the first slide
        slide = presentation.slides[0]

        # Iterate through the shapes and set a reference to the table found
        for shape in slide.shapes:
            if type(shape) is slides.Table:
                # Set the text of the first column of second row
                shape.rows[0][1].text_frame.text = "New"

        # Write the PPTX to Disk
        presentation.save(global_opts.out_dir + "tables_update_table_out.pptx", slides.export.SaveFormat.PPTX)
