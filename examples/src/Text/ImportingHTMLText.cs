using System.IO

import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.text
{
    public class ImportingHTMLText
    {
        public static void Run()
        {
            #ExStart:ImportingHTMLText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create Empty presentation instance# Create Empty presentation instance
            with slides.Presentation() as pres:
            {
                # Acesss the default first slide of presentation
                slide = pres.slides[0]

                # Adding the AutoShape to accomodate the HTML content
                ashape = slide.shapes.add_auto_shape(ShapeType.Rectangle, 10, 10, pres.SlideSize.size.width - 20, pres.SlideSize.size.height - 10)

                ashape.FillFormat.fill_type = FillType.NoFill

                # Adding text frame to the shape
                ashape.AddTextFrame("")

                # Clearing all paragraphs in added text frame
                ashape.text_frame.Paragraphs.clear()

                # Loading the HTML file using stream reader
                TextReader tr = new StreamReader(dataDir + "file.html")

                # Adding text from HTML stream reader in text frame
                ashape.text_frame.Paragraphs.AddFromHtml(tr.ReadToEnd())

                # Saving Presentation
                pres.save(dataDir + "output_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ImportingHTMLText
        }
    }
}