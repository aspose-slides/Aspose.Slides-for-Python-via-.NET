using Aspose.slides.Export
using Aspose.slides.SlideShow

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Transitions
{
    class ManageSimpleSlideTransitions
    {
        public static void Run()
        {
            #ExStart:ManageSimpleSlideTransitions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Transitions()

            # Instantiate Presentation class to load the source presentation file
            using (Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx"))
            {
                # Apply circle type transition on slide 1
                presentation.slides[0].SlideShowTransition.type = TransitionType.Circle

                # Apply comb type transition on slide 2
                presentation.slides[1].SlideShowTransition.type = TransitionType.Comb

                # Write the presentation to disk
                presentation.save(dataDir + "SampleTransition_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ManageSimpleSlideTransitions
        }
    }
}