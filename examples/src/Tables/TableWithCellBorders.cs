using System.IO
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.Tables
{
    public class TableWithCellBorders
    {
        public static void Run()
        {
            #ExStart:TableWithCellBorders
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Presentation class that represents PPTX file
            with slides.Presentation() as pres:
            {

                # Access first slide
                Slide sld = (Slide)pres.slides[0]

                # Define columns with widths and rows with heights
                double[] dblCols = { 50, 50, 50, 50 }
                double[] dblRows = { 50, 30, 30, 30, 30 }

                # Add table shape to slide

                # Add table shape to slide
                ITable tbl = sld.shapes.AddTable(100, 50, dblCols, dblRows)

                # Set border format for each cell
                foreach (IRow row in tbl.Rows)
                    foreach (ICell cell in row)
                    {
                        cell.CellFormat.BorderTop.FillFormat.fill_type = FillType.NoFill
                        cell.CellFormat.BorderBottom.FillFormat.fill_type = FillType.NoFill
                        cell.CellFormat.BorderLeft.FillFormat.fill_type = FillType.NoFill
                        cell.CellFormat.BorderRight.FillFormat.fill_type = FillType.NoFill
                    }

                #Write PPTX to Disk
                pres.save(dataDir + "table_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:TableWithCellBorders
        }
    }
}