import aspose.slides as slides


def charts_data_source_type_property_added():
    #ExStart:DataSourceTypePropertyAdded
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "charts_with_external_workbook.pptx") as pres:
        slide = pres.slides[0]
        chart = slide.shapes[0]
        sourceType = chart.chart_data.data_source_type
        if sourceType == slides.charts.ChartDataSourceType.EXTERNAL_WORKBOOK:
            path = chart.chart_data.external_workbook_path
            print(path)

        # Saving presentation
        pres.save(dataDir + "charts_data_source_type_property_added_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:DataSourceTypePropertyAdded