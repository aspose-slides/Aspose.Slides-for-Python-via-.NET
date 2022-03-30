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
	class FontPropertiesForInvidualLegend
	{
		public static void Run()
		{

			#ExStart:FontPropertiesForInvidualLegend
			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
          {
               chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

				IChartTextFormat tf = chart.legend.Entries[1].TextFormat

				tf.portion_format.font_bold = 1

				tf.portion_format.font_height = 20

				tf.portion_format.font_italic = 1

				tf.portion_format.fill_format.fill_type = slides.FillType.SOLID 

				tf.portion_format.fill_format.solid_fill_color.color = drawing.Color.blue
				pres.save(dataDir+"output.pptx", slides.export.SaveFormat.PPTX)

			}
			#ExEnd:FontPropertiesForInvidualLegend
		}
	}
}
