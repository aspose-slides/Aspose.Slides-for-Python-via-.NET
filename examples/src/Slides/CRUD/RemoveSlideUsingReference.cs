import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Slides
{
    public class RemoveSlideUsingReference
    {
        public static void Run()
        {
            #ExStart:RemoveSlideUsingReference
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_CRUD()

            # Instantiate a Presentation object that represents a presentation file
            using (Presentation pres = new Presentation(dataDir + "RemoveSlideUsingReference.pptx"))
            {

                # Accessing a slide using its index in the slides collection
                slide = pres.slides[0]

                # Removing a slide using its reference
                pres.slides.Remove(slide)

                #Writing the presentation file
                pres.save(dataDir + "modified_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:RemoveSlideUsingReference
        }
    }
}