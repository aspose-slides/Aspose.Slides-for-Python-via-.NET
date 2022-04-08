import aspose.slides as slides
import aspose.pydrawing as drawing

def charts_hide_information_from_chart():
    #ExStart:HideInformationFromChart
    # The path to the documents directory.
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        slide = pres.slides[0]
        chart = slide.shapes.add_chart(slides.charts.ChartType.LINE_WITH_MARKERS, 140, 118, 320, 370)

        #Hiding chart Title
        chart.has_title = False

        #/Hiding Values axis
        chart.axes.vertical_axis.is_visible = False

        #Category Axis visibility
        chart.axes.horizontal_axis.is_visible = False

        #Hiding Legend
        chart.has_legend = False

        #Hiding MajorGridLines
        chart.axes.horizontal_axis.major_grid_lines_format.line.fill_format.fill_type = slides.FillType.NO_FILL

        for i in range(len(chart.chart_data.series)-1): 
            chart.chart_data.series.remove_at(i)

        series = chart.chart_data.series[0]

        series.marker.symbol = slides.charts.MarkerStyleType.CIRCLE
        series.labels.default_data_label_format.show_value = True
        series.labels.default_data_label_format.position = slides.charts.LegendDataLabelPosition.TOP
        series.marker.size = 15

        #Setting series line color
        series.format.line.fill_format.fill_type = slides.FillType.SOLID
        series.format.line.fill_format.solid_fill_color.color = drawing.Color.purple
        series.format.line.dash_style = slides.LineDashStyle.SOLID

        pres.save(outDir + "charts_hide_information_from_chart_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:HideInformationFromChart
