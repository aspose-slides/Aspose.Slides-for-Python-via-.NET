import aspose.slides as slides


def charts_add_error_bars(global_opts):
    # Creating empty presentation
    with slides.Presentation() as presentation:
        # Creating a bubble chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 400, 300, True)

        # Adding Error bars and setting its format
        err_bar_x = chart.chart_data.series[0].error_bars_x_format
        err_bar_y = chart.chart_data.series[0].error_bars_y_format
        err_bar_x.is_visible = True
        err_bar_y.is_visible = True
        err_bar_x.value_type = slides.charts.ErrorBarValueType.FIXED
        err_bar_x.value = 0.1
        err_bar_y.value_type = slides.charts.ErrorBarValueType.PERCENTAGE
        err_bar_y.value = 5
        err_bar_x.type = slides.charts.ErrorBarType.PLUS
        err_bar_y.format.line.width = 2
        err_bar_x.has_end_cap = True

        # Saving presentation
        presentation.save(global_opts.out_dir + "charts_add_error_bars_out.pptx", slides.export.SaveFormat.PPTX)
