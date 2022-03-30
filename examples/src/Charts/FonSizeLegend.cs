using Aspose.slides.Charts
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{

	public class FontSizeLegend
	{
		public static void Run()
		{
			#ExStart:FontSizeLegend
			# The path to the documents directory.
			dataDir = RunExamples.GetDataDir_Charts()

			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
			{
				chart = pres.slides[0].shapes.AddChart(Aspose.slides.Charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

				chart.legend.text_format.portion_format.font_height = 20

				chart.axes.vertical_axis.is_automatic_min_value = False

				chart.axes.vertical_axis.min_value = -5

				chart.axes.vertical_axis.is_automatic_max_value = False

				chart.axes.vertical_axis.max_value = 10

				pres.save(dataDir+"output.pptx", slides.export.SaveFormat.PPTX)
			}

			#ExEnd:FontSizeLegend
		}
	}
}
	