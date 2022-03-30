import aspose.slides as slides
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Tables
{
    class CreateTable
    {
        public static void Run() {

            #ExStart:CreateTable

            with slides.Presentation() as pres:

            #Access first slide
            sld = pres.slides[0]

            #Define columns with widths and rows with heights
            double[] dblCols = { 50, 50, 50 }
            double[] dblRows = { 50, 30, 30, 30, 30 }

            #Add a table
            Aspose.slides.ITable tbl = sld.shapes.AddTable(50, 50, dblCols, dblRows)

            #Set border format for each cell
            foreach (IRow row in tbl.Rows)
            {
                foreach (ICell cell in row)
                {

                    #Get text frame of each cell
                    ITextFrame tf = cell.text_frame
                    #Add some text
                    tf.text = "T" + cell.FirstRowIndex.ToString() + cell.FirstColumnIndex.ToString()
                    #Set font size of 10
                    tf.paragraphs[0].portions[0].portion_format.font_height = 10
                    tf.paragraphs[0].ParagraphFormat.Bullet.type = BulletType.NONE
                }
            }

            #Write the presentation to the disk
            pres.save("C:\\data\\tblSLD.ppt", SaveFormat.Ppt)
            #ExEnd:CreateTable

        }
    }
}
