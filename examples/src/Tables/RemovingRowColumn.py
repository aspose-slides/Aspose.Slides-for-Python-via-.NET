import aspose.slides as slides


#ExStart:RemovingRowColumn
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"


with slides.Presentation() as pres:
    slide = pres.slides[0]
    colWidth = [ 100, 50, 30 ]
    rowHeight = [ 30, 50, 30 ]

    table = slide.shapes.add_table(100, 100, colWidth, rowHeight)
    table.rows.remove_at(1, False)
    table.columns.remove_at(1, False)
    pres.save(outDir + "tables_remove_at_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:RemovingRowColumn