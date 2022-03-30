import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.IO
using System.Linq
using System.text
using System.Threading.Tasks
using Aspose.slides.DOM.Ole

namespace CSharp.shapes
{
    class SubstitutePictureTitleOfOLEObjectFrame
    {
        public static void Run() {

            #ExStart:SubstitutePictureTitleOfOLEObjectFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()
            oleSourceFile = dataDir +"ExcelObject.xlsx"
            oleIconFile = dataDir + "Image.png"

            with slides.Presentation() as pres:
            {
                image = None
                slide = pres.slides[0]

                # Add Ole objects
                byte[] allbytes = File.ReadAllBytes(oleSourceFile)
                IOleEmbeddedDataInfo dataInfo = new OleEmbeddedDataInfo(allbytes, "xlsx")
                IOleObjectFrame oof = slide.shapes.AddOleObjectFrame(20, 20, 50, 50, dataInfo)
                oof.IsObjectIcon = True

                # Add image object
                byte[] imgBuf = File.ReadAllBytes(oleIconFile)
                using (MemoryStream ms = new MemoryStream(imgBuf))
                {
                    image = pres.images.add_image(drawing.Bitmap(ms))
                }
                oof.substitute_picture_format.picture.image = image

                # Set caption to OLE icon
                oof.SubstitutePictureTitle = "Caption example"
            }

            #ExEnd:SubstitutePictureTitleOfOLEObjectFrame

        }
    }
}
