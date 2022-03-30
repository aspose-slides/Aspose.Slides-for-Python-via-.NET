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
    class SetTransitionEffects
    {
        public static void Run()
        {
            #ExStart:SetTransitionEffects
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Transitions()

            # Create an instance of Presentation class
            Presentation presentation = new Presentation(dataDir + "AccessSlides.pptx")

            # Set effect
            presentation.slides[0].SlideShowTransition.type = TransitionType.Cut
            ((OptionalBlackTransition)presentation.slides[0].SlideShowTransition.value).FromBlack = True

            # Write the presentation to disk
            presentation.save(dataDir + "SetTransitionEffects_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:SetTransitionEffects
        }
    }
}