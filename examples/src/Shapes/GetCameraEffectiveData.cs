import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.shapes
{
    class GetCameraEffectiveData
    {
        public static void Run() {

            #ExStart:GetCameraEffectiveData

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            using (Presentation pres = new Presentation(dataDir + "Presentation1.pptx"))
            {
                IThreeDFormatEffectiveData threeDEffectiveData = pres.slides[0].shapes[0].ThreeDFormat.GetEffective()

                print("= Effective camera properties =")
                print("Type: " + threeDEffectiveData.Camera.CameraType)
                print("Field of view: " + threeDEffectiveData.Camera.FieldOfViewAngle)
                print("Zoom: " + threeDEffectiveData.Camera.Zoom)

                
            }

            #ExEnd:GetCameraEffectiveData
        }
    }
}
