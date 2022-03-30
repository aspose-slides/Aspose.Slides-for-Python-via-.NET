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
	class SettingRotationAngle
	{
		public static void Run()
		{
			#ExStart:SettingRotationAngle
			# The path to the documents directory.
			dataDir = RunExamples.GetDataDir_Charts()
			with slides.Presentation() as pres:
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 450, 300)
				chart.axes.vertical_axis.has_title = True
                chart.axes.vertical_axis.title.text_format.text_block_format.RotationAngle = 90

				pres.save(dataDir + "test.pptx", slides.export.SaveFormat.PPTX)
			}
		    #ExEnd:SettingRotationAngle

		}
	}
}