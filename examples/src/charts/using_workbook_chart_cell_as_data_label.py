import aspose.slides as slides


def charts_workbook_as_datalabel(global_opts):
    lbl0 = "Label 0 cell value"
    lbl1 = "Label 1 cell value"
    lbl2 = "Label 2 cell value"

    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "charts_workbook_as_datalabel.pptx") as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 600, 400, True)
        series = chart.chart_data.series
        series[0].labels.default_data_label_format.show_label_value_from_cell = True

        wb = chart.chart_data.chart_data_workbook

        series[0].labels[0].value_from_cell = wb.get_cell(0, "A10", lbl0)
        series[0].labels[1].value_from_cell = wb.get_cell(0, "A11", lbl1)
        series[0].labels[2].value_from_cell = wb.get_cell(0, "A12", lbl2)

        pres.save(global_opts.out_dir + "charts_workbook_as_datalabel_out.pptx", slides.export.SaveFormat.PPTX)
