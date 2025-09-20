import aspose.slides as slides


def title_legend_chart_example():
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 350)
        chart.validate_chart_layout()

        chart_title = chart.chart_title
        print(f"Chart Title X = {chart_title.actual_x}, Chart Title Y = {chart_title.actual_y}")
        print(f"Chart Title Width = {chart_title.actual_width}, Chart Title Height = {chart_title.actual_height}")

        legend = chart.legend
        print(f"Legend X = {legend.actual_x}, Legend Y = {legend.actual_y}")
        print(f"Legend Width = {legend.actual_width}, Legend Height = {legend.actual_height}")
