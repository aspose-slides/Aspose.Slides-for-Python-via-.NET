using System.Collections.Generic
using System.IO
using System.text
using Aspose.slides.Export
using Aspose.slides.Export.Xaml

/*
This example demonstrates the saving presentation in HTML5 operation.
*/

namespace Aspose.slides.Examples.CSharp.Presentations.Conversion
{
    public class ConvertToHtml5
    {
        public static void Run()
        {
            # The path to the documents directory
            dataDir = RunExamples.GetDataDir_Conversion()

            # The path to output file
            outFilePath = Path.Combine(RunExamples.OutPath, "Demo.html")

            using (Presentation pres = new Presentation(dataDir + "Demo.pptx"))
            {
                # Export a presentation containing slides transitions, animations, and shapes animations to HTML5
                Html5Options options = new Html5Options()
                {
                    AnimateShapes = True,
                    AnimateTransitions = True
                }

                # Save presentation
                pres.save(outFilePath, SaveFormat.Html5, options)
            }
        }
    }
}