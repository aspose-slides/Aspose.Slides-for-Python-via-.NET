using System.IO
using Aspose.slides.Export

/*
This example imports a PDF document into Presentation. 
A new SlideCollection.AddFromPdf method creates slides from the PDF document 
and adds them to the end of the collection
*/


namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    public class PdfImportExample
    {
        public static void Run()
        {
            dataDir = RunExamples.GetDataDir_Conversion()

            pdfFileName = Path.Combine(dataDir, "welcome-to-powerpoint.pdf")
            resultPath = Path.Combine(RunExamples.OutPath, "fromPdfDocument.pptx")

            with slides.Presentation() as pres:
            {
                pres.slides.AddFromPdf(pdfFileName)
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}