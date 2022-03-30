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
    class LineSpacing
    {
        public static void Run()
        {
            #ExStart:LineSpacing

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create an instance of Presentation class
            Presentation presentation = new Presentation(dataDir + "Fonts.pptx")

            # Obtain a slide's reference by its index
            sld = presentation.slides[0]

            # Access the TextFrame
            ITextFrame tf1 = ((IAutoShape)sld.shapes[0]).text_frame

            # Access the Paragraph
            para1 = tf1.paragraphs[0]

            # Set properties of Paragraph
            para1.ParagraphFormat.SpaceWithin = 80
            para1.ParagraphFormat.SpaceBefore = 40
            para1.ParagraphFormat.SpaceAfter = 40
            # Save Presentation
            presentation.save(dataDir + "LineSpacing_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:LineSpacing
        }
    }
}