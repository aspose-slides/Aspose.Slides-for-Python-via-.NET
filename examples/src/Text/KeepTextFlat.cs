using System
using System.Collections.Generic
using System.Data
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Charts
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using DataTable = System.Data.DataTable

namespace CSharp.Presentations.Conversion
{
    # This example demonstrates setting keep text out of 3D scene.

    public class KeepTextFlat
    {
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Text()
            pptxFileName = Path.Combine(dataDir, "KeepTextFlat.pptx")
            resultPath = Path.Combine(RunExamples.OutPath, "KeepTextFlat_out.png")

            using (Presentation pres = new Presentation(pptxFileName))
            {
                shape1 = pres.slides[0].shapes[0] as AutoShape
                shape2 = pres.slides[0].shapes[1] as AutoShape

                shape1.text_frame.TextFrameFormat.KeepTextFlat = False
                shape2.text_frame.TextFrameFormat.KeepTextFlat = True

                pres.slides[0].get_thumbnail(4 / 3f, 4 / 3f).save(resultPath, drawing.imaging.ImageFormat.png)
            }
        }
    }
}
