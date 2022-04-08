import aspose.slides as slides


#ExStart:TableWithCellBorders
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX file
with slides.Presentation() as pres:
    # Access first slide
    sld = pres.slides[0]

    # Define columns with widths and rows with heights
    dblCols = [ 50, 50, 50, 50 ]
    dblRows = [ 50, 30, 30, 30, 30 ]

    # Add table shape to slide

    # Add table shape to slide
    tbl = sld.shapes.add_table(100, 50, dblCols, dblRows)

    # Set border format for each cell
    for row in tbl.rows:
        for cell in row:
            cell.cell_format.border_top.fill_format.fill_type = slides.FillType.NO_FILL
            cell.cell_format.border_bottom.fill_format.fill_type = slides.FillType.NO_FILL
            cell.cell_format.border_left.fill_format.fill_type = slides.FillType.NO_FILL
            cell.cell_format.border_right.fill_format.fill_type = slides.FillType.NO_FILL

    #Write PPTX to Disk
    pres.save(outDir + "table_border_no_fill_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:TableWithCellBorders