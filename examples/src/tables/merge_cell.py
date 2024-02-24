import aspose.pydrawing as drawing
import aspose.slides as slides


def merge_cell(global_opts):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation() as presentation:
        # Access first slide
        slide = presentation.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [70, 70, 70, 70]
        dbl_rows = [70, 70, 70, 70]

        # Add table shape to slide
        table = slide.shapes.add_table(100, 50, dbl_cols, dbl_rows)

        # Set border format for each cell
        for row in table.rows:
            for cell in row:
                cell.cell_format.border_top.fill_format.fill_type = slides.FillType.SOLID
                cell.cell_format.border_top.fill_format.solid_fill_color.color = drawing.Color.red
                cell.cell_format.border_top.width = 5

                cell.cell_format.border_bottom.fill_format.fill_type = slides.FillType.SOLID
                cell.cell_format.border_bottom.fill_format.solid_fill_color.color = drawing.Color.red
                cell.cell_format.border_bottom.width = 5

                cell.cell_format.border_left.fill_format.fill_type = slides.FillType.SOLID
                cell.cell_format.border_left.fill_format.solid_fill_color.color = drawing.Color.red
                cell.cell_format.border_left.width = 5

                cell.cell_format.border_right.fill_format.fill_type = slides.FillType.SOLID
                cell.cell_format.border_right.fill_format.solid_fill_color.color = drawing.Color.red
                cell.cell_format.border_right.width = 5

        # Merging cells (1, 1) x (2, 1)
        table.merge_cells(table.rows[1][1], table.rows[2][1], False)

        # Merging cells (1, 2) x (2, 2)
        table.merge_cells(table.rows[1][2], table.rows[2][2], False)

        # Merging cells (1, 2) x (2, 2)
        table.merge_cells(table.rows[1][1], table.rows[1][2], True)

        # Write PPTX to Disk
        presentation.save(global_opts.out_dir + "tables_merge_cells_out.pptx", slides.export.SaveFormat.PPTX)
