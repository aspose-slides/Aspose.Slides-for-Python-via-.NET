import aspose.pydrawing as drawing
import aspose.slides as slides

def charts_multi_category_chart():
    #ExStart:MultiCategoryChart
    # The path to the documents directory.
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        slide = pres.slides[0]

        ch = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 100, 100, 600, 450)
        ch.chart_data.series.clear()
        ch.chart_data.categories.clear()


        fact = ch.chart_data.chart_data_workbook
        fact.clear(0)
        defaultWorksheetIndex = 0

        category = ch.chart_data.categories.add(fact.get_cell(0, "c2", "A"))
        category.grouping_levels.set_grouping_item(1, "Group1")
        category = ch.chart_data.categories.add(fact.get_cell(0, "c3", "B"))

        category = ch.chart_data.categories.add(fact.get_cell(0, "c4", "C"))
        category.grouping_levels.set_grouping_item(1, "Group2")
        category = ch.chart_data.categories.add(fact.get_cell(0, "c5", "D"))

        category = ch.chart_data.categories.add(fact.get_cell(0, "c6", "E"))
        category.grouping_levels.set_grouping_item(1, "Group3")
        category = ch.chart_data.categories.add(fact.get_cell(0, "c7", "F"))

        category = ch.chart_data.categories.add(fact.get_cell(0, "c8", "G"))
        category.grouping_levels.set_grouping_item(1, "Group4")
        category = ch.chart_data.categories.add(fact.get_cell(0, "c9", "H"))

        #            Adding Series
        series = ch.chart_data.series.add(fact.get_cell(0, "D1", "Series 1"),
            slides.charts.ChartType.CLUSTERED_COLUMN)

        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D2", 10))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D3", 20))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D4", 30))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D5", 40))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D6", 50))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D7", 60))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D8", 70))
        series.data_points.add_data_point_for_bar_series(fact.get_cell(defaultWorksheetIndex, "D9", 80))
        # Save presentation with chart
        pres.save(outDir + "charts_multi_category_chart_out.pptx", slides.export.SaveFormat.PPTX)
    #ExEnd:MultiCategoryChart