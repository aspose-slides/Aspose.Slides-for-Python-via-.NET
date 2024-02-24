import aspose.slides as slides
from datetime import date


def charts_setting_date_format_for_category_axis(options):
	with slides.Presentation() as pres:
		chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.AREA, 50, 50, 450, 300)

		wb = chart.chart_data.chart_data_workbook
		wb.clear(0)

		chart.chart_data.categories.clear()
		chart.chart_data.series.clear()
		chart.chart_data.categories.add(wb.get_cell(0, "A2", date(2015, 1, 1)))
		chart.chart_data.categories.add(wb.get_cell(0, "A3", date(2016, 1, 1)))
		chart.chart_data.categories.add(wb.get_cell(0, "A4", date(2017, 1, 1)))
		chart.chart_data.categories.add(wb.get_cell(0, "A5", date(2018, 1, 1)))

		series = chart.chart_data.series.add(slides.charts.ChartType.LINE)
		series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B2", 1))
		series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B3", 2))
		series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B4", 3))
		series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B5", 4))
		chart.axes.horizontal_axis.category_axis_type = slides.charts.CategoryAxisType.DATE
		chart.axes.horizontal_axis.is_number_format_linked_to_source = False
		chart.axes.horizontal_axis.number_format = "yyyy"

		pres.save(options.out_dir + "charts_setting_date_format_for_category_axis_out.pptx", slides.export.SaveFormat.PPTX)
