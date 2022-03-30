using System
using Aspose.slides.SmartArt
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
    class AccessSmartArtParticularLayout
    {
        public static void Run()
        {
            #ExStart:AccessSmartArtParticularLayout
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            using (Presentation presentation = new Presentation(dataDir + "AccessSmartArtShape.pptx"))
            {
                # Traverse through every shape inside first slide
                foreach (IShape shape in presentation.slides[0].shapes)
                {
                    # Check if shape is of SmartArt type
                    if (shape is ISmartArt)
                    {
                        # Typecast shape to SmartArtEx
                        ISmartArt smart = (ISmartArt) shape

                        # Checking SmartArt Layout
                        if (smart.Layout == SmartArtLayoutType.BasicBlockList)
                        {
                            print("Do some thing here....")
                        }
                    }
                }
            }
            #ExEnd:AccessSmartArtParticularLayout
        }
    }
}
