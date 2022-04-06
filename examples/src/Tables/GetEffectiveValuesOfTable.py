import aspose.slides as slides


#ExStart:GetEffectiveValuesOfTable

# The path to the documents directory.

dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "tables.pptx") as pres:
    tbl = pres.slides[0].shapes[0]
    tableFormatEffective = tbl.table_format.get_effective()
    rowFormatEffective = tbl.rows[0].row_format.get_effective()
    columnFormatEffective = tbl.columns[0].column_format.get_effective()
    cellFormatEffective = tbl.rows[0][0].cell_format.get_effective()

    tableFillFormatEffective = tableFormatEffective.fill_format
    rowFillFormatEffective = rowFormatEffective.fill_format
    columnFillFormatEffective = columnFormatEffective.fill_format
    cellFillFormatEffective = cellFormatEffective.fill_format
    
#ExEnd:GetEffectiveValuesOfTable
