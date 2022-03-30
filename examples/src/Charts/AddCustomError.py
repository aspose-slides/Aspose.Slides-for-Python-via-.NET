import aspose.slides as slides

def charts_add_custom_error():
    #ExStart:AddCustomError
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Creating empty presentation
    with slides.Presentation() as presentation:
        # Creating a bubble chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 400, 300, True)

        # Adding custom Error bars and setting its format
        series = chart.chart_data.series[0]
        errBarX = series.error_bars_xformat
        errBarY = series.error_bars_yformat
        errBarX.is_visible = True
        errBarY.is_visible = True
        errBarX.value_type = slides.charts.ErrorBarValueType.CUSTOM
        errBarY.value_type = slides.charts.ErrorBarValueType.CUSTOM

        # Accessing chart series data point and setting error bars values for individual point
        points = series.data_points
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_xplus_values = slides.charts.DataSourceType.DOUBLE_LITERALS
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_xminus_values = slides.charts.DataSourceType.DOUBLE_LITERALS
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_yplus_values = slides.charts.DataSourceType.DOUBLE_LITERALS
        points.data_source_type_for_error_bars_custom_values.data_source_type_for_yminus_values = slides.charts.DataSourceType.DOUBLE_LITERALS

        # Setting error bars for chart series points
        for i in range(len(points)):
            points[i].error_bars_custom_values.xminus.as_literal_double = i + 1
            points[i].error_bars_custom_values.xplus.as_literal_double = i + 1
            points[i].error_bars_custom_values.yminus.as_literal_double = i + 1
            points[i].error_bars_custom_values.yplus.as_literal_double = i + 1

        # Saving presentation
        presentation.save(outDir + "charts_add_custom_error_out.pptx", slides.export.SaveFormat.PPTX)
        
    #ExEnd:AddCustomError

