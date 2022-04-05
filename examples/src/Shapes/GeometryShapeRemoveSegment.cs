
using System.IO
import aspose.slides as slides

"""
This example demonstrates removing a segment from the existing geometry shape.
"""

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class GeometryShapeRemoveSegment
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "GeometryShapeRemoveSegment.pptx")

            with slides.Presentation() as pres:
            {
                # Create new shape
                GeometryShape shape = (GeometryShape)pres.slides[0].shapes.add_auto_shape(ShapeType.Heart, 100, 100, 300, 300)

                # Get geometry path of the shape
                IGeometryPath path = shape.GetGeometryPaths()[0]

                # remove segment
                path.remove_at(2)

                # set new geometry path
                shape.SetGeometryPath(path)

                # Save the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
