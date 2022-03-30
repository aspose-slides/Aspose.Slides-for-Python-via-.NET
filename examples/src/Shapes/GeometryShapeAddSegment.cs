using System.IO

import aspose.slides as slides
using Aspose.slides.Export

/*
This example demonstrates adding new segment to the existing geometry shape.
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class GeometryShapeAddSegment
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "GeometryShapeAddSegment.pptx")

            with slides.Presentation() as pres:
            {
                # Create new shape
                GeometryShape shape = (GeometryShape)pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 200, 100)
                # Get geometry path of the shape
                IGeometryPath geometryPath = shape.GetGeometryPaths()[0]

                # Add two lines to geometry path
                geometryPath.LineTo(100, 50, 1)
                geometryPath.LineTo(100, 50, 4)

                # Assign edited geometry path to the shape
                shape.SetGeometryPath(geometryPath)

                # Save the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
