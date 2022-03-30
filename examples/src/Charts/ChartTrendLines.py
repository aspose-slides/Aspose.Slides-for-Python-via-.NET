import aspose.slides as slides
import aspose.pydrawing as drawing

def charts_trend_lines():
    #ExStart:ChartTrendLines
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Creating empty presentation
    with slides.Presentation() as pres:

        # Creating a clustered column chart
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 20, 500, 400)

        # Adding ponential trend line for chart series 1
        tredLinep = chart.chart_data.series[0].trend_lines.add(slides.charts.TrendlineType.EXPONENTIAL)
        tredLinep.display_equation = False
        tredLinep.display_rsquared_value = False

        # Adding Linear trend line for chart series 1
        tredLineLin = chart.chart_data.series[0].trend_lines.add(slides.charts.TrendlineType.LINEAR)
        tredLineLin.trendline_type = slides.charts.TrendlineType.LINEAR
        tredLineLin.format.line.fill_format.fill_type = slides.FillType.SOLID
        tredLineLin.format.line.fill_format.solid_fill_color.color = drawing.Color.red


        # Adding Logarithmic trend line for chart series 2
        tredLineLog = chart.chart_data.series[1].trend_lines.add(slides.charts.TrendlineType.LOGARITHMIC)
        tredLineLog.trendline_type = slides.charts.TrendlineType.LOGARITHMIC
        tredLineLog.add_text_frame_for_overriding("New log trend line")

        # Adding MovingAverage trend line for chart series 2
        tredLineMovAvg = chart.chart_data.series[1].trend_lines.add(slides.charts.TrendlineType.MOVING_AVERAGE)
        tredLineMovAvg.trendline_type = slides.charts.TrendlineType.MOVING_AVERAGE
        tredLineMovAvg.period = 3
        tredLineMovAvg.trendline_name = "New TrendLine Name"

        # Adding Polynomial trend line for chart series 3
        tredLinePol = chart.chart_data.series[2].trend_lines.add(slides.charts.TrendlineType.POLYNOMIAL)
        tredLinePol.trendline_type = slides.charts.TrendlineType.POLYNOMIAL
        tredLinePol.forward = 1
        tredLinePol.order = 3

        # Adding Power trend line for chart series 3
        tredLinePower = chart.chart_data.series[1].trend_lines.add(slides.charts.TrendlineType.POWER)
        tredLinePower.trendline_type = slides.charts.TrendlineType.POWER
        tredLinePower.backward = 1

        # Saving presentation
        pres.save(outDir + "charts_ChartTrendLines_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:ChartTrendLines

