using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

/*
The example demonstrates loading and saving presentation in Fodp format.
*/
namespace CSharp.Presentations.Conversion
{
    class FodpFormatConvertion
    {
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Conversion()
            outFodpPath = Path.Combine(RunExamples.OutPath, "FodpFormatConvertion.fodp")
            outPptxPath = Path.Combine(RunExamples.OutPath, "FodpFormatConvertion.pptx")

            using (Presentation presentation = new Presentation(dataDir + "Example.fodp"))
            {
                presentation.save(outPptxPath, slides.export.SaveFormat.PPTX)
            }

            using (Presentation pres = new Presentation(outPptxPath))
            {
                pres.save(outFodpPath, SaveFormat.Fodp)
            }
        }
    }
}
