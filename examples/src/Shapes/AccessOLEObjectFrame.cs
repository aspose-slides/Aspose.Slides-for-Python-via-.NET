using System.IO
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AccessOLEObjectFrame
    {
        public static void Run()
        {
            #ExStart:AccessOLEObjectFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Load the PPTX to Presentation object
            using (Presentation pres = new Presentation(dataDir + "AccessingOLEObjectFrame.pptx"))
            {
                # Access the first slide
                sld = pres.slides[0]

                # Cast the shape to OleObjectFrame
                OleObjectFrame oleObjectFrame = sld.shapes[0] as OleObjectFrame

                # Read the OLE Object and write it to disk
                if (oleObjectFrame != None)
                {
                    # Get embedded file data
                    byte[] data = oleObjectFrame.EmbeddedData.EmbeddedFileData

                    # Get embedded file extention
                    fileExtention = oleObjectFrame.EmbeddedData.EmbeddedFileExtension

                    # Create path for saving the extracted file
                    extractedPath = dataDir + "excelFromOLE_out" + fileExtention

                    # Save extracted data
                    using (FileStream fstr = new FileStream(extractedPath, FileMode.Create, FileAccess.Write))
                    {
                        fstr.Write(data, 0, data.Length)
                    }
                }
            }

            #ExEnd:AccessOLEObjectFrame
        }
    }
}