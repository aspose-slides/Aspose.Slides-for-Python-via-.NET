import aspose.slides as slides


def charts_second_plot_options(options):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:

        # Add chart on slide
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.PIE_OF_PIE, 50, 50, 500, 400)

        # Set different properties
        chart.chart_data.series[0].labels.default_data_label_format.show_value = True
        chart.chart_data.series[0].parent_series_group.second_pie_size = 149
        chart.chart_data.series[0].parent_series_group.pie_split_by = slides.charts.PieSplitType.BY_PERCENTAGE
        chart.chart_data.series[0].parent_series_group.pie_split_position = 53

        # Write presentation to disk
        presentation.save(options.out_dir + "charts_second_plot_options_out.pptx", slides.export.SaveFormat.PPTX)
