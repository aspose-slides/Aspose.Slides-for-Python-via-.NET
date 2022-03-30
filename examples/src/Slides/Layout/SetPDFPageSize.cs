using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Layout
{
    class SetPDFPageSize
    {
        public static void Run()
        {
            #ExStart:SetPDFPageSize
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Layout()

            # Instantiate a Presentation object that represents a presentation file 
            with slides.Presentation() as presentation:

            # Set SlideSize.type Property 
            presentation.SlideSize.SetSize(SlideSizeType.A4Paper,SlideSizeScaleType.EnsureFit)

            # Set different properties of PDF Options
            PdfOptions opts = new  PdfOptions()
            opts.SufficientResolution = 600

            # Save presentation to disk
            presentation.save(dataDir + "SetPDFPageSize_out.pdf", SaveFormat.Pdf, opts)
            #ExEnd:SetPDFPageSize
        }
    }
}