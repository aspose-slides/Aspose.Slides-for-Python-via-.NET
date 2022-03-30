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
    class Apply3DRotationEffecrOnShapes
    {
        public static void Run()
        {
            #ExStart:Apply3DRotationEffecrOnShapes
            # The path to the documents directory.                    
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create an instance of Presentation class
            with slides.Presentation() as pres:
            IShape autoShape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 30, 30, 200, 200)

            autoShape.ThreeDFormat.Depth = 6
            autoShape.ThreeDFormat.Camera.SetRotation(40, 35, 20)
            autoShape.ThreeDFormat.Camera.CameraType = CameraPresetType.IsometricLeftUp
            autoShape.ThreeDFormat.LightRig.LightType = LightRigPresetType.Balanced

            autoShape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.LINE, 30, 300, 200, 200)
            autoShape.ThreeDFormat.Depth = 6
            autoShape.ThreeDFormat.Camera.SetRotation(0, 35, 20)
            autoShape.ThreeDFormat.Camera.CameraType = CameraPresetType.IsometricLeftUp
            autoShape.ThreeDFormat.LightRig.LightType = LightRigPresetType.Balanced

          
            pres.save(dataDir + "Rotation_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:Apply3DRotationEffecrOnShapes
        }
    }
}
