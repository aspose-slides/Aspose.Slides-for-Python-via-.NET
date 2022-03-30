import aspose.slides as slides


"""
This example demonstrates how to recover data from chart cache 
if the data source of the chart is an external workbook and it's not available.
"""

def charts_recover_workbook():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    lo = slides.LoadOptions()
    lo.spreadsheet_options.recover_workbook_from_chart_cache = True

    with slides.Presentation(dataDir + "ExternalWB.pptx", lo) as pres:
        chart = pres.slides[0].shapes[0]
        wb = chart.chart_data.chart_data_workbook

        pres.save(outDir + "charts_ExternalWB_out.pptx", slides.export.SaveFormat.PPTX)
