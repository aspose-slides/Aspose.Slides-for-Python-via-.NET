using System
using System.Collections.Generic
using System.Drawing.Imaging
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Util
import aspose.slides as slides
using Aspose.slides.MathText

"""
The example below demonstrates how to set sketchy type for a shape.
Please pay attention that not all versions of PowerPoint can display sketched shapes.
"""
namespace CSharp.shapes
{
    class SketchedShapes
    {
        public static void Run()
        {
            #Path for output presentation
            outPptxFile = Path.Combine(RunExamples.OutPath, "SketchedShapes_out.pptx")
            outPngFile = Path.Combine(RunExamples.OutPath, "SketchedShapes_out.png")

            with slides.Presentation() as pres:
            {
                shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 20, 20, 300, 150)
                shape.fill_format.fill_type = slides.FillType.NO_FILL

                # Transform shape to sketch of a freehand style
                shape.line_format.SketchFormat.SketchType = LineSketchType.Scribble

                pres.slides[0].get_thumbnail(4/3f, 4/3f).save(outPngFile, drawing.imaging.ImageFormat.png)
                pres.save(outPptxFile, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
