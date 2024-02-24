import aspose.slides as slides


def charts_data_cell_formulas(global_opts):
    """This example demonstrates a way to set a formula value for a chart data cell."""
    with slides.Presentation() as presentation:
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 150, 150, 500, 300)
        workbook = chart.chart_data.chart_data_workbook

        cell1 = workbook.get_cell(0, "B2")
        cell1.formula = "1 + SUM(F2:H5)"

        cell2 = workbook.get_cell(0, "C2")
        cell2.r1c1_formula = "MAX(R2C6:R5C8) / 3"
        workbook.calculate_formulas()

        presentation.save(global_opts.out_dir + "charts_data_cell_formulas_out.pptx", slides.export.SaveFormat.PPTX)
