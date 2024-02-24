import aspose.slides as slides


def custom_rotation_angle_text_frame(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 300)

        series = chart.chart_data.series[0]

        series.labels.default_data_label_format.show_value = True
        series.labels.default_data_label_format.text_format.text_block_format.rotation_angle = 65

        chart.has_title = True
        chart.chart_title.add_text_frame_for_overriding("Custom title").text_frame_format.rotation_angle = -30

        # Save Presentation
        presentation.save(global_opts.out_dir + "text_textframe_rotation_out.pptx", slides.export.SaveFormat.PPTX)
