import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.shapes
{
    class GetLightRigEffectiveData
    {
        public static void Run()
        {

            #ExStart:GetLightRigEffectiveData

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            using (Presentation pres = new Presentation(dataDir + "Presentation1.pptx"))
            {
                IThreeDFormatEffectiveData threeDEffectiveData = pres.slides[0].shapes[0].three_dformat.get_effective()

                print("= Effective light rig properties =")
                print("Type: " + threeDEffectiveData.light_rig.light_type)
                print("Direction: " + threeDEffectiveData.light_rig.direction)


            }

            #ExEnd:GetLightRigEffectiveData
        }
    }
}
