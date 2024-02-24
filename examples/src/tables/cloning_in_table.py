import aspose.slides as slides


def cloning_in_table(global_opts):
    # Instantiate presentation class that represents PPTX file
    with slides.Presentation() as presentation:
        # Access first slide
        slide = presentation.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [50, 50, 50]
        dbl_rows = [50, 30, 30, 30, 30]

        # Add table shape to slide
        table = slide.shapes.add_table(100, 50, dbl_cols, dbl_rows)

        # Add text to the row 1 cell 1
        table.rows[0][0].text_frame.text = "Row 1 Cell 1"

        # Add text to the row 1 cell 2
        table.rows[1][0].text_frame.text = "Row 1 Cell 2"

        # Clone Row 1 at end of table
        table.rows.add_clone(table.rows[0], False)

        # Add text to the row 2 cell 1
        table.rows[0][1].text_frame.text = "Row 2 Cell 1"

        # Add text to the row 2 cell 2
        table.rows[1][1].text_frame.text = "Row 2 Cell 2"

        # Clone Row 2 as 4th row of table
        table.rows.insert_clone(3, table.rows[1], False)

        # Cloning first column at end
        table.columns.add_clone(table.columns[0], False)

        # Cloning 2nd column at 4th column index
        table.columns.insert_clone(3, table.columns[1], False)

        # Write PPTX to Disk
        presentation.save(global_opts.out_dir + "tables_clone_out.pptx", slides.export.SaveFormat.PPTX)
