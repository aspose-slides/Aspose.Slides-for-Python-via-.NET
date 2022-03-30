import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
	class SupportForChangingSeriesColor
	{
		public static void Run()
		{
			#ExStart:SupportForChangingSeriesColor
			# The path to the documents directory.
			dataDir = RunExamples.GetDataDir_Charts()

			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
			{
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.PIE, 50, 50, 600, 400)

				point = chart.chart_data.series[0].data_points[1]

				point.explosion = 30

				point.format.fill.fill_type = slides.FillType.SOLID

				point.format.fill.solid_fill_color.color = drawing.Color.blue


				pres.save(dataDir+"output.pptx", slides.export.SaveFormat.PPTX)
			}
			#ExEnd:SupportForChangingSeriesColor

		}
	}
}