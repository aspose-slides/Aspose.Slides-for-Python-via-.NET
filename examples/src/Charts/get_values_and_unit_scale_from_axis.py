import aspose.slides as slides


def charts_get_values_and_unit_scale_from_axis(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.AREA, 100, 100, 500, 350)
        chart.validate_chart_layout()

        max_value = chart.axes.vertical_axis.actual_max_value
        min_value = chart.axes.vertical_axis.actual_min_value

        major_unit = chart.axes.horizontal_axis.actual_major_unit
        minor_unit = chart.axes.horizontal_axis.actual_minor_unit

        # Saving presentation
        pres.save(options.out_dir + "charts_get_values_and_unit_scale_from_axis_out.pptx", slides.export.SaveFormat.PPTX)
