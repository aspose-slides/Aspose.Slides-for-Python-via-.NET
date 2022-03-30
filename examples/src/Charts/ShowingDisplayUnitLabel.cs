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
	class ShowingDisplayUnitLabel
	{
		public static void Run()
		{
			#ExStart:ShowingDisplayUnitLabel
			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir+"Test.pptx"))
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 450, 300)
				chart.axes.vertical_axis.display_unit = slides.charts.DisplayUnitType.Millions
				pres.save(dataDir + "Result.pptx", slides.export.SaveFormat.PPTX)

			}
            #ExEnd:ShowingDisplayUnitLabel
		}
	}
}