using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Util
using Aspose.slides.Export
using Aspose.slides.MathText

/*
This example demonstrates of using SlideUtil.AlignShapes method.
*/
namespace CSharp.shapes
{
    class ShapesAlignment
    {
        public static void Run()
        {
            #Path for output presentation
            outpptxFile = Path.Combine(RunExamples.OutPath, "ShapesAlignment_out.pptx")

            with slides.Presentation() as pres:
            {
                slide = pres.slides[0]
                # Create some shapes
                slide.shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 100, 100)
                slide.shapes.add_auto_shape(ShapeType.Rectangle, 200, 200, 100, 100)
                slide.shapes.add_auto_shape(ShapeType.Rectangle, 300, 300, 100, 100)
                # Aligning all shapes within IBaseSlide.
                SlideUtil.AlignShapes(ShapesAlignmentType.AlignBottom, True, pres.slides[0])

                slide = pres.slides.AddEmptySlide(slide.LayoutSlide)
                # Add group shape
                IGroupShape groupShape = slide.shapes.AddGroupShape()
                # Create some shapes to the group shape
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 350, 50, 50, 50)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 450, 150, 50, 50)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 550, 250, 50, 50)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 650, 350, 50, 50)
                # Aligning all shapes within IGroupShape.
                SlideUtil.AlignShapes(ShapesAlignmentType.AlignLeft, False, groupShape)

                slide = pres.slides.AddEmptySlide(slide.LayoutSlide)
                # Add group shape
                groupShape = slide.shapes.AddGroupShape()
                # Create some shapes to the group shape
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 350, 50, 50, 50)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 450, 150, 50, 50)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 550, 250, 50, 50)
                groupShape.shapes.add_auto_shape(ShapeType.Rectangle, 650, 350, 50, 50)
                # Aligning shapes with specified indexes within IGroupShape.
                SlideUtil.AlignShapes(ShapesAlignmentType.AlignLeft, False, groupShape, new int[] { 0, 2 })

                # Save presentation
                pres.save(outpptxFile, slides.export.SaveFormat.PPTX)
            }
        }
    }
}
