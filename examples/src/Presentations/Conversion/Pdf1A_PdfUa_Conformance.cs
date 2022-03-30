using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export

/*
This example demonstrates saving presentation to PDF/A-1a and PDF/UA compliant document.
*/
namespace CSharp.Presentations.Conversion
{
    class Pdf1A_PdfUa_Conformance
    {
        public static void Run()
        {
            pptxFile = Path.Combine(RunExamples.GetDataDir_Conversion(), "tagged-pdf-demo.pptx")
            outPdf1aFile = Path.Combine(RunExamples.OutPath, "tagged-pdf-demo_1a.pdf")
            outPdf1bFile = Path.Combine(RunExamples.OutPath, "tagged-pdf-demo_1b.pdf")
            outPdfUaFile = Path.Combine(RunExamples.OutPath, "tagged-pdf-demo_1ua.pdf")

            using (Presentation presentation = new Presentation(pptxFile))
            {
                presentation.save(outPdf1aFile, SaveFormat.Pdf,
                    new PdfOptions { Compliance = PdfCompliance.PdfA1a })

                presentation.save(outPdf1bFile, SaveFormat.Pdf,
                    new PdfOptions { Compliance = PdfCompliance.PdfA1b })

                presentation.save(outPdfUaFile, SaveFormat.Pdf,
                    new PdfOptions { Compliance = PdfCompliance.PdfUa })
            }
        }
    }
}
