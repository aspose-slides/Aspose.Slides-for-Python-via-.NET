using System.IO

import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class FontProperties
    {
        public static void Run()
        {
            #ExStart:FontProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Instantiate a Presentation object that represents a PPTX file# Instantiate a Presentation object that represents a PPTX file
            using (Presentation pres = new Presentation(dataDir + "FontProperties.pptx"))
            {

                # Accessing a slide using its slide position
                slide = pres.slides[0]

                # Accessing the first and second placeholder in the slide and typecasting it as AutoShape
                ITextFrame tf1 = ((IAutoShape)slide.shapes[0]).text_frame
                ITextFrame tf2 = ((IAutoShape)slide.shapes[1]).text_frame

                # Accessing the first Paragraph
                IParagraph para1 = tf1.paragraphs[0]
                IParagraph para2 = tf2.paragraphs[0]

                # Accessing the first portion
                port1 = para1.portions[0]
                port2 = para2.portions[0]

                # Define new fonts
                FontData fd1 = slides.FontData("Elephant")
                FontData fd2 = slides.FontData("Castellar")

                # Assign new fonts to portion
                port1.portion_format.latin_font = fd1
                port2.portion_format.latin_font = fd2

                # Set font to Bold
                port1.portion_format.font_bold = 1
                port2.portion_format.font_bold = 1

                # Set font to Italic
                port1.portion_format.font_italic = 1
                port2.portion_format.font_italic = 1

                # Set font color
                port1.portion_format.fill_format.fill_type = slides.FillType.SOLID
                port1.portion_format.fill_format.solid_fill_color.color = Color.Purple
                port2.portion_format.fill_format.fill_type = slides.FillType.SOLID
                port2.portion_format.fill_format.solid_fill_color.color = Color.Peru

                #Write the PPTX to disk
                pres.save(dataDir + "WelcomeFont_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FontProperties
        }
    }
}