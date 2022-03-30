using Aspose.slides.SlideShow
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Transitions
{
    public class SimpleSlideTransitions
    {
        public static void Run()
        {
            #ExStart:SimpleSlideTransitions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Transitions()

            # Instantiate Presentation class that represents a presentation file
            using (Presentation pres = new Presentation(dataDir + "SimpleSlideTransitions.pptx"))
            {

                # Apply circle type transition on slide 1
                pres.slides[0].SlideShowTransition.type = TransitionType.Circle

                # Apply comb type transition on slide 2
                pres.slides[1].SlideShowTransition.type = TransitionType.Comb

                # Write the presentation to disk
                pres.save(dataDir + "SampleTransition_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SimpleSlideTransitions
        }
    }
}