import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class GetTextStyleEffectiveData
    {
        public static void Run() {

            #ExStart:
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()


            using (Presentation pres = new Presentation(dataDir + "Presentation1.pptx"))
            {
                shape = pres.slides[0].shapes[0] as IAutoShape

                ITextStyleEffectiveData effectiveTextStyle = shape.text_frame.TextFrameFormat.TextStyle.GetEffective()

                for (i = 0 i <= 8 i++)
                {
                    IParagraphFormatEffectiveData effectiveStyleLevel = effectiveTextStyle.GetLevel(i)
                    print("= Effective paragraph formatting for style level #" + i + " =")

                    print("Depth: " + effectiveStyleLevel.Depth)
                    print("Indent: " + effectiveStyleLevel.Indent)
                    print("Alignment: " + effectiveStyleLevel.Alignment)
                    print("Font alignment: " + effectiveStyleLevel.FontAlignment)
                }

            }

            #ExEnd:
        }

    }
}
