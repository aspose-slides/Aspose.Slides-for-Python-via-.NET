using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Background
{
    public class SetBackgroundToGradient
    {
        public static void Run()
        {
            #ExStart:SetBackgroundToGradient
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Background()

            # Instantiate the Presentation class that represents the presentation file
            using (Presentation pres = new Presentation(dataDir + "SetBackgroundToGradient.pptx"))
            {

                # Apply Gradiant effect to the Background
                pres.slides[0].Background.type = BackgroundType.OwnBackground
                pres.slides[0].Background.fill_format.fill_type = FillType.Gradient
                pres.slides[0].Background.FillFormat.GradientFormat.TileFlip = TileFlip.FlipBoth

                #Write the presentation to disk
                pres.save(dataDir + "ContentBG_Grad_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetBackgroundToGradient
        }
    }
}