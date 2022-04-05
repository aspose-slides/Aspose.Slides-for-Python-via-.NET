using System.IO

import aspose.slides as slides
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class SimpleEllipse
    {
        public static void Run()
        {
            #ExStart:SimpleEllipse
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of ellipse type
                sld.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 50, 150, 150, 50)

                #Write the PPTX file to disk
                pres.save(dataDir + "EllipseShp1_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SimpleEllipse
        }
    }
}