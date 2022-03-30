import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.shapes
{
    class GetShapeBevelEffectiveData
    {
        public static void Run()
        {

            #ExStart:GetShapeBevelEffectiveData

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            using (Presentation pres = new Presentation(dataDir + "Presentation1.pptx"))
            {
                IThreeDFormatEffectiveData threeDEffectiveData = pres.slides[0].shapes[0].ThreeDFormat.GetEffective()

                print("= Effective shape's top face relief properties =")
                print("Type: " + threeDEffectiveData.BevelTop.BevelType)
                print("Width: " + threeDEffectiveData.BevelTop.width)
                print("Height: " + threeDEffectiveData.BevelTop.height)


            }

            #ExEnd:GetShapeBevelEffectiveData
        }
    }
}
