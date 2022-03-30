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
    class CheckSmartArtHiddenProperty
    {
        public static void Run()
        {
            #ExStart:CheckSmartArtHiddenProperty
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            with slides.Presentation() as presentation:
            {
                # Add SmartArt BasicProcess 
                ISmartArt smart = presentation.slides[0].shapes.AddSmartArt(10, 10, 400, 300, SmartArtLayoutType.RadialCycle)

                # Add node on SmartArt 
                ISmartArtNode node = smart.AllNodes.AddNode()

                # Check isHidden property
                bool hidden = node.IsHidden # Returns True

                if (hidden)
                {
                    # Do some actions or notifications
                }
                # Saving Presentation
                presentation.save(dataDir + "CheckSmartArtHiddenProperty_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:CheckSmartArtHiddenProperty
        }
    }
}
