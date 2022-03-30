import aspose.slides as slides
using Aspose.slides.Effects
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class SetTransparencyOfTextInShadow
    {
        public static void Run() {
            #ExStart:SetTransparencyOfTextInShadow
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            using (Presentation pres = new Presentation(dataDir+ "transparency.pptx"))
            {
                shape = (IAutoShape)pres.slides[0].shapes[0]
                IEffectFormat effects = shape.text_frame.paragraphs[0].portions[0].portion_format.EffectFormat

                IOuterShadow outerShadowEffect = effects.OuterShadowEffect

                Color shadowColor = outerShadowEffect.ShadowColor.Color
                print("{0} - transparency is: {1}", shadowColor, ((float)shadowColor.A / byte.max_value) * 100)

                # set transparency to zero percent
                outerShadowEffect.ShadowColor.color = drawing.Color.from_argb(255, shadowColor)

                pres.save(dataDir+"transparency-2.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetTransparencyOfTextInShadow
        }
    }
}
