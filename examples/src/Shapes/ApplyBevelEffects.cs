import aspose.pydrawing as drawing
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class ApplyBevelEffects
    {
        public static void Run()
        {
            #ExStart:ApplyBevelEffects
            # The path to the documents directory.                    
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create an instance of Presentation class
            with slides.Presentation() as pres:
            slide = pres.slides[0]

            # Add a shape on slide
            shape = slide.shapes.add_auto_shape(slides.ShapeType.ELLIPSE, 30, 30, 100, 100)
            shape.fill_format.fill_type = slides.FillType.SOLID
            shape.fill_format.solid_fill_color.color = drawing.Color.green
            ILineFillFormat format = shape.line_format.FillFormat
            format.fill_type = slides.FillType.SOLID
            format.solid_fill_color.color = drawing.Color.orange
            shape.line_format.width = 2.0

            # Set ThreeDFormat properties of shape
            shape.ThreeDFormat.Depth = 4
            shape.ThreeDFormat.BevelTop.BevelType = BevelPresetType.Circle
            shape.ThreeDFormat.BevelTop.height = 6
            shape.ThreeDFormat.BevelTop.width = 6
            shape.ThreeDFormat.Camera.CameraType = CameraPresetType.OrthographicFront
            shape.ThreeDFormat.LightRig.LightType = LightRigPresetType.ThreePt
            shape.ThreeDFormat.LightRig.Direction = LightingDirection.Top

            # Write the presentation as a PPTX file
            pres.save(dataDir + "Bavel_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:ApplyBevelEffects
        }
    }
}
