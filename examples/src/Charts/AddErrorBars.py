import aspose.slides as slides

def charts_add_error_bars():
    #ExStart:AddErrorBars
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Creating empty presentation
    with slides.Presentation() as presentation:
        # Creating a bubble chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 400, 300, True)

        # Adding Error bars and setting its format
        errBarX = chart.chart_data.series[0].error_bars_xformat
        errBarY = chart.chart_data.series[0].error_bars_yformat
        errBarX.is_visible = True
        errBarY.is_visible = True
        errBarX.value_type = slides.charts.ErrorBarValueType.FIXED
        errBarX.value = 0.1
        errBarY.value_type = slides.charts.ErrorBarValueType.PERCENTAGE
        errBarY.value = 5
        errBarX.type = slides.charts.ErrorBarType.PLUS
        errBarY.format.line.width = 2
        errBarX.has_end_cap = True

        # Saving presentation
        presentation.save(outDir + "charts_add_error_bars_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:AddErrorBars