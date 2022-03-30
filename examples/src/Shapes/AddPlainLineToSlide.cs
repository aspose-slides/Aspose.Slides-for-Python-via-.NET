using System.IO
import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AddPlainLineToSlide
    {
        public static void Run()
        {
            #ExStart:AddPlainLineToSlide
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PresentationEx class that represents the PPTX file
            with slides.Presentation() as pres:
            {
                # Get the first slide
                sld = pres.slides[0]

                # Add an autoshape of type line
                sld.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)

                #Write the PPTX to Disk
                pres.save(dataDir + "LineShape1_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddPlainLineToSlide
        }
    }
}