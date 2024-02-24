import aspose.slides as slides


def charts_add_custom_error(options):
    # Creating empty presentation
    with slides.Presentation() as presentation:
        # Creating a bubble chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 400, 300, True)

        # Adding custom Error bars and setting its format
        series = chart.chart_data.series[0]
        err_bar_x = series.error_bars_x_format
        err_bar_y = series.error_bars_y_format
        err_bar_x.is_visible = True
        err_bar_y.is_visible = True
        err_bar_x.value_type = slides.charts.ErrorBarValueType.CUSTOM
        err_bar_y.value_type = slides.charts.ErrorBarValueType.CUSTOM

        # Accessing chart series data point and setting error bars values for individual point
        points = series.data_points
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_x_plus_values = slides.charts.DataSourceType.DOUBLE_LITERALS
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_x_minus_values = slides.charts.DataSourceType.DOUBLE_LITERALS
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_y_plus_values = slides.charts.DataSourceType.DOUBLE_LITERALS
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_y_minus_values = slides.charts.DataSourceType.DOUBLE_LITERALS

        # Setting error bars for chart series points
        for i in range(len(points)):
            points[i].error_bars_custom_values.x_minus.as_literal_double = i + 1
            points[i].error_bars_custom_values.x_plus.as_literal_double = i + 1
            points[i].error_bars_custom_values.y_minus.as_literal_double = i + 1
            points[i].error_bars_custom_values.y_plus.as_literal_double = i + 1

        # Saving presentation
        presentation.save(options.out_dir + "charts_add_custom_error_out.pptx", slides.export.SaveFormat.PPTX)
