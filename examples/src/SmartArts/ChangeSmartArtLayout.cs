using Aspose.slides.SmartArt
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    class ChangeSmartArtLayout
    {
        public static void Run()
        {
            #ExStart:ChangeSmartArtLayout
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            with slides.Presentation() as presentation:
            {
                # Add SmartArt BasicProcess 
                ISmartArt smart = presentation.slides[0].shapes.AddSmartArt(10, 10, 400, 300, SmartArtLayoutType.BasicBlockList)

                # Change LayoutType to BasicProcess
                smart.Layout = SmartArtLayoutType.BasicProcess

                # Saving Presentation
                presentation.save(dataDir + "ChangeSmartArtLayout_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ChangeSmartArtLayout
        }
    }
}
