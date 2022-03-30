import aspose.slides as slides
using Aspose.slides.Animation
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class AnimationEffectinParagraph
    {
        public static void Run()
        {
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            #ExStart:AnimationEffectinParagraph
            using (Presentation presentation = new Presentation(dataDir + "Presentation1.pptx"))
            {
                # select paragraph to add effect
                autoShape = (IAutoShape)presentation.slides[0].shapes[0]
                paragraph = autoShape.text_frame.paragraphs[0]

                # add Fly animation effect to selected paragraph
                IEffect effect = presentation.slides[0].timeline.main_sequence.add_effect(paragraph, slides.animation.EffectType.Fly, slides.animation.EffectSubtype.Left, slides.animation.EffectTriggerType.OnClick)


                presentation.save(dataDir + "AnimationEffectinParagraph.pptx", slides.export.SaveFormat.PPTX)
            }



            #ExEnd:AnimationEffectinParagraph
        }
    }
}
