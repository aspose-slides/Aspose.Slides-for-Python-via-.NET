import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Hyperlinks
{
    class SetHyperLinkColor
    {
        public static void Run() {

            #ExStart:SetHyperLinkColor
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Hyperlink()
            with slides.Presentation() as presentation:
            {
                shape1 = presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 450, 50, False)
                shape1.AddTextFrame("This is a sample of colored hyperlink.")
                shape1.text_frame.paragraphs[0].portions[0].portion_format.HyperlinkClick = new Hyperlink("https:#www.aspose.com/")
                shape1.text_frame.paragraphs[0].portions[0].portion_format.HyperlinkClick.ColorSource = HyperlinkColorSource.portion_format
                shape1.text_frame.paragraphs[0].portions[0].portion_format.fill_format.fill_type = slides.FillType.SOLID
                shape1.text_frame.paragraphs[0].portions[0].portion_format.fill_format.solid_fill_color.color = drawing.Color.red

                shape2 = presentation.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 200, 450, 50, False)
                shape2.AddTextFrame("This is a sample of usual hyperlink.")
                shape2.text_frame.paragraphs[0].portions[0].portion_format.HyperlinkClick = new Hyperlink("https:#www.aspose.com/")

                presentation.save(dataDir+"presentation-out-hyperlink.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetHyperLinkColor
        }
    }
}
