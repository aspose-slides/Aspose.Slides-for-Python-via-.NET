using System.IO
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.Tables
{
    public class UpdateExistingTable
    {
        public static void Run()
        {
            #ExStart:UpdateExistingTable
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Instantiate Presentation class that represents PPTX# Instantiate Presentation class that represents PPTX
            using (Presentation pres = new Presentation(dataDir + "UpdateExistingTable.pptx"))
            {

                # Access the first slide
                sld = pres.slides[0]

                # Initialize None TableEx
                ITable tbl = None

                # Iterate through the shapes and set a reference to the table found
                foreach (IShape shp in sld.shapes)
                    if (shp is ITable)
                        tbl = (ITable)shp

                # Set the text of the first column of second row
                tbl[0, 1].text_frame.text = "New"

                #Write the PPTX to Disk
                pres.save(dataDir + "table1_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:UpdateExistingTable
        }
    }
}