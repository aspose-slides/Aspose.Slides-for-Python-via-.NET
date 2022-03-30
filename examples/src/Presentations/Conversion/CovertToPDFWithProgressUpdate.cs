import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Conversion
{
    class CovertToPDFWithProgressUpdate
    {
        public static void Run() {

            #ExStart:CovertToPDFWithProgressUpdate
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            using (Presentation presentation = new Presentation(dataDir + "ConvertToPDF.pptx"))
            {
                ISaveOptions saveOptions = new PdfOptions()
                saveOptions.ProgressCallback = new ExportProgressHandler()
                presentation.save(dataDir + "ConvertToPDF.pdf", SaveFormat.Pdf, saveOptions)
            }


            #ExEnd:CovertToPDFWithProgressUpdate
        }
    }

    #ExStart:ExportProgressHandler
    class ExportProgressHandler : IProgressCallback
    {
        public void Reporting(double progressValue)
        {
            # Use progress percentage value here
            progress = Convert.ToInt32(progressValue)
            print(progress + "% file converted")
        }
    }

    #ExEnd:ExportProgressHandler
}
