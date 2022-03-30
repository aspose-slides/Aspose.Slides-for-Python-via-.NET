import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class GetTextFrameFormatEffectiveData
    {
        public static void Run() {

            #ExStart:GetTextFrameFormatEffectiveData

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            using (Presentation pres = new Presentation(dataDir + "Presentation1.pptx"))
            {
                shape = pres.slides[0].shapes[0] as IAutoShape

                ITextFrameFormat textFrameFormat = shape.text_frame.TextFrameFormat
                ITextFrameFormatEffectiveData effectiveTextFrameFormat = textFrameFormat.GetEffective()


                print("Anchoring type: " + effectiveTextFrameFormat.AnchoringType)
                print("Autofit type: " + effectiveTextFrameFormat.autofit_type)
                print("Text vertical type: " + effectiveTextFrameFormat.TextVerticalType)
                print("Margins")
                print("   Left: " + effectiveTextFrameFormat.MarginLeft)
                print("   Top: " + effectiveTextFrameFormat.MarginTop)
                print("   Right: " + effectiveTextFrameFormat.MarginRight)
                print("   Bottom: " + effectiveTextFrameFormat.MarginBottom)

            }
            #ExEnd:GetTextFrameFormatEffectiveData

        }
    }
}
