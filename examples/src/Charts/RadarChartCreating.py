import aspose.pydrawing as drawing
import aspose.slides as slides

def charts_radar_chart():
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        # Access first slide
        sld = pres.slides[0]

        # Add Radar chart
        ichart = sld.shapes.add_chart(slides.charts.ChartType.RADAR, 0, 0, 400, 400)

        # Setting the index of chart data sheet
        defaultWorksheetIndex = 0

        # Getting the chart data WorkSheet
        fact = ichart.chart_data.chart_data_workbook

        # Set chart title
        ichart.chart_title.add_text_frame_for_overriding("Radar Chart")

        # Delete default generated series and categories
        ichart.chart_data.categories.clear()
        ichart.chart_data.series.clear()

        # Adding new categories
        ichart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 1, 0, "Caetegoty 1"))
        ichart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 2, 0, "Caetegoty 3"))
        ichart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 3, 0, "Caetegoty 5"))
        ichart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 4, 0, "Caetegoty 7"))
        ichart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 5, 0, "Caetegoty 9"))
        ichart.chart_data.categories.add(fact.get_cell(defaultWorksheetIndex, 6, 0, "Caetegoty 11"))

        # Adding new series
        ichart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 0, 1, "Series 1"), ichart.type)
        ichart.chart_data.series.add(fact.get_cell(defaultWorksheetIndex, 0, 2, "Series 2"), ichart.type)

        # Now populating series data
        series = ichart.chart_data.series[0]
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 1, 1, 2.7))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 2, 1, 2.4))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 3, 1, 1.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 4, 1, 3.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 5, 1, 5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 6, 1, 3.5))

        # Set series color
        series.format.line.fill_format.fill_type = slides.FillType.SOLID
        series.format.line.fill_format.solid_fill_color.color = drawing.Color.dark_red

        # Now populating another series data
        series = ichart.chart_data.series[1]
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 1, 2, 2.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 2, 2, 2.4))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 3, 2, 1.6))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 4, 2, 3.5))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 5, 2, 4))
        series.data_points.add_data_point_for_radar_series(fact.get_cell(defaultWorksheetIndex, 6, 2, 3.6))

        # Set series color
        series.format.line.fill_format.fill_type = slides.FillType.SOLID
        series.format.line.fill_format.solid_fill_color.color = drawing.Color.orange

        # Set legend position
        ichart.legend.position = slides.charts.LegendPositionType.BOTTOM

        # Setting Category Axis Text Properties
        txtCat = ichart.axes.horizontal_axis.text_format.portion_format
        txtCat.font_bold = 1
        txtCat.font_height = 10
        txtCat.fill_format.fill_type = slides.FillType.SOLID 
        txtCat.fill_format.solid_fill_color.color = drawing.Color.dim_gray
        txtCat.latin_font = slides.FontData("Calibri")

        # Setting Legends Text Properties
        txtleg = ichart.legend.text_format.portion_format
        txtleg.font_bold = 1
        txtleg.font_height = 10
        txtleg.fill_format.fill_type = slides.FillType.SOLID 
        txtleg.fill_format.solid_fill_color.color = drawing.Color.dim_gray
        txtCat.latin_font = slides.FontData("Calibri")

        # Setting Value Axis Text Properties
        txtVal = ichart.axes.vertical_axis.text_format.portion_format
        txtVal.font_bold = 1
        txtVal.font_height = 10
        txtVal.fill_format.fill_type = slides.FillType.SOLID 
        txtVal.fill_format.solid_fill_color.color = drawing.Color.dim_gray
        txtVal.latin_font = slides.FontData("Calibri")

        # Setting value axis number format
        ichart.axes.vertical_axis.is_number_format_linked_to_source = False
        ichart.axes.vertical_axis.number_format = "\"$\"#,##0.00"

        # Setting chart major unit value
        ichart.axes.vertical_axis.is_automatic_major_unit = False
        ichart.axes.vertical_axis.major_unit = 1.25

        # Save generated presentation
        pres.save(outDir + "charts_radar_chart_out.pptx", slides.export.SaveFormat.PPTX)
