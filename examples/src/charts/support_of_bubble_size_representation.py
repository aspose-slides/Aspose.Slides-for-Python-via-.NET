import aspose.slides as slides


def charts_bubble_size_representation(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 50, 50, 600, 400, True)
        chart.chart_data.series_groups[0].bubble_size_representation = slides.charts.BubbleSizeRepresentationType.WIDTH
        pres.save(options.out_dir + "charts_bubble_size_representation_out.pptx", slides.export.SaveFormat.PPTX)
