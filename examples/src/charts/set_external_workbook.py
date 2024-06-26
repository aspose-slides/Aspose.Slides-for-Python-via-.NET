﻿import aspose.slides as slides
import shutil


def charts_set_external_workbook(global_opts):
    external_workbook_file_name = "charts_external_workbook.xlsx"
    shutil.copyfile(global_opts.data_dir + external_workbook_file_name, global_opts.out_dir + external_workbook_file_name)

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 400, 600, False)
        chart_data = chart.chart_data
                        
        chart_data.set_external_workbook(global_opts.out_dir + "charts_external_workbook.xlsx")

        chart_data.series.add(chart_data.chart_data_workbook.get_cell(0, "B1"), slides.charts.ChartType.PIE)
        chart_data.series[0].data_points.add_data_point_for_pie_series(chart_data.chart_data_workbook.get_cell(0, "B2"))
        chart_data.series[0].data_points.add_data_point_for_pie_series(chart_data.chart_data_workbook.get_cell(0, "B3"))
        chart_data.series[0].data_points.add_data_point_for_pie_series(chart_data.chart_data_workbook.get_cell(0, "B4"))

        chart_data.categories.add(chart_data.chart_data_workbook.get_cell(0, "A2"))
        chart_data.categories.add(chart_data.chart_data_workbook.get_cell(0, "A3"))
        chart_data.categories.add(chart_data.chart_data_workbook.get_cell(0, "A4"))
        pres.save(global_opts.out_dir + "charts_set_external_workbook_out.pptx", slides.export.SaveFormat.PPTX)
