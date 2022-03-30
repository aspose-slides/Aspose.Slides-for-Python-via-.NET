import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using Aspose.slides.SmartArt
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.SmartArts
{
    class BulletFillFormat
    {
        public static void Run() {

            #ExStart:BulletFillFormat
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_SmartArts()

            with slides.Presentation() as presentation:
            {
                ISmartArt smart = presentation.slides[0].shapes.AddSmartArt(10, 10, 500, 400, SmartArtLayoutType.VerticalPictureList)
                ISmartArtNode node = smart.AllNodes[0]

                if (node.BulletFillFormat != None)
                {
                    img = (Image)drawing.Bitmap(dataDir + "aspose-logo.jpg")
                    image = presentation.images.add_image(img)
                    node.BulletFillFormat.fill_type = slides.FillType.PICTURE
                    node.BulletFillFormat.picture_fill_format.picture.image = image
                    node.BulletFillFormat.picture_fill_format.PictureFillMode = PictureFillMode.Stretch
                }
                presentation.save(dataDir +"out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:BulletFillFormat
        }
    }
}
