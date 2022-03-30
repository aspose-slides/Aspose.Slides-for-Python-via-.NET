﻿import aspose.pydrawing as drawing
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    class ConvertSlidesToPdfNotes
    {
        public static void Run()
        {
            #ExStart:ConvertSlidesToPdfNotes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            # Instantiate a Presentation object that represents a presentation file 
            Presentation presentation = new Presentation(dataDir + "SelectedSlides.pptx")
            Presentation auxPresentation = new Presentation()

            slide = presentation.slides[0]

            auxPresentation.slides.insert_clone(0, slide)

            # Setting Slide Type and Size 
            #auxPresentation.SlideSize.SetSize(presentation.SlideSize.size.width, presentation.SlideSize.size.height,SlideSizeScaleType.EnsureFit)
            auxPresentation.SlideSize.SetSize(612F, 792F,SlideSizeScaleType.EnsureFit)


            PdfOptions pdfOptions = new PdfOptions()
            INotesCommentsLayoutingOptions options = pdfOptions.NotesCommentsLayouting
            options.NotesPosition = NotesPositions.BottomFull



            auxPresentation.save(dataDir + "PDFnotes_out.pdf", SaveFormat.Pdf, pdfOptions)
            #ExEnd:ConvertSlidesToPdfNotes
        }
    }
}
