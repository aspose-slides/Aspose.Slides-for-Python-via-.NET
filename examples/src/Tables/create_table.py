import aspose.slides as slides


def create_table(global_opts):
    with slides.Presentation() as pres:
        # Access first slide
        slide = pres.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [50, 50, 50]
        dbl_rows = [50, 30, 30, 30, 30]

        # Add a table
        table = slide.shapes.add_table(50, 50, dbl_cols, dbl_rows)

        # Set border format for each cell
        for row in table.rows:
            for cell in row:
                # Get text frame of each cell
                tf = cell.text_frame
                # Add some text
                tf.text = "T" + str(cell.first_row_index) + str(cell.first_column_index)
                # Set font size of 10
                tf.paragraphs[0].portions[0].portion_format.font_height = 10
                tf.paragraphs[0].paragraph_format.bullet.type = slides.BulletType.NONE

        # Write the presentation to the disk
        pres.save(global_opts.out_dir + "tables_create_table_out.ppt", slides.export.SaveFormat.PPT)
