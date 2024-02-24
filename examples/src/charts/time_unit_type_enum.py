import aspose.slides as slides


def charts_time_unit_type_enum(global_opts):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.AREA, 10, 10, 400, 300, True)
        chart.axes.horizontal_axis.major_unit_scale = slides.charts.TimeUnitType.NONE
        pres.save(global_opts.out_dir + "charts_time_unit_type_enum_out.pptx", slides.export.SaveFormat.PPTX)
