import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Conversion
{
    class ExportToHTMLWithResponsiveLayout
    {
        public static void Run() {

            #ExStart:ExportToHTMLWithResponsiveLayout
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            Presentation presentation = new Presentation(dataDir+"SomePresentation.pptx")
            HtmlOptions saveOptions = new HtmlOptions()
            saveOptions.SvgResponsiveLayout = True
            presentation.save(dataDir+"SomePresentation-out.html", SaveFormat.Html, saveOptions)
            #ExEnd:ExportToHTMLWithResponsiveLayout
        }
    }
}
