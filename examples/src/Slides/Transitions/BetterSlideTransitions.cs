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
    public class BetterSlideTransitions
    {
        public static void Run()
        {
            #ExStart:BetterSlideTransitions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Transitions()

            # Instantiate Presentation class that represents a presentation file
            using (Presentation pres = new Presentation(dataDir + "BetterSlideTransitions.pptx"))
            {

                # Apply circle type transition on slide 1
                pres.slides[0].SlideShowTransition.type = TransitionType.Circle


                # Set the transition time of 3 seconds
                pres.slides[0].SlideShowTransition.AdvanceOnClick = True
                pres.slides[0].SlideShowTransition.AdvanceAfterTime = 3000

                # Apply comb type transition on slide 2
                pres.slides[1].SlideShowTransition.type = TransitionType.Comb


                # Set the transition time of 5 seconds
                pres.slides[1].SlideShowTransition.AdvanceOnClick = True
                pres.slides[1].SlideShowTransition.AdvanceAfterTime = 5000

                # Apply zoom type transition on slide 3
                pres.slides[2].SlideShowTransition.type = TransitionType.Zoom


                # Set the transition time of 7 seconds
                pres.slides[2].SlideShowTransition.AdvanceOnClick = True
                pres.slides[2].SlideShowTransition.AdvanceAfterTime = 7000

                # Write the presentation to disk
                pres.save(dataDir + "SampleTransition_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:BetterSlideTransitions
        }
    }
}