import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
using Aspose.slides.MathText

# This example demonstrates export a mathematical paragraph or block to MathML format. 

namespace CSharp.Presentations.Conversion
{
    class ExportMathParagraphToMathML
    {
        public static void Run()
        {
            outSvgFileName = Path.Combine(RunExamples.OutPath, "mathml.xml")

            with slides.Presentation() as pres:
            {
                autoShape = pres.slides[0].shapes.AddMathShape(0, 0, 500, 50)
                mathParagraph = ((MathPortion) autoShape.text_frame.paragraphs[0].portions[0]).MathParagraph

                mathParagraph.add(new MathematicalText("a").SetSuperscript("2").Join("+")
                    .Join(new MathematicalText("b").SetSuperscript("2")).Join("=")
                    .Join(new MathematicalText("c").SetSuperscript("2")))

                using (Stream stream = new FileStream(outSvgFileName, FileMode.Create))
                    mathParagraph.WriteAsMathMl(stream)
            }
        }
    }
}