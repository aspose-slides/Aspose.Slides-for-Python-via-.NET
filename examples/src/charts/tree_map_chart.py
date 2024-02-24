import aspose.slides as slides


def charts_tree_map_chart(global_opts):
    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.TREEMAP, 50, 50, 500, 400)
        chart.chart_data.categories.clear()
        chart.chart_data.series.clear()

        wb = chart.chart_data.chart_data_workbook

        wb.clear(0)

        # branch 1
        leaf = chart.chart_data.categories.add(wb.get_cell(0, "C1", "Leaf1"))
        leaf.grouping_levels.set_grouping_item(1, "Stem1")
        leaf.grouping_levels.set_grouping_item(2, "Branch1")

        chart.chart_data.categories.add(wb.get_cell(0, "C2", "Leaf2"))

        leaf = chart.chart_data.categories.add(wb.get_cell(0, "C3", "Leaf3"))
        leaf.grouping_levels.set_grouping_item(1, "Stem2")

        chart.chart_data.categories.add(wb.get_cell(0, "C4", "Leaf4"))

        # branch 2
        leaf = chart.chart_data.categories.add(wb.get_cell(0, "C5", "Leaf5"))
        leaf.grouping_levels.set_grouping_item(1, "Stem3")
        leaf.grouping_levels.set_grouping_item(2, "Branch2")

        chart.chart_data.categories.add(wb.get_cell(0, "C6", "Leaf6"))

        leaf = chart.chart_data.categories.add(wb.get_cell(0, "C7", "Leaf7"))
        leaf.grouping_levels.set_grouping_item(1, "Stem4")

        chart.chart_data.categories.add(wb.get_cell(0, "C8", "Leaf8"))

        series = chart.chart_data.series.add(slides.charts.ChartType.TREEMAP)
        series.labels.default_data_label_format.show_category_name = True
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D1", 4))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D2", 5))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D3", 3))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D4", 6))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D5", 9))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D6", 9))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D7", 4))
        series.data_points.add_data_point_for_treemap_series(wb.get_cell(0, "D8", 3))

        series.parent_label_layout = slides.charts.ParentLabelLayoutType.OVERLAPPING

        pres.save(global_opts.out_dir + "charts_tree_map_chart_out.pptx", slides.export.SaveFormat.PPTX)
