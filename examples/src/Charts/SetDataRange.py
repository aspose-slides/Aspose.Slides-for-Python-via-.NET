import aspose.slides as slides

def charts_set_data_range():
    #ExStart:SetDataRange
    # The path to the documents directory.
    outDir = "./examples/out/"
    dataDir = "./examples/data/"

    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation(dataDir + "charts_with_external_workbook.pptx") as presentation:
        # Access first slideMarker and add chart with default data
        slide = presentation.slides[0]
        chart = slide.shapes[0]
        chart.chart_data.set_range("Sheet1!A1:B4")
        presentation.save(outDir + "charts_set_data_range_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:SetDataRange