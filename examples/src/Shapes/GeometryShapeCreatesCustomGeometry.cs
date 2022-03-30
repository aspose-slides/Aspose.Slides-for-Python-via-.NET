
using System
using System.Collections.Generic
using System.Diagnostics
import aspose.pydrawing as drawing
using System.IO
using Aspose.slides.Export

/*
The example demonstrates creation a shape with completely custom geometry.
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class GeometryShapeCreatesCustomGeometry
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "GeometryShapeCreatesCustomGeometry.pptx")

            R = 100, r = 50 # Outer and inner star radius

            # Create star geometry path
            GeometryPath starPath = CreateStarGeometry(R, r)

            with slides.Presentation() as pres:
            {
                # Create new shape
                GeometryShape shape = (GeometryShape)pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, R * 2, R * 2)

                # Set new geometry path to the shape
                shape.SetGeometryPath(starPath)

                # Save the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }

        #/ <summary>
        #/ Creates star geometry path.
        #/ </summary>
        #/ <param name="outerRadius">Outet radius of a star figure.</param>
        #/ <param name="innerRadiusr">inner radius of a star figure.</param>
        #/ <returns>Geometry Path</returns>
        private static GeometryPath CreateStarGeometry(outerRadius, innerRadiusr)
        {
            GeometryPath starPath = new GeometryPath()
            List<PointF> points = new List<PointF>()

            step = 72

            for (angle = -90 angle < 270 angle += step)
            {
                radians = angle * (Math.PI / 180f)
                x = outerRadius * Math.Cos(radians)
                y = outerRadius * Math.Sin(radians)
                points.add(new PointF((float)x + outerRadius, (float)y + outerRadius))

                radians = Math.PI * (angle + step / 2) / 180.0
                x = innerRadiusr * Math.Cos(radians)
                y = innerRadiusr * Math.Sin(radians)
                points.add(new PointF((float)x + outerRadius, (float)y + outerRadius))
            }

            starPath.MoveTo(points[0])

            for (i = 1 i < points.Count i++)
            {
                starPath.LineTo(points[i])
            }

            starPath.CloseFigure()

            return starPath
        }
    }
}
