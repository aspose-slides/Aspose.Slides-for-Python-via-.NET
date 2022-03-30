using System.IO
using Aspose.slides.Export

/*
The example demonstrates creation a composite custom shape from two GeometryPath objects.
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class GeometryShapeCompositeObjects
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "GeometryShapeCompositeObjects.pptx")

            with slides.Presentation() as pres:
            {
                # Create new shape
                GeometryShape shape = (GeometryShape)pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 200, 100)

                # Create first geometry path
                GeometryPath geometryPath0 = new GeometryPath()
                geometryPath0.MoveTo(0, 0)
                geometryPath0.LineTo(shape.width, 0)
                geometryPath0.LineTo(shape.width, shape.height / 3)
                geometryPath0.LineTo(0, shape.height / 3)
                geometryPath0.CloseFigure()

                # Create second geometry path
                GeometryPath geometryPath1 = new GeometryPath()
                geometryPath1.MoveTo(0, shape.height / 3 * 2)
                geometryPath1.LineTo(shape.width, shape.height / 3 * 2)
                geometryPath1.LineTo(shape.width, shape.height)
                geometryPath1.LineTo(0, shape.height)
                geometryPath1.CloseFigure()

                # Set shape geometry as composition of two geometry path
                shape.SetGeometryPaths(new GeometryPath[] { geometryPath0, geometryPath1 })

                # Save the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
