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
	class SupportForPrecisionOfData
	{
         	public static void Run()
			{
			#ExStart:SupportForPrecisionOfData
			# The path to the documents directory.
			    dataDir = RunExamples.GetDataDir_Charts()

			    with slides.Presentation() as pres:
			    {
				chart = pres.slides[0].shapes.add_chart(slides.charts.ChartType.Line, 50, 50, 450, 300)
				chart.HasDataTable = True
				chart.chart_data.series[0].NumberFormatOfValues = "#,##0.00"

				pres.save(dataDir + "PrecisionOfDatalabels_out.pptx", slides.export.SaveFormat.PPTX)

     			}
			#ExEnd:SupportForPrecisionOfData
		       }
	        }
		}
	


