using System.IO
import aspose.slides as slides
import aspose.pydrawing as drawing
using Aspose.slides.Export

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class AddStretchOffsetForImageFill
    {
        public static void Run()
        {
            #ExStart:AddStretchOffsetForImageFill
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Instantiate the ImageEx class
                img = drawing.Bitmap(dataDir+ "aspose-logo.jpg")
                imgx = pres.images.add_image(img)

                # Add Picture Frame with height and width equivalent of Picture
                sld.shapes.AddPictureFrame(ShapeType.Rectangle, 50, 150, imgx.width, imgx.height, imgx)

                #Write the PPTX file to disk
                pres.save(dataDir + "AddStretchOffsetForImageFill_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddStretchOffsetForImageFill
        }
    }
}