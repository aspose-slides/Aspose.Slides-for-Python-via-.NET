import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
	class SupportForBubbleChartScaling
	{
		public static void Run()
		{
			#ExStart:SupportForBubbleChartScaling
			dataDir = RunExamples.GetDataDir_Charts()
			with slides.Presentation() as pres:
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.BUBBLE, 100, 100, 400, 300)

				chart.chart_data.SeriesGroups[0].BubbleSizeScale = 150

				pres.save(dataDir+"Result.pptx",slides.export.SaveFormat.PPTX)
			}

			#ExEnd:SupportForBubbleChartScaling

		}
	}
}