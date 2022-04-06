import aspose.pydrawing as drawing
import aspose.slides as slides


#ExStart:CloningInTable
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate presentation class that represents PPTX file
with slides.Presentation() as presentation:
    # Access first slide
    sld = presentation.slides[0]

    # Define columns with widths and rows with heights
    dblCols = [ 50, 50, 50 ]
    dblRows = [ 50, 30, 30, 30, 30 ]

    # Add table shape to slide
    table = sld.shapes.add_table(100, 50, dblCols, dblRows)


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
    table.rows.insert_clone(3,table.rows[1], False)

    #Cloning first column at end
    table.columns.add_clone(table.columns[0], False)

    #Cloning 2nd column at 4th column index
    table.columns.insert_clone(3,table.columns[1], False)
    

    # Write PPTX to Disk
    presentation.save(outDir + "tables_clone_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CloningInTable