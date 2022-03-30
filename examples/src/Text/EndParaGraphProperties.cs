import aspose.pydrawing as drawing
import aspose.slides as slides
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class EndParaGraphProperties
    {
        public static void Run()
        {
            #ExStart:EndParaGraphProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            with slides.Presentation() as pres:
        {
             shape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 10, 10, 200, 250)

             Paragraph para1 = new Paragraph()
             para1.portions.add(new Portion("Sample text"))

             Paragraph para2 = new Paragraph()
             para2.portions.add(new Portion("Sample text 2"))
             PortionFormat endParagraphPortionFormat = new PortionFormat()
             endParagraphPortionFormat.font_height = 48
             endParagraphPortionFormat.latin_font = slides.FontData("Times New Roman")
             para2.EndParagraphPortionFormat = endParagraphPortionFormat

             shape.text_frame.Paragraphs.add(para1)
             shape.text_frame.Paragraphs.add(para2)

             pres.save(RunExamples.OutPath + "pres.pptx", slides.export.SaveFormat.PPTX)
            }
            }
            #ExEnd:EndParaGraphProperties
        }
    }

