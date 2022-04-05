using System.IO
import aspose.slides as slides
import aspose.pydrawing as drawing
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class StretchOffsetLeftForPictureFrame
    {
        public static void Run()
        {
            #ExStart:StretchOffsetLeftForPictureFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Prseetation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                slide = pres.slides[0]

                # Instantiate the ImageEx class
                img = drawing.Bitmap(dataDir + "aspose-logo.jpg")
                imgEx = pres.images.add_image(img)

                # Add an AutoShape of Rectangle type
                aShape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 300, 300)

                # Set shape's fill type
                aShape.fill_format.fill_type = slides.FillType.PICTURE

                # Set shape's picture fill mode
                aShape.fill_format.picture_fill_format.PictureFillMode = PictureFillMode.Stretch

                # Set image to fill the shape
                aShape.fill_format.picture_fill_format.picture.image = imgEx

                # Specify image offsets from the corresponding edge of the shape's bounding box
                aShape.fill_format.picture_fill_format.StretchOffsetLeft = 25
                aShape.fill_format.picture_fill_format.StretchOffsetRight = 25
                aShape.fill_format.picture_fill_format.StretchOffsetTop = -20
                aShape.fill_format.picture_fill_format.StretchOffsetBottom = -10


                #Write the PPTX file to disk
                pres.save(dataDir + "StretchOffsetLeftForPictureFrame_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:StretchOffsetLeftForPictureFrame
        }
    }
}
