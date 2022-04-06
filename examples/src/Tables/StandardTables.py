import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:StandardTables
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX file
with slides.Presentation() as pres:
    # Access first slide
    slide = pres.slides[0]

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

    #Write PPTX to Disk
    pres.save(outDir + "tables_add_standard_table_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:StandardTables

