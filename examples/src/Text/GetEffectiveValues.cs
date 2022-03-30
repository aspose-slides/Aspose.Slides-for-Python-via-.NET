import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class GetEffectiveValues
    {
        public static void Run() {

            #ExStart:GetEffectiveValues
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            using (Presentation pres = new Presentation(dataDir + "Presentation1.pptx"))
            {
                shape = pres.slides[0].shapes[0] as IAutoShape

                ITextFrameFormat localTextFrameFormat = shape.text_frame.TextFrameFormat
                ITextFrameFormatEffectiveData effectiveTextFrameFormat = localTextFrameFormat.GetEffective()

                IPortionFormat localPortionFormat = shape.text_frame.paragraphs[0].portions[0].portion_format
                IPortionFormatEffectiveData effectivePortionFormat = localPortionFormat.GetEffective()
            }

            #ExEnd:GetEffectiveValues


        }
    }
}
