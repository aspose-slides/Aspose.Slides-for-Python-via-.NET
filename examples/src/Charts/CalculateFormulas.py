import aspose.pydrawing as drawing
import aspose.slides as slides


"""This example demonstrates a functionality of an explicit formulas calculation within the workbook."""

def charts_calculate_formulas():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as presentation:
        s_chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 10, 10, 600, 300)

        workbook = s_chart.chart_data.chart_data_workbook
        cell = workbook.get_cell(0, "A1")
        cell.formula = "ABS(A2) + MAX(B2:C2)"

        workbook.get_cell(0, "A2").value = -1
        workbook.calculate_formulas()

        workbook.get_cell(0, "B2").formula = "2"
        workbook.calculate_formulas()

        workbook.get_cell(0, "C2").formula = "A2 + 4"
        workbook.calculate_formulas()

        cell.formula = "MAX(2:2)"
        workbook.calculate_formulas()

        presentation.save(outDir + "charts_CalculateFormulas_out.pptx", slides.export.SaveFormat.PPTX)
