import aspose.pydrawing as drawing
import aspose.slides as slides


def charts_pie_chart(options):
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

        # Not working in new version
        # Adding new points and setting sector color
        # series.is_color_varied = True
        chart.chart_data.series_groups[0].is_color_varied = True

        point = series.data_points[0]
        point.format.fill.fill_type = slides.FillType.SOLID
        point.format.fill.solid_fill_color.color = drawing.Color.cyan

        # Setting Sector border
        point.format.line.fill_format.fill_type = slides.FillType.SOLID
        point.format.line.fill_format.solid_fill_color.color = drawing.Color.gray
        point.format.line.width = 3.0
        point.format.line.style = slides.LineStyle.THIN_THICK
        point.format.line.dash_style = slides.LineDashStyle.DASH_DOT

        point1 = series.data_points[1]
        point1.format.fill.fill_type = slides.FillType.SOLID
        point1.format.fill.solid_fill_color.color = drawing.Color.brown

        # Setting Sector border
        point1.format.line.fill_format.fill_type = slides.FillType.SOLID
        point1.format.line.fill_format.solid_fill_color.color = drawing.Color.blue
        point1.format.line.width = 3.0
        point1.format.line.style = slides.LineStyle.SINGLE
        point1.format.line.dash_style = slides.LineDashStyle.LARGE_DASH_DOT

        point2 = series.data_points[2]
        point2.format.fill.fill_type = slides.FillType.SOLID
        point2.format.fill.solid_fill_color.color = drawing.Color.coral

        # Setting Sector border
        point2.format.line.fill_format.fill_type = slides.FillType.SOLID
        point2.format.line.fill_format.solid_fill_color.color = drawing.Color.red
        point2.format.line.width = 2.0
        point2.format.line.style = slides.LineStyle.THIN_THIN
        point2.format.line.dash_style = slides.LineDashStyle.LARGE_DASH_DOT_DOT

        # Create custom labels for each of categories for new series
        lbl1 = series.data_points[0].label

        # lbl.show_category_name = True
        lbl1.data_label_format.show_value = True

        lbl2 = series.data_points[1].label
        lbl2.data_label_format.show_value = True
        lbl2.data_label_format.show_legend_key = True
        lbl2.data_label_format.show_percentage = True

        lbl3 = series.data_points[2].label
        lbl3.data_label_format.show_series_name = True
        lbl3.data_label_format.show_percentage = True

        # Showing Leader Lines for Chart
        series.labels.default_data_label_format.show_leader_lines = True

        # Setting Rotation Angle for Pie Chart Sectors
        chart.chart_data.series_groups[0].first_slice_angle = 180

        # Save presentation with chart
        presentation.save(options.out_dir + "charts_pie_chart_out.pptx", slides.export.SaveFormat.PPTX)
