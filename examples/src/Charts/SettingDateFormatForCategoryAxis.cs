import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
	class SettingDateFormatForCategoryAxis
	{
		public static void Run()
		{
			#ExStart:SettingDateFormatForCategoryAxis
			# The path to the documents directory.
			dataDir = RunExamples.GetDataDir_Charts()
			with slides.Presentation() as pres:
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.AREA, 50, 50, 450, 300)

				wb = chart.chart_data.chart_data_workbook

				wb.clear(0)

				chart.chart_data.categories.clear()
				chart.chart_data.series.clear()
				chart.chart_data.categories.add(wb.get_cell(0, "A2", new DateTime(2015, 1, 1).ToOADate()))
				chart.chart_data.categories.add(wb.get_cell(0, "A3", new DateTime(2016, 1, 1).ToOADate()))
				chart.chart_data.categories.add(wb.get_cell(0, "A4", new DateTime(2017, 1, 1).ToOADate()))
				chart.chart_data.categories.add(wb.get_cell(0, "A5", new DateTime(2018, 1, 1).ToOADate()))

				series = chart.chart_data.series.add(ChartType.Line)
				series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B2", 1))
				series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B3", 2))
				series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B4", 3))
				series.data_points.add_data_point_for_line_series(wb.get_cell(0, "B5", 4))
				chart.axes.horizontal_axis.category_axis_type = CategoryAxisType.DATE
				chart.axes.horizontal_axis.is_number_format_linked_to_source = False
				chart.axes.horizontal_axis.number_format = "yyyy"
				pres.save(dataDir+"test.pptx", slides.export.SaveFormat.PPTX)
			}
			#ExEnd:SettingDateFormatForCategoryAxis
		}
	}
}