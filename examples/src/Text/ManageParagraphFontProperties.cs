import aspose.pydrawing as drawing
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
    class ManageParagraphFontProperties
    {
        public static void Run()
        {
            #ExStart:ManageParagraphFontProperties
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Instantiate PresentationEx 
            using (Presentation presentation = new Presentation(dataDir + "DefaultFonts.pptx"))
            {
                # Accessing a slide using its slide position
                slide = presentation.slides[0]
                
                # Accessing the first and second placeholder in the slide and typecasting it as AutoShape
                ITextFrame tf1 = ((IAutoShape)slide.shapes[0]).text_frame
                ITextFrame tf2 = ((IAutoShape)slide.shapes[1]).text_frame
                
                # Accessing the first Paragraph
                IParagraph para1 = tf1.paragraphs[0]
                IParagraph para2 = tf2.paragraphs[0]

                # Justify the paragraph
                para2.ParagraphFormat.Alignment = TextAlignment.JustifyLow

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

                # Write the PPTX to disk 
                presentation.save(dataDir + "ManagParagraphFontProperties_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ManageParagraphFontProperties
        }
    }
}
