import aspose.slides as slides


def table_with_cell_borders(global_opts):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation() as pres:
        # Access first slide
        slide = pres.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [50, 50, 50, 50]
        dbl_rows = [50, 30, 30, 30, 30]

        # Add table shape to slide
        table = slide.shapes.add_table(100, 50, dbl_cols, dbl_rows)

        # Set border format for each cell
        for row in table.rows:
            for cell in row:
                cell.cell_format.border_top.fill_format.fill_type = slides.FillType.NO_FILL
                cell.cell_format.border_bottom.fill_format.fill_type = slides.FillType.NO_FILL
                cell.cell_format.border_left.fill_format.fill_type = slides.FillType.NO_FILL
                cell.cell_format.border_right.fill_format.fill_type = slides.FillType.NO_FILL

        # Write PPTX to Disk
        pres.save(global_opts.out_dir + "table_border_no_fill_out.pptx", slides.export.SaveFormat.PPTX)
