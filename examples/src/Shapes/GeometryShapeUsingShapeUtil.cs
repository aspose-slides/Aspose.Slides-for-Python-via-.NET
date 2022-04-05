
import aspose.pydrawing as drawing
using System.Drawing.Drawing2D
using System.IO
import aspose.slides as slides
using Aspose.slides.Util

"""
The example demonstrates using of ShapeUtil for editing shape geometry as System.Drawing.Drawing2D.GrpahicsPath object.
"""

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class GeometryShapeUsingShapeUtil
    {
        public static void Run()
        {
            # Output file name
            resultPath = Path.Combine(RunExamples.OutPath, "GeometryShapeUsingShapeUtil.pptx")

            with slides.Presentation() as pres:
            {
                # Create new shape
                GeometryShape shape = (GeometryShape)pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 100)

                # Get geometry path of the shape
                IGeometryPath originalPath = shape.GetGeometryPaths()[0]
                originalPath.FillMode = PathFillModeType.NONE

                # Create new graphics path with text
                GraphicsPath graphicsPath = new GraphicsPath()
                graphicsPath.AddString("Text in shape", new FontFamily("Arial"), 1, 40, new PointF(10, 10), StringFormat.GenericDefault)

                # Convert graphics path to geometry path
                IGeometryPath textPath = ShapeUtil.GraphicsPathToGeometryPath(graphicsPath)
                textPath.FillMode = PathFillModeType.Normal

                # Set combination of new geometry path and origin geometry path to the shape
                shape.SetGeometryPaths(new[] { originalPath, textPath })

                # Save the presentation
                pres.save(resultPath, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
