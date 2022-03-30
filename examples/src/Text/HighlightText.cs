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
    class HighlightText
    {
        public static void Run()
        {

            #ExStart:HighlightText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()
            Presentation presentation = new Presentation(dataDir +"SomePresentation.pptx")
            ((AutoShape)presentation.slides[0].shapes[0]).text_frame.HighlightText("title", Color.LightBlue) # highlighting all words 'important'
            ((AutoShape)presentation.slides[0].shapes[0]).text_frame.HighlightText("to", Color.Violet, new TextHighlightingOptions()
            {
                WholeWordsOnly = True
            }) # highlighting all separate 'the' occurrences
            presentation.save(dataDir+ "SomePresentation-out2.pptx", slides.export.SaveFormat.PPTX)

            #ExEnd:HighlightText
        }
    }
}
