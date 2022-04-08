import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:CellSplit
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX file
with slides.Presentation() as presentation:
    # Access first slide
    slide = presentation.slides[0]

    # Define columns with widths and rows with heights
    dblCols = [ 70, 70, 70, 70 ]
    dblRows = [ 70, 70, 70, 70 ]

    # Add table shape to slide
    table = slide.shapes.add_table(100, 50, dblCols, dblRows)

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

    # split cell (1, 1). 
    table.rows[1][1].split_by_width(table.rows[2][1].width / 2)

    #Write PPTX to Disk
    presentation.save(outDir + "tables_cell_split_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CellSplit

