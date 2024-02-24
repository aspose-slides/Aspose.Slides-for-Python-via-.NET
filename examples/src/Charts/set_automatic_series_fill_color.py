import aspose.slides as slides


def charts_set_automatic_series_fill_color(options):
    with slides.Presentation() as presentation:
        # Creating a clustered column chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 50, 600, 400)

        # Setting series fill format to automatic
        for i in range(len(chart.chart_data.series)):
            chart.chart_data.series[i].get_automatic_series_color()

        # Write the presentation file to disk
        presentation.save(options.out_dir + "charts_set_automatic_series_fill_color_out.pptx", slides.export.SaveFormat.PPTX)
