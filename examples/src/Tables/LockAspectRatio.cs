import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Tables
{
    class LockAspectRatio
    {
        public static void Run()
        {
            #ExStart:LockAspectRatio
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            using (Presentation pres = new Presentation(dataDir + "pres.pptx"))
            {
                ITable table = (ITable)pres.slides[0].shapes[0]
                print("Lock aspect ratio set: {0}", table.ShapeLock.AspectRatioLocked)

                table.ShapeLock.AspectRatioLocked = !table.ShapeLock.AspectRatioLocked # invert

                print("Lock aspect ratio set: {0}", table.ShapeLock.AspectRatioLocked)

                pres.save(dataDir + "pres-out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:LockAspectRatio

        }
    }
}
