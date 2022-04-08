import aspose.slides as slides

def charts_get_values_and_unit_scale_from_axis():
    #ExStart:GetValuesAndUnitScaleFromAxis
    # The path to the documents directory.
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.AREA, 100, 100, 500, 350)
        chart.validate_chart_layout()

        maxValue = chart.axes.vertical_axis.actual_max_value
        minValue = chart.axes.vertical_axis.actual_min_value

        majorUnit = chart.axes.horizontal_axis.actual_major_unit
        minorUnit = chart.axes.horizontal_axis.actual_minor_unit

        # Saving presentation
        pres.save(outDir + "charts_get_values_and_unit_scale_from_axis_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:GetValuesAndUnitScaleFromAxis
