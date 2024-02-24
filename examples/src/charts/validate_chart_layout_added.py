import aspose.slides as slides


def charts_validate_chart_layout(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 500, 350)
        chart.validate_chart_layout()
        x = chart.plot_area.actual_x
        y = chart.plot_area.actual_y
        w = chart.plot_area.actual_width
        h = chart.plot_area.actual_height

        pres.save(options.out_dir + "charts_validate_chart_layout_out.pptx", slides.export.SaveFormat.PPTX)
