import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Rendering_Printing
{
	public class RenderingEmoji
	{
		#ExStart:RenderingEmoji
		public static void Run()
		{
			dataDir = RunExamples.GetDataDir_Rendering()

			Presentation pres = new Presentation(dataDir+"input.pptx")

			pres.save(dataDir+"emoji.pdf",Aspose.slides.Export.SaveFormat.Pdf)
         }

	}
      #ExEnd:RenderingEmoji
}
