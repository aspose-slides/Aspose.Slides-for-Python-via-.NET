using System.IO

import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.text
{
    public class SettingPresentationLanguageAndShapeText
    {
        public static void Run()
        {
            # ExStart:SettingPresentationLanguageAndShapeText
            with slides.Presentation() as pres:
            {
                shape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 50, 50, 200, 50)
                shape.AddTextFrame("Text to apply spellcheck language")
                shape.text_frame.paragraphs[0].portions[0].portion_format.LanguageId = "en-EN"

                pres.save(RunExamples.OutPath + "test1.pptx", slides.export.SaveFormat.PPTX)
            }
        }
        # ExEnd:SettingPresentationLanguageAndShapeText
    }
}
