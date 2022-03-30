import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
	class GetChartImage
	{
		public static void Run()
		{
			#ExStart:GetChartImage
			# The path to the documents directory.
			dataDir = RunExamples.GetDataDir_Charts()

			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
            {
            	chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)
             	Image img = chart.GetThumbnail()
             	img.save(dataDir+"image.png", ImageFormat.Png)
			}
			#ExEnd:GetChartImage
		}
	}
}
