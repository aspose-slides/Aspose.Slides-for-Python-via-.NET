import aspose.pydrawing as drawing
import aspose.slides as slides
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.text
{
    class RotatingText
    {
        public static void Run()
        {
            #ExStart:RotatingText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            # Get the first slide 
            slide = presentation.slides[0]

            # Add an AutoShape of Rectangle type
            ashp = slide.shapes.add_auto_shape(ShapeType.Rectangle, 150, 75, 350, 350)

            # Add TextFrame to the Rectangle
            ashp.AddTextFrame(" ")
            ashp.FillFormat.fill_type = FillType.NoFill

            # Accessing the text frame
            ITextFrame txtFrame = ashp.text_frame
            txtFrame.TextFrameFormat.TextVerticalType = TextVerticalType.Vertical270

            # Create the Paragraph object for text frame
            IParagraph para = txtFrame.paragraphs[0]

            # Create Portion object for paragraph
            portion = para.portions[0]
            portion.text = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog."
            portion.portion_format.fill_format.fill_type = slides.FillType.SOLID
            portion.portion_format.fill_format.solid_fill_color.color = Color.Black

            # Save Presentation
            presentation.save(dataDir + "RotateText_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:RotatingText
        }
    }
}