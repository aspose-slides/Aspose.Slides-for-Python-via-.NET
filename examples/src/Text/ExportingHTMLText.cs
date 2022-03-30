using System.IO
using System.text
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    public class ExportingHTMLText
    {
        public static void Run()
        {
            #ExStart:ExportingHTMLText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Load the presentation file
            using (Presentation pres = new Presentation(dataDir + "ExportingHTMLText.pptx"))
            {

                # Acesss the default first slide of presentation
                slide = pres.slides[0]

                # Desired index
                index = 0

                # Accessing the added shape
                ashape = (IAutoShape)slide.shapes[index]

                StreamWriter sw = new StreamWriter(dataDir + "output_out.html", False, Encoding.UTF8)

                #Writing Paragraphs data to HTML by providing paragraph starting index, total paragraphs to be copied
                sw.Write(ashape.text_frame.Paragraphs.ExportToHtml(0, ashape.text_frame.Paragraphs.Count, None))

                sw.Close()
            }
            #ExEnd:ExportingHTMLText
        }
    }
}