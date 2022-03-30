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
The example shows of using read-only recommendation for presentation (this feature was introduced in PowerPoint 2019).
When enabled it makes PowerPoint to open the presentation in read-only mode first.
*/
namespace CSharp.Presentations.properties
{
    class ReadOnlyRecommended
    {
        public static void Run()
        {
            outPptxPath = Path.Combine(RunExamples.OutPath, "ReadOnlyRecommended.pptx")

            with slides.Presentation() as pres:
            {
                pres.ProtectionManager.ReadOnlyRecommended = True
                pres.save(outPptxPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
