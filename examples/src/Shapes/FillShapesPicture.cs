using System.IO
import aspose.slides as slides
import aspose.slides as slides
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
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate PrseetationEx class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Add autoshape of rectangle type
                shp = sld.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)


                # Set the fill type to Picture
                shp.fill_format.fill_type = slides.FillType.PICTURE

                # Set the picture fill mode
                shp.fill_format.picture_fill_format.PictureFillMode = PictureFillMode.Tile

                # Set the picture
                img = drawing.Bitmap(dataDir + "Tulips.jpg")
                imgx = pres.images.add_image(img)
                shp.fill_format.picture_fill_format.picture.image = imgx

                #Write the PPTX file to disk
                pres.save(dataDir + "RectShpPic_out.pptx", slides.export.SaveFormat.PPTX)
                #ExEnd:FillShapesPicture
            }
        }
    }
}