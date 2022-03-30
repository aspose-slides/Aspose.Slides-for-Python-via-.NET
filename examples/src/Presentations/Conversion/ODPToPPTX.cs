import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.Presentations.Conversion
{
    class ODPToPPTX
    {

        public static void Run() {

            #ExStart:ODPToPPTX

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Conversion()

            
            srcFileName = dataDir + "AccessOpenDoc.odp"
            destFileName = dataDir + "AccessOpenDoc.pptx"
            #Instantiate a Presentation object that represents a presentation file
            using (Presentation pres = new Presentation(srcFileName))
            {
                #Saving the PPTX presentation to PPTX format
                pres.save(destFileName, slides.export.SaveFormat.PPTX)
            }
            #ExEnd:ODPToPPTX



        }
    }
}
