using Aspose.slides.Export


/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Conversion
{
    public class RenderingNotesWhileConvertingToHTML
    {
        public static void Run()
        {
            #ExStart:RenderingNotesWhileConvertingToHTML
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            using (Presentation pres = new Presentation(dataDir + "Presentation.pptx"))
            {
                HtmlOptions opt = new HtmlOptions()

                INotesCommentsLayoutingOptions options = opt.NotesCommentsLayouting
                options.NotesPosition = NotesPositions.BottomFull

                # Saving notes pages
                pres.save(dataDir + "Output.html", SaveFormat.Html, opt)
            }
            #ExEnd:RenderingNotesWhileConvertingToHTML
        }
    }
}