import aspose.slides as slides
import aspose.pydrawing as drawing


def charts_add_color_to_data_points(options):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.SUNBURST, 100, 100, 450, 400)

        data_points = chart.chart_data.series[0].data_points
        data_points[3].data_point_levels[0].label.data_label_format.show_value = True

        branch1_label = data_points[0].data_point_levels[2].label
        branch1_label.data_label_format.show_category_name = False
        branch1_label.data_label_format.show_series_name = True

        branch1_label.data_label_format.text_format.portion_format.fill_format.fill_type = slides.FillType.SOLID
        branch1_label.data_label_format.text_format.portion_format.fill_format.solid_fill_color.color = drawing.Color.yellow

        steam4_format = data_points[9].format
        steam4_format.fill.fill_type = slides.FillType.SOLID
        
        steam4_format.fill.solid_fill_color.color = drawing.Color.from_argb(0, 176, 240, 255)

        pres.save(options.out_dir + "charts_add_color_to_data_points_out.pptx", slides.export.SaveFormat.PPTX)
