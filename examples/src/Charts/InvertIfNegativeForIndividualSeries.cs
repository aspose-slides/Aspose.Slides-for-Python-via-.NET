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
	class InvertIfNegativeForIndividualSeries
	{
       public static void Run()
		{
			#ExStart:InvertIfNegativeForIndividualSeries
			dataDir = RunExamples.GetDataDir_Charts()
			with slides.Presentation() as pres:
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400, True)
				IChartSeriesCollection series = chart.chart_data.series
				chart.chart_data.series.clear()

				series.add(chart.chart_data.chart_data_workbook.get_cell(0, "B1"), chart.type)
				series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B2", -5))
				series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B3", 3))
				series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B4", -2))
				series[0].data_points.add_data_point_for_bar_series(chart.chart_data.chart_data_workbook.get_cell(0, "B5", 1))

				series[0].InvertIfNegative = False

				series[0].data_points[2].InvertIfNegative = True

				pres.save(dataDir+ "InvertIfNegativeForIndividualSeries.pptx", slides.export.SaveFormat.PPTX)
			}

		}

		#ExEnd:InvertIfNegativeForIndividualSeries
	}
}