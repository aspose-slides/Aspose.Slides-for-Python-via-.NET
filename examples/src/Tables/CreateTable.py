import aspose.slides as slides


#ExStart:CreateTable

dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    #Access first slide
    sld = pres.slides[0]

    #Define columns with widths and rows with heights
    dblCols = [ 50, 50, 50 ]
    dblRows = [ 50, 30, 30, 30, 30 ]

    #Add a table
    tbl = sld.shapes.add_table(50, 50, dblCols, dblRows)

    #Set border format for each cell
    for row in tbl.rows:
        for cell in row:
            #Get text frame of each cell
            tf = cell.text_frame
            #Add some text
            tf.text = "T" + str(cell.first_row_index) + str(cell.first_column_index)
            #Set font size of 10
            tf.paragraphs[0].portions[0].portion_format.font_height = 10
            tf.paragraphs[0].paragraph_format.bullet.type = slides.BulletType.NONE

    #Write the presentation to the disk
    pres.save(outDir + "tables_create_table_out.ppt", slides.export.SaveFormat.PPT)
#ExEnd:CreateTable
