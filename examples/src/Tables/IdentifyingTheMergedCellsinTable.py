import aspose.pydrawing as drawing
import aspose.slides as slides


# ExStart:IdentifyingTheMergedCellsinTable
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"


with slides.Presentation(dataDir + "tables.pptx") as pres:
    table = pres.slides[0].shapes[0] # assuming that Slide#0.Shape#0 is a table
    for i in range(len(table.rows)):
        for j in range(len(table.rows[i])):
            currentCell = table.rows[i][j]
            if currentCell.is_merged_cell:
                print("Cell {0}{1} is a part of merged cell with row_span={2} and col_span={3} starting from Cell {4}{5}.".format(
                                    i, j, currentCell.row_span, currentCell.col_span, currentCell.first_row_index, currentCell.first_column_index))

# ExEnd:IdentifyingTheMergedCellsinTable

