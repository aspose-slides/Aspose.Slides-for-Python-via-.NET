using System.IO

import aspose.slides as slides
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class ParagraphsAlignment
    {
        public static void Run()
        {
            #ExStart:ParagraphsAlignment
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Instantiate a Presentation object that represents a PPTX file
            using (Presentation pres = new Presentation(dataDir + "ParagraphsAlignment.pptx"))
            {

                # Accessing first slide
                slide = pres.slides[0]

                # Accessing the first and second placeholder in the slide and typecasting it as AutoShape
                ITextFrame tf1 = ((IAutoShape)slide.shapes[0]).text_frame
                ITextFrame tf2 = ((IAutoShape)slide.shapes[1]).text_frame

                # Change the text in both placeholders
                tf1.text = "Center Align by Aspose"
                tf2.text = "Center Align by Aspose"

                # Getting the first paragraph of the placeholders
                IParagraph para1 = tf1.paragraphs[0]
                IParagraph para2 = tf2.paragraphs[0]

                # Aligning the text paragraph to center
                para1.ParagraphFormat.Alignment = TextAlignment.Center
                para2.ParagraphFormat.Alignment = TextAlignment.Center

                #Writing the presentation as a PPTX file
                pres.save(dataDir + "Centeralign_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ParagraphsAlignment
        }
    }
}