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

namespace Aspose.slides.Examples.CSharp.Tables
{
    public class VerticallyAlignText
    {
        public static void Run()
        {
            #ExStart:VerticallyAlignText
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Create an instance of Presentation class
            with slides.Presentation() as presentation:

            # Get the first slide 
            slide = presentation.slides[0]

            # Define columns with widths and rows with heights
            double[] dblCols = { 120, 120, 120, 120 }
            double[] dblRows = { 100, 100, 100, 100 }

            # Add table shape to slide
            ITable tbl = slide.shapes.AddTable(100, 50, dblCols, dblRows)
            tbl[1, 0].text_frame.text = "10"
            tbl[2, 0].text_frame.text = "20"
            tbl[3, 0].text_frame.text = "30"

            # Accessing the text frame
            ITextFrame txtFrame = tbl[0, 0].text_frame

            # Create the Paragraph object for text frame
            paragraph = txtFrame.paragraphs[0]

            # Create Portion object for paragraph
            portion = paragraph.portions[0]
            portion.text = "Text here"
            portion.portion_format.fill_format.fill_type = slides.FillType.SOLID
            portion.portion_format.fill_format.solid_fill_color.color = Color.Black

            # Aligning the text vertically
            ICell cell = tbl[0, 0]
            cell.TextAnchorType = TextAnchorType.Center
            cell.TextVerticalType = TextVerticalType.Vertical270

            # Save Presentation
            presentation.save(dataDir +  "Vertical_Align_Text_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:VerticallyAlignText
         }
    }
}

