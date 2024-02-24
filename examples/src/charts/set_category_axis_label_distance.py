import aspose.slides as slides


def charts_set_category_axis_label_distance(global_opts):
    with slides.Presentation() as presentation:
        # Get reference of the slide
        slide = presentation.slides[0]

        # Adding a chart on slide
        ch = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 20, 500, 300)

        # Setting the position of label from axis
        ch.axes.horizontal_axis.label_offset = 500

        # Write the presentation file to disk
        presentation.save(global_opts.out_dir + "charts_set_category_axis_label_distance_out.pptx", slides.export.SaveFormat.PPTX)
