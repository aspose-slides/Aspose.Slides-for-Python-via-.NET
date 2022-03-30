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
	public class FunnelChart
	{

		#ExStart:FunnelChart
		public static void Run()

		{
			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.Funnel, 50, 50, 500, 400)
				chart.chart_data.categories.clear()
				chart.chart_data.series.clear()

				wb = chart.chart_data.chart_data_workbook

				wb.clear(0)

				chart.chart_data.categories.add(wb.get_cell(0, "A1", "Category 1"))
				chart.chart_data.categories.add(wb.get_cell(0, "A2", "Category 2"))
				chart.chart_data.categories.add(wb.get_cell(0, "A3", "Category 3"))
				chart.chart_data.categories.add(wb.get_cell(0, "A4", "Category 4"))
				chart.chart_data.categories.add(wb.get_cell(0, "A5", "Category 5"))
				chart.chart_data.categories.add(wb.get_cell(0, "A6", "Category 6"))

				series = chart.chart_data.series.add(ChartType.Funnel)

				series.data_points.AddDataPointForFunnelSeries(wb.get_cell(0, "B1", 50))
				series.data_points.AddDataPointForFunnelSeries(wb.get_cell(0, "B2", 100))
				series.data_points.AddDataPointForFunnelSeries(wb.get_cell(0, "B3", 200))
				series.data_points.AddDataPointForFunnelSeries(wb.get_cell(0, "B4", 300))
				series.data_points.AddDataPointForFunnelSeries(wb.get_cell(0, "B5", 400))
				series.data_points.AddDataPointForFunnelSeries(wb.get_cell(0, "B6", 500))

				pres.save(dataDir+"Funnel.pptx", slides.export.SaveFormat.PPTX)
         }

		}
		#ExEnd:FunnelChart
	}
}
