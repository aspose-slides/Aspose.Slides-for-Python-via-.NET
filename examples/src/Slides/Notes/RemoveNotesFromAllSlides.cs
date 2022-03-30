using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Notes
{
    class RemoveNotesFromAllSlides
    {
        public static void Run()
        {
            #ExStart:RemoveNotesFromAllSlides
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Notes()

            # Instantiate a Presentation object that represents a presentation file 
            Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx")

            # Removing notes of all slides
            INotesSlideManager mgr = None
            for (i = 0 i < presentation.slides.Count i++)
            {
                mgr = presentation.slides[i].NotesSlideManager
                mgr.RemoveNotesSlide()
            }
            # Save presentation to disk
            presentation.save(dataDir + "RemoveNotesFromAllSlides_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:RemoveNotesFromAllSlides
        }
    }
}