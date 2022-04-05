using System.IO

import aspose.slides as slides
import aspose.pydrawing as drawing
import aspose.slides as slides

namespace Aspose.slides.Examples.CSharp.shapes
{
    public class PictureFrameFormatting
    {
        public static void Run()
        {
            #ExStart:PictureFrameFormatting
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Create directory if it is not already present.
            IsExists = System.IO.Directory.Exists(dataDir)
            if (!IsExists)
                System.IO.Directory.CreateDirectory(dataDir)

            # Instantiate Presentation class that represents the PPTX
            with slides.Presentation() as pres:
            {

                # Get the first slide
                sld = pres.slides[0]

                # Instantiate the ImageEx class
                img = drawing.Bitmap(dataDir+ "aspose-logo.jpg")
                imgx = pres.images.add_image(img)

                # Add Picture Frame with height and width equivalent of Picture
                pf = sld.shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 50, 150, imgx.width, imgx.height, imgx)

                # Apply some formatting to PictureFrameEx
                pf.line_format.fill_format.fill_type = slides.FillType.SOLID
                pf.line_format.fill_format.solid_fill_color.color = drawing.Color.blue
                pf.line_format.width = 20
                pf.rotation = 45

                #Write the PPTX file to disk
                pres.save(dataDir + "RectPicFrameFormat_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:PictureFrameFormatting            
        }
    }
}