import aspose.slides as slides


def charts_setting_automic_pie_chart_slice_colors(options):
    # Instantiate Presentation class that represents PPTX file
    with slides.Presentation() as presentation:
        # Access first slide
        slide = presentation.slides[0]

        # Add chart with default data
        chart = slide.shapes.add_chart(slides.charts.ChartType.PIE, 100, 100, 400, 400)

        # Setting chart Title
        chart.chart_title.add_text_frame_for_overriding("Sample Title")
        chart.chart_title.text_frame_for_overriding.text_frame_format.center_text = slides.NullableBool.TRUE
        chart.chart_title.height = 20
        chart.has_title = True

        # Set first series to Show Values
        chart.chart_data.series[0].labels.default_data_label_format.show_value = True

        # Setting the index of chart data sheet
        default_worksheet_index = 0

        # Getting the chart data worksheet
        fact = chart.chart_data.chart_data_workbook

        # Delete default generated series and categories
        chart.chart_data.series.clear()
        chart.chart_data.categories.clear()

        # Adding new categories
        chart.chart_data.categories.add(fact.get_cell(0, 1, 0, "First Qtr"))
        chart.chart_data.categories.add(fact.get_cell(0, 2, 0, "2nd Qtr"))
        chart.chart_data.categories.add(fact.get_cell(0, 3, 0, "3rd Qtr"))

        # Adding new series
        series = chart.chart_data.series.add(fact.get_cell(0, 0, 1, "Series 1"), chart.type)

        # Now populating series data
        series.data_points.add_data_point_for_pie_series(fact.get_cell(default_worksheet_index, 1, 1, 20))
        series.data_points.add_data_point_for_pie_series(fact.get_cell(default_worksheet_index, 2, 1, 50))
        series.data_points.add_data_point_for_pie_series(fact.get_cell(default_worksheet_index, 3, 1, 30))
    
        series.parent_series_group.is_color_varied = True
        presentation.save(options.out_dir + "charts_setting_automic_pie_chart_slice_colors_out.pptx", slides.export.SaveFormat.PPTX)
