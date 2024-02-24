import aspose.slides as slides


def text_formatting_inside_table_row(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "tables.pptx") as presentation:
        # let's say that the first shape on the first slide is a table
        table = presentation.slides[0].shapes[0]

        # setting first row cells' font height
        portion_format = slides.PortionFormat()
        portion_format.font_height = 25
        table.rows[0].set_text_format(portion_format)

        # setting first row cells' text alignment and right margin in one call
        paragraph_format = slides.ParagraphFormat()
        paragraph_format.alignment = slides.TextAlignment.RIGHT
        paragraph_format.margin_right = 20
        table.rows[0].set_text_format(paragraph_format)

        # setting second row cells' text vertical type
        text_frame_format = slides.TextFrameFormat()
        text_frame_format.text_vertical_type = slides.TextVerticalType.VERTICAL
        table.rows[1].set_text_format(text_frame_format)

        presentation.save(global_opts.out_dir + "tables_text_format_inside_row_out.pptx", slides.export.SaveFormat.PPTX)
