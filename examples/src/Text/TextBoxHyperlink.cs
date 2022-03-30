using System.IO
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.text
{
    public class TextBoxHyperlink
    {
        public static void Run()
        {
            #ExStart:TextBoxHyperlink
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate a Presentation class that represents a PPTX
            Presentation pptxPresentation = new Presentation()

            # Get first slide
            slide = pptxPresentation.slides[0]

            # Add an AutoShape of Rectangle Type
            IShape pptxShape = slide.shapes.add_auto_shape(ShapeType.Rectangle, 150, 150, 150, 50)

            # Cast the shape to AutoShape
            pptxAutoShape = (IAutoShape)pptxShape

            # Access ITextFrame associated with the AutoShape
            pptxAutoShape.AddTextFrame("")

            ITextFrame ITextFrame = pptxAutoShape.text_frame

            # Add some text to the frame
            ITextFrame.paragraphs[0].portions[0].text = "Aspose.Slides"

            # Set Hyperlink for the portion text
            IHyperlinkManager HypMan = ITextFrame.paragraphs[0].portions[0].portion_format.HyperlinkManager
            HypMan.SetExternalHyperlinkClick("http:#www.aspose.com")
            # Save the PPTX Presentation
            pptxPresentation.save(dataDir + "hLinkPPTX_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:TextBoxHyperlink
        }
    }
}