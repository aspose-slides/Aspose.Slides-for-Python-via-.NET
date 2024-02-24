import aspose.slides as slides


def chart_data_point_index(options):
    with slides.Presentation(options.data_dir + "ChartIndex.pptx") as presentation:
        chart = presentation.slides[0].shapes[0]
        for data_point in chart.chart_data.series[0].data_points:
            print("Point with index {0} is applied to {1}".format(data_point.index, data_point.value.to_double()))
