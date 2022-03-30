import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.Import
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Saving
{
    class AddImageFromSVGObjectFromExternalResource
    {
        public static void Run() {

            #ExStart:AddImageFromSVGObjectFromExternalResource
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_PresentationSaving()
            outPptxPath = dataDir + "presentation_external.pptx"

            using (p = new Presentation())
            {
                svgContent = File.ReadAllText(new Uri(new Uri(dataDir), "image1.svg").AbsolutePath)
                ISvgImage svgImage = new SvgImage(svgContent, new ExternalResourceResolver(), dataDir)
                ppImage = p.images.add_image(svgImage)
                p.slides[0].shapes.AddPictureFrame(ShapeType.Rectangle, 0, 0, ppImage.width, ppImage.height, ppImage)
                p.save(outPptxPath, slides.export.SaveFormat.PPTX)
            }

            #ExEnd:AddImageFromSVGObjectFromExternalResource
        }
    }
}
