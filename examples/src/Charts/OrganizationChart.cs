import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.SmartArt
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Charts
{
	public class OrganizationChart
	{
		#ExStart:OrganizationChart
		public static void Run()
			 {
			
			# The path to the documents directory.
			dataDir = RunExamples.GetDataDir_Charts()
				using (Presentation pres = new Presentation(dataDir+"test.pptx"))
				{
					ISmartArt smartArt = pres.slides[0].shapes.AddSmartArt(0, 0, 400, 400, SmartArtLayoutType.PictureOrganizationChart)

					pres.save(dataDir+"OrganizationChart.pptx", slides.export.SaveFormat.PPTX)
				}			

			}
		#ExEnd:OrganizationChart
	    }
	}
