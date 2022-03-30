import aspose.pydrawing as drawing
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class SetTextFontProperties
    {
        public static void Run()
        {
            #ExStart:SetTextFontProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Instantiate Presentation
            with slides.Presentation() as presentation:
            {
               
                # Get first slide
                sld = presentation.slides[0]

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

                # Write the PPTX to disk 
                presentation.save(dataDir + "SetTextFontProperties_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetTextFontProperties
        }
    }
}
