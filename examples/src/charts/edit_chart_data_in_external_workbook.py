import aspose.slides as slides


def charts_edit_chart_data_in_external_workbook(global_opts):
    with slides.Presentation(global_opts.data_dir + "charts_with_external_workbook.pptx") as pres:
        chart = pres.slides[0].shapes[0]
        chart_data = chart.chart_data
        chart_data.series[0].data_points[0].value.as_cell.value = 100
        pres.save(global_opts.out_dir + "charts_edit_chartdata_in_external_workbook_out.pptx", slides.export.SaveFormat.PPTX)
