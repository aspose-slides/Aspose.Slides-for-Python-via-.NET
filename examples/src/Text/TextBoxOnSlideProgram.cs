using System.IO

import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.text
{
    public class TextBoxOnSlideProgram
    {
        public static void Run()
        {
            #ExStart:TextBoxOnSlideProgram
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)
            
            # Instantiate PresentationEx# Instantiate PresentationEx
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add an AutoShape of Rectangle type
                ashp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 150, 75, 150, 50)

                # Add TextFrame to the Rectangle
                ashp.AddTextFrame(" ")

                # Accessing the text frame
                ITextFrame txtFrame = ashp.text_frame

                # Create the Paragraph object for text frame
                IParagraph para = txtFrame.paragraphs[0]

                # Create Portion object for paragraph
                portion = para.portions[0]

                # Set Text
                portion.text = "Aspose TextBox"

                # Save the presentation to disk
                pres.save(dataDir + "TextBox_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:TextBoxOnSlideProgram
        }
    }
}