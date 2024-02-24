import aspose.slides as slides


def charts_worksheets_example(global_opts):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 500)

        workbook = chart.chart_data.chart_data_workbook
        print("Worksheets example:")
        for i in range(len(workbook.worksheets)):
            print(workbook.worksheets[i].name)
