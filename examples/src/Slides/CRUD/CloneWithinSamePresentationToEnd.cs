using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/


namespace Aspose.slides.Examples.CSharp.slides.CRUD
{
    public class CloneWithinSamePresentationToEnd
    {
        public static void Run()
        {
            #ExStart:CloneWithinSamePresentationToEnd
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_CRUD()

            # Instantiate Presentation class that represents a presentation file
            using (Presentation pres = new Presentation(dataDir + "CloneWithinSamePresentationToEnd.pptx"))
            {

                # Clone the desired slide to the end of the collection of slides in the same presentation
                ISlideCollection slds = pres.Slides

                slds.AddClone(pres.slides[0])

                # Write the modified presentation to disk
                pres.save(dataDir + "Aspose_CloneWithinSamePresentationToEnd_out.pptx", slides.export.SaveFormat.PPTX)

            }
            #ExEnd:CloneWithinSamePresentationToEnd
        }
    }
}