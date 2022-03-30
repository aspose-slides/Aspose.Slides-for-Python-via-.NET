import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.properties
{
    class AccessLayoutFormats
    {
        public static void Run() {

            #ExStart:AccessLayoutFormats

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationProperties()

            using (Presentation pres = new Presentation(dataDir + "pres.pptx"))
            {
                foreach (ILayoutSlide layoutSlide in pres.LayoutSlides)
                {
                    IFillFormat[] fillFormats = layoutSlide.shapes.Select(shape => shape.FillFormat).ToArray()
                    ILineFormat[] lineFormats = layoutSlide.shapes.Select(shape => shape.line_format).ToArray()
                }
            }
            #ExEnd:AccessLayoutFormats

        }

    }
}
