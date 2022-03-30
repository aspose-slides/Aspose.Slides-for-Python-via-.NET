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
	class SettingFontProperties
	{
		public static void Run()
		{
			#ExStart:SettingFontProperties
			dataDir = RunExamples.GetDataDir_Charts()
			using (Presentation pres = new Presentation(dataDir+"test.pptx"))
			{

				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.CLUSTERED_COLUMN, 50, 50, 600, 400)

				chart.HasDataTable = True

				chart.ChartDataTable.text_format.portion_format.font_bold = 1
				chart.ChartDataTable.text_format.portion_format.font_height = 20

				pres.save(dataDir+"output.pptx", slides.export.SaveFormat.PPTX)

			}
		}
		#ExEnd:SettingFontProperties
	}
}