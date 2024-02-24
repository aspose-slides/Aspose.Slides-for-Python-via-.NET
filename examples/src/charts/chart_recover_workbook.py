import aspose.slides as slides


def charts_recover_workbook(global_opts):
    """
    This example demonstrates how to recover data from chart cache
    if the data source of the chart is an external workbook and it's not available.
    """

    load_options = slides.LoadOptions()
    load_options.spreadsheet_options.recover_workbook_from_chart_cache = True

    with slides.Presentation(global_opts.data_dir + "charts_with_external_workbook.pptx", load_options) as pres:
        chart = pres.slides[0].shapes[0]
        wb = chart.chart_data.chart_data_workbook

        pres.save(global_opts.out_dir + "charts_recover_workbook_out.pptx", slides.export.SaveFormat.PPTX)
