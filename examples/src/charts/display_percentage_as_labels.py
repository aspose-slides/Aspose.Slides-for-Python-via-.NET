﻿import aspose.slides as slides


def charts_display_percentage_as_labels(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation() as presentation:
        slide = presentation.slides[0]
        chart = slide.shapes.add_chart(slides.charts.ChartType.STACKED_COLUMN, 20, 20, 400, 400)
        series = chart.chart_data.series[0]
        total_for_category = []
        for k in range(len(chart.chart_data.categories)):
            
            value = 0
            for i in range(len(chart.chart_data.series)):
                value += chart.chart_data.series[i].data_points[k].value.data

            total_for_category.append(value)

        for series in chart.chart_data.series:

            series.labels.default_data_label_format.show_legend_key = False

            for j in range(len(series.data_points)):
                lbl = series.data_points[j].label
                
                data_pont_percent = series.data_points[j].value.data / total_for_category[j] * 100.0

                port = slides.Portion()
                port.text = "{0:4.2f} %".format(data_pont_percent)
                port.portion_format.font_height = 8
                lbl.text_frame_for_overriding.text = ""
                para = lbl.text_frame_for_overriding.paragraphs[0]
                para.portions.add(port)

                lbl.data_label_format.show_series_name = False
                lbl.data_label_format.show_percentage = False
                lbl.data_label_format.show_legend_key = False
                lbl.data_label_format.show_category_name = False
                lbl.data_label_format.show_bubble_size = False

        # Save presentation with chart
        presentation.save(global_opts.out_dir + "charts_display_percentage_as_labels_out.pptx", slides.export.SaveFormat.PPTX)
