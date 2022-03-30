using System.IO
import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.text
{
    public class FontFamilyExample
    {
        public static void Run()
        {
            #ExStart:FontFamily
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Presentation Class
            with slides.Presentation() as pres:
            {

                # Get first slide
                sld = pres.slides[0]

                # Add an AutoShape of Rectangle type
                ashp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 50, 200, 50)

                # Remove any fill style associated with the AutoShape
                ashp.fill_format.fill_type = slides.FillType.NO_FILL

                # Access the TextFrame associated with the AutoShape
                ITextFrame tf = ashp.text_frame
                tf.text = "Aspose TextBox"

                # Access the Portion associated with the TextFrame
                port = tf.paragraphs[0].portions[0]

                # Set the Font for the Portion
                port.portion_format.latin_font = slides.FontData("Times New Roman")

                # Set Bold property of the Font
                port.portion_format.font_bold = 1

                # Set Italic property of the Font
                port.portion_format.font_italic = 1

                # Set Underline property of the Font
                port.portion_format.FontUnderline = TextUnderlineType.Single

                # Set the Height of the Font
                port.portion_format.font_height = 25

                # Set the color of the Font
                port.portion_format.fill_format.fill_type = slides.FillType.SOLID
                port.portion_format.fill_format.solid_fill_color.color = drawing.Color.blue

                #Write the presentation to disk
                pres.save(dataDir + "pptxFont_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:FontFamily
        }
    }
}