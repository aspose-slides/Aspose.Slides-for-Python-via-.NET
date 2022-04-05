using System.IO

import aspose.slides as slides
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class RotatingShapes
    {
        public static void Run()
        {
            #ExStart:RotatingShapes
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PrseetationEx class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of rectangle type
                shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

                # Rotate the shape to 90 degree
                shp.rotation = 90

                # Write the PPTX file to disk
                pres.save(dataDir + "RectShpRot_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:RotatingShapes
        }
    }
}