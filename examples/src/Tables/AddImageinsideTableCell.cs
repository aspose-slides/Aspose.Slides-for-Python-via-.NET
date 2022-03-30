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
    public class AddImageinsideTableCell
    {
        public static void Run()
        {
            #ExStart:AddImageinsideTableCell
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Instantiate Presentation class object
            with slides.Presentation() as presentation:

            # Access first slide
            islide = presentation.slides[0]

            # Define columns with widths and rows with heights
            double[] dblCols = { 150, 150, 150, 150 }
            double[] dblRows = { 100, 100, 100, 100, 90 }

            # Add table shape to slide
            ITable tbl = islide.shapes.AddTable(50, 50, dblCols, dblRows)

            # Creating a Image object to hold the image file
            image = drawing.Bitmap(dataDir + "aspose-logo.jpg")

            # Create an object using the bitmap object
            imgx1 = presentation.images.add_image(image)

            # Add image to first table cell
            tbl[0, 0].CellFormat.fill_format.fill_type = slides.FillType.PICTURE
            tbl[0, 0].CellFormat.FillFormat.picture_fill_format.PictureFillMode = PictureFillMode.Stretch
            tbl[0, 0].CellFormat.FillFormat.picture_fill_format.picture.image = imgx1

            # Save PPTX to Disk
            presentation.save(dataDir + "Image_In_TableCell_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:AddImageinsideTableCell
        }
    }
}