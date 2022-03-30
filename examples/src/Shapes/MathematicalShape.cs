using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.MathText

/*
This example demonstrates of using API for creation a mathematical expression for Pythagorean theorem.
*/
namespace CSharp.shapes
{
    class MathematicalShape
    {
        public static void Run()
        {
            #Path for output presentation
            outpptxFile = Path.Combine(RunExamples.OutPath, "MathematicalShape_out.pptx")

            with slides.Presentation() as pres:
            {
                # Create a new AutoShape of the type Rectangle to host mathematical content inside and adds it to the end of the collection.
                mathShape = pres.slides[0].shapes.AddMathShape(10, 10, 100, 25)

                # Cteate mathematical paragraph that is a container for mathematical blocks.
                IMathParagraph mathParagraph = ((MathPortion)mathShape.text_frame.paragraphs[0].portions[0]).MathParagraph

                # Create mathematical expression as an instance of mathematical text that contained within a MathParagraph.
                IMathBlock mathBlock = new MathematicalText("c")
                    .SetSuperscript("2")
                    .Join("=")
                    .Join(new MathematicalText("a")
                        .SetSuperscript("2"))
                    .Join("+")
                    .Join(new MathematicalText("b")
                        .SetSuperscript("2"))

                # Add mathematical expression to the mathematical paragraph.
                mathParagraph.add(mathBlock)

                pres.save(outpptxFile, slides.export.SaveFormat.PPTX) 
            }
        }
    }
}
