import aspose.slides as slides

def charts_edit_chartdata_in_external_workbook():
    # Pay attention the path to external workbook is hardly saved in the presentation
    # so please copy file charts_external_workbook.xlsx from Data/Chart directory D:\Aspose.Slides\Aspose.Slides-for-.NET-master\Examples\Data\Charts\ before run the example

    #ExStart:EditChartDatainExternalWorkbook
    # The path to the documents directory.

    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "charts_with_external_workbook.pptx") as pres:
        chart = pres.slides[0].shapes[0]
        chartData = chart.chart_data
                        

        chartData.series[0].data_points[0].value.as_cell.value = 100
        pres.save(outDir + "charts_edit_chartdata_in_external_workbook_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:EditChartDatainExternalWorkbook

