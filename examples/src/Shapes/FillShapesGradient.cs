using System.IO

import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FillShapesGradient
    {
        public static void Run()
        {
            #ExStart:FillShapesGradient
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX# Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of ellipse type
                IShape shp = sld.shapes.add_auto_shape(ShapeType.Ellipse, 50, 150, 75, 150)

                # Apply some gradiant formatting to ellipse shape
                shp.FillFormat.fill_type = FillType.Gradient
                shp.FillFormat.GradientFormat.GradientShape = GradientShape.Linear

                # Set the Gradient Direction
                shp.FillFormat.GradientFormat.GradientDirection = GradientDirection.FromCorner2

                # Add two Gradiant Stops
                shp.FillFormat.GradientFormat.GradientStops.add((float)1.0, PresetColor.Purple)
                shp.FillFormat.GradientFormat.GradientStops.add((float)0, PresetColor.Red)

                #Write the PPTX file to disk
                pres.save(dataDir + "EllipseShpGrad_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FillShapesGradient
        }
    }
}