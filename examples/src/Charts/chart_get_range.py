import aspose.slides as slides


def charts_get_range():
    """Using IChartData.get_range() method example."""
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 10, 10, 400, 300)
        result = chart.chart_data.get_range()
        print("GetRange result: {0}".format(result))
