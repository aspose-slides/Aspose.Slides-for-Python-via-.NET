import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.shapes
{
    class ExtractEmbeddedFileDataFromOLEObject
    {
        public static void Run() {

            #ExStart:ExtractEmbeddedFileDataFromOLEObject

            # The documents directory path.
            dataDir = RunExamples.GetDataDir_Shapes()

            pptxFileName = dataDir +"TestOlePresentation.pptx"
            using (Presentation pres = new Presentation(pptxFileName))
            {
                objectnum = 0
                foreach (sld in pres.Slides)
                {
                    foreach (IShape shape in sld.shapes)
                    {
                        if (shape is OleObjectFrame)
                        {
                            objectnum++
                            OleObjectFrame oleFrame = shape as OleObjectFrame
                            byte[] data = oleFrame.EmbeddedData.EmbeddedFileData
                            fileExtention = oleFrame.EmbeddedData.EmbeddedFileExtension

                            extractedPath = dataDir +"ExtractedObject_out" + objectnum + fileExtention
                            using (FileStream fs = new FileStream(extractedPath, FileMode.Create))
                            {
                                fs.Write(data, 0, data.Length)
                            }
                        }
                    }
                }
            }

            #ExEnd:ExtractEmbeddedFileDataFromOLEObject

        }
    }
}
