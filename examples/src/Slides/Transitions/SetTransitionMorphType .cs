import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.SlideShow
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Transitions
{
    class SetTransitionMorphType
    {
        public static void Run() {

            #ExStart:SetTransitionMorphType
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Transitions()

            using (Presentation presentation = new Presentation(dataDir + "presentation.pptx"))
            {
                presentation.slides[0].SlideShowTransition.type = TransitionType.Morph
                ((IMorphTransition)presentation.slides[0].SlideShowTransition.value).MorphType = TransitionMorphType.ByWord
                presentation.save(dataDir + "presentation-out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetTransitionMorphType
        }
    }
}
