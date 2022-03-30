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
	public class HistogramChart
	{

		#ExStart:HistogramChart
		public static void Run()

		{

			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.Histogram, 50, 50, 500, 400)
				chart.chart_data.categories.clear()
				chart.chart_data.series.clear()

				wb = chart.chart_data.chart_data_workbook

				wb.clear(0)

				series = chart.chart_data.series.add(ChartType.Histogram)
				series.data_points.AddDataPointForHistogramSeries(wb.get_cell(0, "A1", 15))
				series.data_points.AddDataPointForHistogramSeries(wb.get_cell(0, "A2", -41))
				series.data_points.AddDataPointForHistogramSeries(wb.get_cell(0, "A3", 16))
				series.data_points.AddDataPointForHistogramSeries(wb.get_cell(0, "A4", 10))
				series.data_points.AddDataPointForHistogramSeries(wb.get_cell(0, "A5", -23))
				series.data_points.AddDataPointForHistogramSeries(wb.get_cell(0, "A6", 16))

				chart.axes.horizontal_axis.AggregationType = AxisAggregationType.Automatic

				pres.save(dataDir+"Histogram.pptx", slides.export.SaveFormat.PPTX)
			}

		}

		#ExEnd:HistogramChart
	}
}
