using System.IO
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.Tables
{
    public class RemovingRowColumn
    {
        public static void Run()
        {
            #ExStart:RemovingRowColumn
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            with slides.Presentation() as pres:

            slide = pres.slides[0]
            double[] colWidth = { 100, 50, 30 }
            double[] rowHeight = { 30, 50, 30 }

            ITable table = slide.shapes.AddTable(100, 100, colWidth, rowHeight)
            table.Rows.remove_at(1, False)
            table.Columns.remove_at(1, False)
            pres.save(dataDir + "TestTable_out.pptx", slides.export.SaveFormat.PPTX)
            #ExEnd:RemovingRowColumn
        }
    }
}