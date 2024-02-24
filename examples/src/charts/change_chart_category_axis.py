import aspose.slides as slides


def charts_change_chart_category_axis(global_opts):
    with slides.Presentation(global_opts.data_dir + "charts_existing_chart.pptx") as presentation:
        chart = presentation.slides[0].shapes[0]
        chart.axes.horizontal_axis.category_axis_type = slides.charts.CategoryAxisType.DATE
        chart.axes.horizontal_axis.is_automatic_major_unit = False
        chart.axes.horizontal_axis.major_unit = 1
        chart.axes.horizontal_axis.major_unit_scale = slides.charts.TimeUnitType.MONTHS
        presentation.save(global_opts.out_dir + "charts_change_chart_category_axis_out.pptx", slides.export.SaveFormat.PPTX)
