import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_trend_lines(global_opts):
    # Creating empty presentation
    with slides.Presentation() as pres:
        # Creating a clustered column chart
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 20, 500, 400)

        # Adding exponential trend line for chart series 1
        exp_trend_line = chart.chart_data.series[0].trend_lines.add(slides.charts.TrendlineType.EXPONENTIAL)
        exp_trend_line.display_equation = False
        exp_trend_line.display_r_squared_value = False

        # Adding Linear trend line for chart series 1
        linear_trend_line = chart.chart_data.series[0].trend_lines.add(slides.charts.TrendlineType.LINEAR)
        linear_trend_line.trendline_type = slides.charts.TrendlineType.LINEAR
        linear_trend_line.format.line.fill_format.fill_type = slides.FillType.SOLID
        linear_trend_line.format.line.fill_format.solid_fill_color.color = drawing.Color.red

        # Adding Logarithmic trend line for chart series 2
        log_trend_line = chart.chart_data.series[1].trend_lines.add(slides.charts.TrendlineType.LOGARITHMIC)
        log_trend_line.trendline_type = slides.charts.TrendlineType.LOGARITHMIC
        log_trend_line.add_text_frame_for_overriding("New log trend line")

        # Adding MovingAverage trend line for chart series 2
        mov_avg_trend_line = chart.chart_data.series[1].trend_lines.add(slides.charts.TrendlineType.MOVING_AVERAGE)
        mov_avg_trend_line.trendline_type = slides.charts.TrendlineType.MOVING_AVERAGE
        mov_avg_trend_line.period = 3
        mov_avg_trend_line.trendline_name = "New TrendLine Name"

        # Adding Polynomial trend line for chart series 3
        poly_trend_line = chart.chart_data.series[2].trend_lines.add(slides.charts.TrendlineType.POLYNOMIAL)
        poly_trend_line.trendline_type = slides.charts.TrendlineType.POLYNOMIAL
        poly_trend_line.forward = 1
        poly_trend_line.order = 3

        # Adding Power trend line for chart series 3
        power_trend_line = chart.chart_data.series[1].trend_lines.add(slides.charts.TrendlineType.POWER)
        power_trend_line.trendline_type = slides.charts.TrendlineType.POWER
        power_trend_line.backward = 1

        # Saving presentation
        pres.save(global_opts.out_dir + "charts_trend_lines_out.pptx", slides.export.SaveFormat.PPTX)
