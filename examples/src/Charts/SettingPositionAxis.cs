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
	class SettingPositionAxis
	{
		public static void Run()
		{
			#ExStart:SettingPositionAxis
			dataDir = RunExamples.GetDataDir_Charts()
			with slides.Presentation() as pres:
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 450, 300)
				chart.axes.horizontal_axis.AxisBetweenCategories = True

				pres.save(dataDir + "AsposeScatterChart.pptx", slides.export.SaveFormat.PPTX)

			}
            #ExEnd:SettingPositionAxis

        }
    }
}