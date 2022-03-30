import aspose.slides as slides
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
    class HighlightTextUsingRegx
    {
        public static void Run() {

            #ExStart:HighlightTextUsingRegx
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            Presentation presentation = new Presentation(dataDir + "SomePresentation.pptx")
            TextHighlightingOptions options = new TextHighlightingOptions()
            ((AutoShape)presentation.slides[0].shapes[0]).text_frame.HighlightRegex(@"\b[^\s]{5,}\b", drawing.Color.blue, options) # highlighting all words with 10 symbols or longer
            presentation.save(dataDir+ "SomePresentation-out.pptx", slides.export.SaveFormat.PPTX)

            #ExEnd:HighlightTextUsingRegx
        }
    }
}
