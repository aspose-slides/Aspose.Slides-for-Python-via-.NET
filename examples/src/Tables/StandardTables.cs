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
    public class StandardTables
    {
        public static void Run()
        {
            #ExStart:StandardTables
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Instantiate Presentation class that represents PPTX file
            with slides.Presentation() as pres:
            {

                # Access first slide
                sld = pres.slides[0]

                # Define columns with widths and rows with heights
                double[] dblCols = { 70, 70, 70, 70 }
                double[] dblRows = { 70, 70, 70, 70 }

                # Add table shape to slide
                ITable tbl = sld.shapes.AddTable(100, 50, dblCols, dblRows)

                # Set border format for each cell
                foreach (IRow row in tbl.Rows)
                {
                    foreach (ICell cell in row)
                    {
                        cell.CellFormat.BorderTop.fill_format.fill_type = slides.FillType.SOLID
                        cell.CellFormat.BorderTop.fill_format.solid_fill_color.color = drawing.Color.red
                        cell.CellFormat.BorderTop.width = 5

                        cell.CellFormat.BorderBottom.fill_format.fill_type = slides.FillType.SOLID
                        cell.CellFormat.BorderBottom.fill_format.solid_fill_color.color = drawing.Color.red
                        cell.CellFormat.BorderBottom.width = 5

                        cell.CellFormat.BorderLeft.fill_format.fill_type = slides.FillType.SOLID
                        cell.CellFormat.BorderLeft.fill_format.solid_fill_color.color = drawing.Color.red
                        cell.CellFormat.BorderLeft.width = 5

                        cell.CellFormat.BorderRight.fill_format.fill_type = slides.FillType.SOLID
                        cell.CellFormat.BorderRight.fill_format.solid_fill_color.color = drawing.Color.red
                        cell.CellFormat.BorderRight.width = 5
                    }
                }

                #Write PPTX to Disk
                pres.save(dataDir + "StandardTables_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:StandardTables
        }
    }
}

