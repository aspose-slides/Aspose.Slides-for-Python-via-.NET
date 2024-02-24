import aspose.slides as slides
import shutil


def charts_create_external_workbook(global_opts):
    external_workbook_file_name = "charts_external_workbook.xlsx"
    shutil.copyfile(global_opts.data_dir + external_workbook_file_name, global_opts.out_dir + external_workbook_file_name)

    with slides.Presentation() as pres:
        chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 500, 400)
        chart.chart_data.chart_data_workbook.clear(0)

        # NOTE: Use absolute path to file here
        chart.chart_data.set_external_workbook(global_opts.out_dir + external_workbook_file_name)

        chart.chart_data.set_range("Sheet1!$A$2:$B$5")
        series = chart.chart_data.series[0]
        series.parent_series_group.is_color_varied = True
        pres.save(global_opts.out_dir + "charts_create_external_workbook_out.pptx", slides.export.SaveFormat.PPTX)
