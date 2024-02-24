import aspose.pydrawing as drawing
import aspose.slides as slides


def charts_radar_chart(options):
    with slides.Presentation() as pres:
        # Access first slide
        slide = pres.slides[0]

        # Add Radar chart
        chart = slide.shapes.add_chart(slides.charts.ChartType.RADAR, 0, 0, 400, 400)

        # Setting the index of chart data sheet
        default_worksheet_index = 0

        # Getting the chart data worksheet
        fact = chart.chart_data.chart_data_workbook

        # Set chart title
        chart.chart_title.add_text_frame_for_overriding("Radar Chart")

        # Delete default generated series and categories
        chart.chart_data.categories.clear()
        chart.chart_data.series.clear()

        # Adding new categories
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 1, 0, "Caetegoty 1"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 2, 0, "Caetegoty 3"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 3, 0, "Caetegoty 5"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 4, 0, "Caetegoty 7"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 5, 0, "Caetegoty 9"))
        chart.chart_data.categories.add(fact.get_cell(default_worksheet_index, 6, 0, "Caetegoty 11"))

        # Adding new series
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 0, 1, "Series 1"), chart.type)
        chart.chart_data.series.add(fact.get_cell(default_worksheet_index, 0, 2, "Series 2"), chart.type)

        # Now populating series data
        series = chart.chart_data.series[0]
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 1, 1, 2.7))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 2, 1, 2.4))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 3, 1, 1.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 4, 1, 3.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 5, 1, 5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 6, 1, 3.5))

        # Set series color
        series.format.line.fill_format.fill_type = slides.FillType.SOLID
        series.format.line.fill_format.solid_fill_color.color = drawing.Color.dark_red

        # Now populating another series data
        series = chart.chart_data.series[1]
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 1, 2, 2.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 2, 2, 2.4))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 3, 2, 1.6))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 4, 2, 3.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 5, 2, 4))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(default_worksheet_index, 6, 2, 3.6))

        # Set series color
        series.format.line.fill_format.fill_type = slides.FillType.SOLID
        series.format.line.fill_format.solid_fill_color.color = drawing.Color.orange

        # Set legend position
        chart.legend.position = slides.charts.LegendPositionType.BOTTOM

        # Setting Category Axis Text Properties
        text_category = chart.axes.horizontal_axis.text_format.portion_format
        text_category.font_bold = slides.NullableBool.TRUE
        text_category.font_height = 10
        text_category.fill_format.fill_type = slides.FillType.SOLID
        text_category.fill_format.solid_fill_color.color = drawing.Color.dim_gray
        text_category.latin_font = slides.FontData("Calibri")

        # Setting Legends Text Properties
        text_legend = chart.legend.text_format.portion_format
        text_legend.font_bold = slides.NullableBool.TRUE
        text_legend.font_height = 10
        text_legend.fill_format.fill_type = slides.FillType.SOLID
        text_legend.fill_format.solid_fill_color.color = drawing.Color.dim_gray
        text_category.latin_font = slides.FontData("Calibri")

        # Setting Value Axis Text Properties
        text_value = chart.axes.vertical_axis.text_format.portion_format
        text_value.font_bold = slides.NullableBool.TRUE
        text_value.font_height = 10
        text_value.fill_format.fill_type = slides.FillType.SOLID
        text_value.fill_format.solid_fill_color.color = drawing.Color.dim_gray
        text_value.latin_font = slides.FontData("Calibri")

        # Setting value axis number format
        chart.axes.vertical_axis.is_number_format_linked_to_source = False
        chart.axes.vertical_axis.number_format = "\"$\"#,##0.00"

        # Setting chart major unit value
        chart.axes.vertical_axis.is_automatic_major_unit = False
        chart.axes.vertical_axis.major_unit = 1.25

        # Save generated presentation
        pres.save(options.out_dir + "charts_radar_chart_out.pptx", slides.export.SaveFormat.PPTX)
