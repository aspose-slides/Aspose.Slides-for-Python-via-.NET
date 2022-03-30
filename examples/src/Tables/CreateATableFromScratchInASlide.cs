import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Tables
{
    class CreateATableFromScratchInASlide
    {
        public static void Run() {

            #ExStart:CreateATableFromScratchInASlide

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Instantiate Presentation class that represents PPTX file
            with slides.Presentation() as pres:

            # Access first slide
            sld = pres.slides[0]

            # Define columns with widths and rows with heights
            double[] dblCols = { 50, 50, 50 }
            double[] dblRows = { 50, 30, 30, 30, 30 }

            # Add table shape to slide
            ITable tbl = sld.shapes.AddTable(100, 50, dblCols, dblRows)

            # Set border format for each cell
            for (row = 0 row < tbl.Rows.Count row++)
            {
                for (cell = 0 cell < tbl.Rows[row].Count cell++)
                {
                    tbl.Rows[row][cell].CellFormat.BorderTop.fill_format.fill_type = slides.FillType.SOLID
                    tbl.Rows[row][cell].CellFormat.BorderTop.fill_format.solid_fill_color.color = drawing.Color.red
                    tbl.Rows[row][cell].CellFormat.BorderTop.width = 5

                    tbl.Rows[row][cell].CellFormat.BorderBottom.FillFormat.fill_type = (slides.FillType.SOLID)
                    tbl.Rows[row][cell].CellFormat.BorderBottom.fill_format.solid_fill_color.color= drawing.Color.red
                    tbl.Rows[row][cell].CellFormat.BorderBottom.width =5

                    tbl.Rows[row][cell].CellFormat.BorderLeft.fill_format.fill_type = slides.FillType.SOLID
                    tbl.Rows[row][cell].CellFormat.BorderLeft.fill_format.solid_fill_color.color =drawing.Color.red
                    tbl.Rows[row][cell].CellFormat.BorderLeft.width = 5

                    tbl.Rows[row][cell].CellFormat.BorderRight.fill_format.fill_type = slides.FillType.SOLID
                    tbl.Rows[row][cell].CellFormat.BorderRight.fill_format.solid_fill_color.color = drawing.Color.red
                    tbl.Rows[row][cell].CellFormat.BorderRight.width = 5
                }
            }
            # Merge cells 1 & 2 of row 1
            tbl.MergeCells(tbl.Rows[0][0], tbl.Rows[1][1], False)

            # Add text to the merged cell
            tbl.Rows[0][0].text_frame.text = "Merged Cells"

            # Save PPTX to Disk
            pres.save(dataDir + "table.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:CreateATableFromScratchInASlide


        }
    }
}
