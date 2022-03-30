import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Saving
{
    class AddImageFromSVGObject
    {
        public static void Run() {

            #ExStart:AddImageFromSVGObject
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationSaving()
            svgPath = dataDir + "sample.svg"
            outPptxPath = dataDir + "presentation.pptx"
            using (p = new Presentation())
            {
                svgContent = File.ReadAllText(svgPath)
                ISvgImage svgImage = new SvgImage(svgContent)
                ppImage = p.images.add_image(svgImage)
                p.slides[0].shapes.AddPictureFrame(ShapeType.Rectangle, 0, 0, ppImage.width, ppImage.height, ppImage)
                p.save(outPptxPath, slides.export.SaveFormat.PPTX)
            }

            #ExEnd:AddImageFromSVGObject
        }
    }
}
