import aspose.slides as slides


def charts_set_layout_mode(options):
    with slides.Presentation() as presentation:
        slide = presentation.slides[0]
        chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 100, 600, 400)
        chart.plot_area.as_i_layoutable.x = 0.2
        chart.plot_area.as_i_layoutable.y = 0.2
        chart.plot_area.as_i_layoutable.width = 0.7
        chart.plot_area.as_i_layoutable.height = 0.7
        chart.plot_area.layout_target_type = slides.charts.LayoutTargetType.INNER

        presentation.save(options.out_dir + "charts_set_layout_mode_out.pptx", slides.export.SaveFormat.PPTX)
