import aspose.slides as slides
using Aspose.slides.DOM.Ole
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.shapes
{
    class SetFileTypeForAnEmbeddingObject
    {
        public static void Run() {

            #ExStart:SetFileTypeForAnEmbeddingObject

            with slides.Presentation() as pres:
            {
                # The path to the documents directory.
                dataDir = RunExamples.GetDataDir_Shapes()

                # Add known Ole objects
                byte[] fileBytes = File.ReadAllBytes(dataDir + "test.zip")

                # Create Ole embedded file info
                IOleEmbeddedDataInfo dataInfo = new OleEmbeddedDataInfo(fileBytes, "zip")

                # Create OLE object
                IOleObjectFrame oleFrame = pres.slides[0].shapes.AddOleObjectFrame(150, 20, 50, 50, dataInfo)
                oleFrame.IsObjectIcon = True


                pres.save(dataDir + "SetFileTypeForAnEmbeddingObject.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:SetFileTypeForAnEmbeddingObject

        }
    }
}
