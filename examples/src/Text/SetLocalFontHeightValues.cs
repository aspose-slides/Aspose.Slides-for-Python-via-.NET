import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.text
{
    class SetLocalFontHeightValues
    {
        public static void Run() {


            #ExStart:SetLocalFontHeightValues
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            with slides.Presentation() as pres:
            {
                newShape = pres.slides[0].shapes.add_auto_shape(ShapeType.Rectangle, 100, 100, 400, 75, False)
                newShape.AddTextFrame("")
                newShape.text_frame.paragraphs[0].portions.clear()

                portion0 = new Portion("Sample text with first portion")
                portion1 = new Portion(" and second portion.")

                newShape.text_frame.paragraphs[0].portions.add(portion0)
                newShape.text_frame.paragraphs[0].portions.add(portion1)

                print("Effective font height just after creation:")
                print("Portion #0: " + portion0.portion_format.GetEffective().font_height)
                print("Portion #1: " + portion1.portion_format.GetEffective().font_height)

                pres.DefaultTextStyle.GetLevel(0).DefaultPortionFormat.font_height = 24

                print("Effective font height after setting entire presentation default font height:")
                print("Portion #0: " + portion0.portion_format.GetEffective().font_height)
                print("Portion #1: " + portion1.portion_format.GetEffective().font_height)

                newShape.text_frame.paragraphs[0].ParagraphFormat.DefaultPortionFormat.font_height = 40

                print("Effective font height after setting paragraph default font height:")
                print("Portion #0: " + portion0.portion_format.GetEffective().font_height)
                print("Portion #1: " + portion1.portion_format.GetEffective().font_height)

                newShape.text_frame.paragraphs[0].portions[0].portion_format.font_height = 55

                print("Effective font height after setting portion #0 font height:")
                print("Portion #0: " + portion0.portion_format.GetEffective().font_height)
                print("Portion #1: " + portion1.portion_format.GetEffective().font_height)

                newShape.text_frame.paragraphs[0].portions[1].portion_format.font_height = 18

                print("Effective font height after setting portion #1 font height:")
                print("Portion #0: " + portion0.portion_format.GetEffective().font_height)
                print("Portion #1: " + portion1.portion_format.GetEffective().font_height)

                pres.save(dataDir + "SetLocalFontHeightValues.pptx",slides.export.SaveFormat.PPTX)
            }

            #ExEnd:SetLocalFontHeightValues

        }
    }
}
