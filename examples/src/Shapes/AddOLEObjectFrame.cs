using System.IO
import aspose.slides as slides
using Aspose.slides.DOM.Ole
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes 
{
    public class AddOLEObjectFrame
    {
        public static void Run()
        {
            #ExStart:AddOLEObjectFrame

            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {
                # Access the first slide
                sld = pres.slides[0]

                # Load an cel file to stream
                MemoryStream mstream = new MemoryStream()
                using (FileStream fs = new FileStream(dataDir + "book1.xlsx", FileMode.Open, FileAccess.Read))
                {
                    byte[] buf = new byte[4096]

                    while (True)
                    {
                        bytesRead = fs.Read(buf, 0, buf.Length)
                        if (bytesRead <= 0)
                            break
                        mstream.Write(buf, 0, bytesRead)
                    }
                }

                # Create data object for embedding
                IOleEmbeddedDataInfo dataInfo = new OleEmbeddedDataInfo(mstream.ToArray(), "xlsx")

                # Add an Ole Object Frame shape
                IOleObjectFrame oleObjectFrame = sld.shapes.AddOleObjectFrame(0, 0, pres.SlideSize.size.width,
                    pres.SlideSize.size.height, dataInfo)

                #Write the PPTX to disk
                pres.save(dataDir + "OleEmbed_out.pptx", slides.export.SaveFormat.PPTX)
            }

            #ExEnd:AddOLEObjectFrame
        }
    }
}