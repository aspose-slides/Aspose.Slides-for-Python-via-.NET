import aspose.slides as slides
import aspose.pydrawing as drawing


def create_table_from_scratch_in_slide(global_opts):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation() as pres:
        # Access first slide
        slide = pres.slides[0]

        # Define columns with widths and rows with heights
        dbl_cols = [50, 50, 50]
        dbl_rows = [50, 30, 30, 30, 30]

        # Add table shape to slide
        table = slide.shapes.add_table(100, 50, dbl_cols, dbl_rows)

        # Set border format for each cell
        for row in range(len(table.rows)):
            for cell in range(len(table.rows[row])):
                table.rows[row][cell].cell_format.border_top.fill_format.fill_type = slides.FillType.SOLID
                table.rows[row][cell].cell_format.border_top.fill_format.solid_fill_color.color = drawing.Color.red
                table.rows[row][cell].cell_format.border_top.width = 5

                table.rows[row][cell].cell_format.border_bottom.fill_format.fill_type = slides.FillType.SOLID
                table.rows[row][cell].cell_format.border_bottom.fill_format.solid_fill_color.color = drawing.Color.red
                table.rows[row][cell].cell_format.border_bottom.width = 5

                table.rows[row][cell].cell_format.border_left.fill_format.fill_type = slides.FillType.SOLID
                table.rows[row][cell].cell_format.border_left.fill_format.solid_fill_color.color = drawing.Color.red
                table.rows[row][cell].cell_format.border_left.width = 5

                table.rows[row][cell].cell_format.border_right.fill_format.fill_type = slides.FillType.SOLID
                table.rows[row][cell].cell_format.border_right.fill_format.solid_fill_color.color = drawing.Color.red
                table.rows[row][cell].cell_format.border_right.width = 5

        # Merge cells 1 & 2 of row 1
        table.merge_cells(table.rows[0][0], table.rows[1][1], False)

        # Add text to the merged cell
        table.rows[0][0].text_frame.text = "Merged Cells"

        # Save PPTX to Disk
        pres.save(global_opts.out_dir + "tables_create_new_out.pptx", slides.export.SaveFormat.PPTX)
