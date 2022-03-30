import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Conversion
{
	class ExportShapeToSVG
	{
		#ExStart:ExportShapeToSVG
		public static void Run()
		{
			
			outSvgFileName = "SingleShape.svg"
			dataDir = RunExamples.GetDataDir_Conversion()
			using (Presentation pres = new Presentation(dataDir+ "TestExportShapeToSvg.pptx"))
			{
				using (Stream stream = new FileStream(outSvgFileName, FileMode.Create, FileAccess.Write))
				{
					pres.slides[0].shapes[0].WriteAsSvg(stream)

					
				}
			
				
			}


		}


		#ExEnd:ExportShapeToSVG
	}
}