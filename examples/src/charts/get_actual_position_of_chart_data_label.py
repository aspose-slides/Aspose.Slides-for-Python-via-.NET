import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_get_actual_position_of_chart_data_label(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 500, 400)
        for series in chart.chart_data.series:
            series.labels.default_data_label_format.position = slides.charts.LegendDataLabelPosition.OUTSIDE_END
            series.labels.default_data_label_format.show_value = True

        chart.validate_chart_layout()

        for series in chart.chart_data.series:
            for point in series.data_points:
                if point.value.to_double() > 4:
                    x = point.label.actual_x
                    y = point.label.actual_y
                    w = point.label.actual_width
                    h = point.label.actual_height

                    shape = chart.user_shapes.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, x, y, w, h)
                    shape.fill_format.fill_type = slides.FillType.SOLID
                    shape.fill_format.solid_fill_color.color = drawing.Color.from_argb(100, 0, 255, 0)

        pres.save(options.out_dir + "charts_get_actual_position_of_chart_datalabel_out.pptx", slides.export.SaveFormat.PPTX)
