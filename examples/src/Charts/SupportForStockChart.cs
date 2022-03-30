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
	class SupportForStockChart
	{
		public static void Run()
		{
			#ExStart:SupportForStockChart
			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir+"Test.pptx"))
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.OpenHighLowClose, 50, 50, 600, 400, False)

				chart.chart_data.series.clear()
				chart.chart_data.categories.clear()

				wb = chart.chart_data.chart_data_workbook

				chart.chart_data.categories.add(wb.get_cell(0, 1, 0, "A"))
				chart.chart_data.categories.add(wb.get_cell(0, 2, 0, "B"))
				chart.chart_data.categories.add(wb.get_cell(0, 3, 0, "C"))

				chart.chart_data.series.add(wb.get_cell(0, 0, 1, "Open"), chart.type)
				chart.chart_data.series.add(wb.get_cell(0, 0, 2, "High"), chart.type)
				chart.chart_data.series.add(wb.get_cell(0, 0, 3, "Low"), chart.type)
				chart.chart_data.series.add(wb.get_cell(0, 0, 4, "Close"), chart.type)

				series = chart.chart_data.series[0]

				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 1, 1, 72))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 2, 1, 25))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 3, 1, 38))

				series = chart.chart_data.series[1]
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 1, 2, 172))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 2, 2, 57))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 3, 2, 57))

				series = chart.chart_data.series[2]
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 1, 3, 12))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 2, 3, 12))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 3, 3, 13))

				series = chart.chart_data.series[3]
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 1, 4, 25))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 2, 4, 38))
				series.data_points.AddDataPointForStockSeries(wb.get_cell(0, 3, 4, 50))

				chart.chart_data.SeriesGroups[0].UpDownBars.HasUpDownBars = True
				chart.chart_data.SeriesGroups[0].HiLowLinesFormat.line.fill_format.fill_type = slides.FillType.SOLID

				foreach (ser in chart.chart_data.series)
				{
					ser.format.line.FillFormat.fill_type = FillType.NoFill
				}

				pres.save(dataDir+"output.pptx", slides.export.SaveFormat.PPTX)
			}

		}
		#ExEnd:SupportForStockChart
	}
}
