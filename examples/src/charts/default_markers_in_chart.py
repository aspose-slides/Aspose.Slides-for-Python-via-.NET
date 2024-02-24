import aspose.slides as slides


def charts_default_markers(global_opts):
    with slides.Presentation() as pres:
        slide = pres.slides[0]
        chart = slide.shapes.add_chart(slides.charts.ChartType.LINE_WITH_MARKERS, 10, 10, 400, 400)

        chart.chart_data.series.clear()
        chart.chart_data.categories.clear()

        fact = chart.chart_data.chart_data_workbook
        chart.chart_data.series.add(fact.get_cell(0, 0, 1, "Series 1"), chart.type)
        series = chart.chart_data.series[0]

        chart.chart_data.categories.add(fact.get_cell(0, 1, 0, "C1"))
        series.data_points.add_data_point_for_line_series(fact.get_cell(0, 1, 1, 24))
        chart.chart_data.categories.add(fact.get_cell(0, 2, 0, "C2"))
        series.data_points.add_data_point_for_line_series(fact.get_cell(0, 2, 1, 23))
        chart.chart_data.categories.add(fact.get_cell(0, 3, 0, "C3"))
        series.data_points.add_data_point_for_line_series(fact.get_cell(0, 3, 1, -10))
        chart.chart_data.categories.add(fact.get_cell(0, 4, 0, "C4"))
        series.data_points.add_data_point_for_line_series(fact.get_cell(0, 4, 1, None))

        chart.chart_data.series.add(fact.get_cell(0, 0, 2, "Series 2"), chart.type)
        # Take second chart series
        series2 = chart.chart_data.series[1]

        # Now populating series data
        series2.data_points.add_data_point_for_line_series(fact.get_cell(0, 1, 2, 30))
        series2.data_points.add_data_point_for_line_series(fact.get_cell(0, 2, 2, 10))
        series2.data_points.add_data_point_for_line_series(fact.get_cell(0, 3, 2, 60))
        series2.data_points.add_data_point_for_line_series(fact.get_cell(0, 4, 2, 40))

        chart.has_legend = True
        chart.legend.overlay = False

        pres.save(global_opts.out_dir + "charts_default_markers_out.pptx", slides.export.SaveFormat.PPTX)
