import aspose.slides as slides


def charts_set_chart_series_overlap(options):
    with slides.Presentation() as presentation:
        # Adding chart
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400, True)
        series = chart.chart_data.series
        if series[0].overlap == 0:
            # Setting series overlap
            series[0].parent_series_group.overlap = -30

        # Write the presentation file to disk
        presentation.save(options.out_dir + "charts_set_chart_series_overlap_out.pptx", slides.export.SaveFormat.PPTX)
