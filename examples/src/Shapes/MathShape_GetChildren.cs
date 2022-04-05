using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
import aspose.slides as slides
using Aspose.slides.MathText

"""
This example demonstrates a using of GetChildren() method of the IMathElement interface.
"""
namespace CSharp.shapes
{
    class MathShape_GetChildren
    {
        public static void Run()
        {
            #Path for output presentation
            outPptxFile = Path.Combine(RunExamples.OutPath, "MathShape_GetChildren_out.pptx")

            using (presentation = new Presentation())
            {
                # Get first slide
                slide = presentation.slides[0]

                # Create MathShape in the first slide
                mathShape = slide.shapes.add_math_shape(10, 10, 500, 500)
                # Create MathParagraph
                IMathParagraph mathParagraph = (mathShape.text_frame.paragraphs[0].portions[0] as MathPortion).math_paragraph

                # Create MathBlock
                IMathBlock mathBlock = new MathBlock(new MathematicalText("F").join("+").join(new MathematicalText("1").Divide("y")).Underbar())

                # Add MathBlock to the MathParagraph
                mathParagraph.add(mathBlock)
                
                # Print all elements of the mathBlock
                ForEachMathElement(mathBlock)

                presentation.save(outPptxFile, slides.export.SaveFormat.PPTX)
            }
        }

        private static void ForEachMathElement(IMathElement root)
        {
            foreach (IMathElement child in root.GetChildren())
            {
                print(child.GetType() + (child is MathematicalText ? " : " +((MathematicalText)child).value : ""))

                #recursive
                ForEachMathElement(child)
            }
        }
    }
}
