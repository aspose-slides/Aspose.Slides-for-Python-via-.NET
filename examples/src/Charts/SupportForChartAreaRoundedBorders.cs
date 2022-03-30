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
	class SupportForChartAreaRoundedBorders
	{
		public static void Run()
		{
			#ExStart:SupportForChartAreaRoundedBorders
			dataDir = RunExamples.GetDataDir_Charts()
			with slides.Presentation() as presentation:
			{
				slide = presentation.slides[0]
				chart = slide.shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 20, 100, 600, 400)
				chart.line_format.fill_format.fill_type = slides.FillType.SOLID
				chart.line_format.style = LineStyle.Single
				chart.HasRoundedCorners = True

				presentation.save(dataDir + "out.pptx", slides.export.SaveFormat.PPTX)
			}
		}	
		#ExEnd:SupportForChartAreaRoundedBorders
	}
}
