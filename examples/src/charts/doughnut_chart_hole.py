import aspose.slides as slides


def charts_doughnut_chart_hole(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        chart = presentation.slides[0].shapes.add_chart(slides.charts.ChartType.DOUGHNUT, 50, 50, 400, 400)
        chart.chart_data.series_groups[0].doughnut_hole_size = 90

        # Write presentation to disk
        presentation.save(global_opts.out_dir + "charts_doughnut_chart_hole_out.pptx", slides.export.SaveFormat.PPTX)
