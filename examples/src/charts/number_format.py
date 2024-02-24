import aspose.slides as slides


def charts_number_format(options):
    # Instantiate the presentation
    with slides.Presentation() as pres:
        # Access the first presentation slide
        slide = pres.slides[0]

        # Adding a default clustered column chart
        chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 400)

        # Accessing the chart series collection
        series = chart.chart_data.series

        # Setting the preset number format
        # Traverse through every chart series
        for ser in series:
            # Traverse through every data cell in series
            for cell in ser.data_points:
                # Setting the number format
                cell.value.as_cell.preset_number_format = 10  # 0.00%

        # Saving presentation
        pres.save(options.out_dir + "charts_number_format_out.pptx", slides.export.SaveFormat.PPTX)
