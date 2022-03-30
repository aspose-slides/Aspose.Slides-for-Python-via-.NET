using System
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.IO
import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class SaveWithDefaaultRegularFont
    {
        #/ <summary>
        #/ The code below demonstrates saving presentation to Html and Pdf with different default regular font.
        #/ </summary>
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Text()
            outPath = RunExamples.OutPath

            using (Presentation pres = new Presentation(dataDir + "DefaultFonts.pptx"))
            {
                HtmlOptions htmlOpts = new HtmlOptions()
                htmlOpts.DefaultRegularFont = "Arial Black"
                pres.save(outPath + "Presentation-out-ArialBlack.html", SaveFormat.Html, htmlOpts)
                htmlOpts.DefaultRegularFont = "Lucida Console"
                pres.save(outPath + "Presentation-out-LucidaConsole.html", SaveFormat.Html, htmlOpts)

                PdfOptions pdfOpts = new PdfOptions()
                pdfOpts.DefaultRegularFont = "Arial Black"
                pres.save(outPath + "Presentation-out-ArialBlack.pdf", SaveFormat.Pdf, pdfOpts)
            }
        }
    }
}