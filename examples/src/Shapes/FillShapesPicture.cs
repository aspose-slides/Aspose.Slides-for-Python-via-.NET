using System.IO
import aspose.slides as slides
using Aspose.slides.Export
import aspose.pydrawing as drawing

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class FillShapesPicture
    {
        public static void Run()
        {
            #ExStart:FillShapesPicture
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            bool IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PrseetationEx class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of rectangle type
                IShape shp = sld.shapes.add_auto_shape(ShapeType.Rectangle, 50, 150, 75, 150)


                # Set the fill type to Picture
                shp.FillFormat.fill_type = slides.FillType.PICTURE

                # Set the picture fill mode
                shp.FillFormat.picture_fill_format.PictureFillMode = PictureFillMode.Tile

                # Set the picture
                img = drawing.Bitmap(dataDir + "Tulips.jpg")
                imgx = pres.images.add_image(img)
                shp.FillFormat.picture_fill_format.picture.image = imgx

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShpPic_out.pptx", slides.export.SaveFormat.PPTX)
                #ExEnd:FillShapesPicture
            }
        }
    }
}