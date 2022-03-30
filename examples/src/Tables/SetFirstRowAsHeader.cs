import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Tables
{
    class SetFirstRowAsHeader
    {

        public static void Run() {

            #ExStart:SetFirstRowAsHeader

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Tables()

            # Instantiate Presentation class that represents PPTX
            Presentation pres = new Presentation(dataDir + "table.pptx")

            # Access the first slide
            sld = pres.slides[0]

            # Initialize None TableEx
            ITable tbl = None

            # Iterate through the shapes and set a reference to the table found
            foreach (IShape shp in sld.shapes)
            {
                if (shp is ITable) {
                tbl = (ITable)shp
            }
        }

       
           #Set the first row of a table as header with a special formatting.
           tbl.FirstRow = True
            

           
            #ExEnd:SetFirstRowAsHeader

        }
    }
}
