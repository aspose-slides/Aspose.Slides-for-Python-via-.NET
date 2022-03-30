using System.IO
import aspose.slides as slides
using Aspose.slides.SmartArt

namespace Aspose.slides.Examples.CSharp.SmartArts
{
    public class CreateSmartArtShape
    {
        public static void Run()
        {
            #ExStart:CreateSmartArtShape
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)
            # Instantiate the presentation
            with slides.Presentation() as pres:
            {

                # Access the presentation slide
                slide = pres.slides[0]

                # Add Smart Art Shape
                ISmartArt smart = slide.shapes.AddSmartArt(0, 0, 400, 400, SmartArtLayoutType.BasicBlockList)

                # Saving presentation
                pres.save(dataDir + "SimpleSmartArt_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:CreateSmartArtShape
        }
    }
}