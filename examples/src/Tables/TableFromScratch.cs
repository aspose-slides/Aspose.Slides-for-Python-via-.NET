using System.IO
import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.Tables
{
    public class TableFromScratch
    {
        public static void Run()
        {
            #ExStart:TableFromScratch
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Instantiate Presentation class that represents PPTX# Instantiate Presentation class that represents PPTX
            using (Presentation presentation = new Presentation(dataDir + "UpdateExistingTable.pptx"))
            {
                # Access the first slide
                sld = presentation.slides[0]

                # Initialize None TableEx
                ITable table = None

                # Iterate through the shapes and set a reference to the table found
                foreach (IShape shape in sld.shapes)
                    if (shape is ITable)
                        table = (ITable)shape

                # Set the text of the first column of second row
                table[0, 1].text_frame.text = "New"

                # Write the PPTX to Disk
                presentation.save(dataDir + "UpdateTable_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:TableFromScratch
        }
    }
}