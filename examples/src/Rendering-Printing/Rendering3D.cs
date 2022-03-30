using Aspose.slides.Export
import aspose.slides as slides
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.IO

namespace Aspose.slides.Examples.CSharp.Rendering.Printing
{
    class Rendering3D
    {

        # This example demonstrates creating and rendering presentation with 3D graphics.

        public static void Run()
        {
            outPptxFile = Path.Combine(RunExamples.OutPath, "sandbox_3d.pptx")
            outPngFile = Path.Combine(RunExamples.OutPath, "sample_3d.png")

            with slides.Presentation() as pres:
            {
                shape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 200, 150, 200, 200)
                shape.text_frame.text = "3D"
                shape.text_frame.paragraphs[0].ParagraphFormat.DefaultPortionFormat.font_height = 64

                shape.ThreeDFormat.Camera.CameraType = CameraPresetType.OrthographicFront
                shape.ThreeDFormat.Camera.SetRotation(20, 30, 40)
                shape.ThreeDFormat.LightRig.LightType = LightRigPresetType.Flat
                shape.ThreeDFormat.LightRig.Direction = LightingDirection.Top
                shape.ThreeDFormat.Material = MaterialPresetType.Powder
                shape.ThreeDFormat.ExtrusionHeight = 100
                shape.ThreeDFormat.ExtrusionColor.color = drawing.Color.blue

                pres.slides[0].get_thumbnail(2, 2).save(outPngFile, drawing.imaging.ImageFormat.png)
                pres.save(outPptxFile, slides.export.SaveFormat.PPTX)
            }
        }
    }
}


