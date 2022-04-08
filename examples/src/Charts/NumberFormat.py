import aspose.slides as slides

def charts_number_format():
    #ExStart:number_format
    # The path to the documents directory.
    outDir = "./examples/out/"

    # Instantiate the presentation# Instantiate the presentation
    with slides.Presentation() as pres:

        # Access the first presentation slide
        slide = pres.slides[0]

        # Adding a defautlt clustered column chart
        chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 400)

        # Accessing the chart series collection
        series = chart.chart_data.series

        # Setting the preset number format
        # Traverse through every chart series
        for ser in series:
            # Traverse through every data cell in series
            for cell in ser.data_points:
                # Setting the number format
                cell.value.as_cell.preset_number_format = 10 #0.00%

        # Saving presentation
        pres.save(outDir + "charts_number_format_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:number_format