import aspose.slides as slides
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Hyperlinks
{
    class AddHyperlink
    {
        public static void Run() {

            #ExStart:AddHyperlink

            with slides.Presentation() as presentation:
            {
                shape1 = presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 600, 50, False)
                shape1.AddTextFrame("Aspose: File Format APIs")
                shape1.text_frame.paragraphs[0].portions[0].portion_format.HyperlinkClick = new Hyperlink("https:#www.aspose.com/")
                shape1.text_frame.paragraphs[0].portions[0].portion_format.HyperlinkClick.Tooltip = "More than 70% Fortune 100 companies trust Aspose APIs"
                shape1.text_frame.paragraphs[0].portions[0].portion_format.font_height = 32

                presentation.save("presentation-out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddHyperlink
        }
    }
}
