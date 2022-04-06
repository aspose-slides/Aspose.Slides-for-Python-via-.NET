import aspose.slides as slides
import aspose.pydrawing as drawing


#ExStart:CreateATableFromScratchInASlide

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class that represents PPTX file
with slides.Presentation() as pres:

    # Access first slide
    sld = pres.slides[0]

    # Define columns with widths and rows with heights
    dblCols = [ 50, 50, 50 ]
    dblRows = [ 50, 30, 30, 30, 30 ]

    # Add table shape to slide
    tbl = sld.shapes.add_table(100, 50, dblCols, dblRows)

    # Set border format for each cell
    for row in range(len(tbl.rows)):
        for cell in range(len(tbl.rows[row])):
            tbl.rows[row][cell].cell_format.border_top.fill_format.fill_type = slides.FillType.SOLID
            tbl.rows[row][cell].cell_format.border_top.fill_format.solid_fill_color.color = drawing.Color.red
            tbl.rows[row][cell].cell_format.border_top.width = 5

            tbl.rows[row][cell].cell_format.border_bottom.fill_format.fill_type = (slides.FillType.SOLID)
            tbl.rows[row][cell].cell_format.border_bottom.fill_format.solid_fill_color.color= drawing.Color.red
            tbl.rows[row][cell].cell_format.border_bottom.width =5

            tbl.rows[row][cell].cell_format.border_left.fill_format.fill_type = slides.FillType.SOLID
            tbl.rows[row][cell].cell_format.border_left.fill_format.solid_fill_color.color =drawing.Color.red
            tbl.rows[row][cell].cell_format.border_left.width = 5

            tbl.rows[row][cell].cell_format.border_right.fill_format.fill_type = slides.FillType.SOLID
            tbl.rows[row][cell].cell_format.border_right.fill_format.solid_fill_color.color = drawing.Color.red
            tbl.rows[row][cell].cell_format.border_right.width = 5
    # Merge cells 1 & 2 of row 1
    tbl.merge_cells(tbl.rows[0][0], tbl.rows[1][1], False)

    # Add text to the merged cell
    tbl.rows[0][0].text_frame.text = "Merged Cells"

    # Save PPTX to Disk
    pres.save(outDir + "tables_create_new_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CreateATableFromScratchInASlide
