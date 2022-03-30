import aspose.pydrawing as drawing
using Aspose.slides.Export
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.shapes
{
    class AddRelativeScaleHeightPictureFrame
    {
        public static void Run()
        {
            #ExStart:AddRelativeScaleHeightPictureFrame
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate presentation object
            with slides.Presentation() as presentation:
            {

                # Load Image to be added in presentaiton image collection
                Image img = drawing.Bitmap(dataDir + "aspose-logo.jpg")
                image = presentation.images.add_image(img)

                # Add picture frame to slide
                IPictureFrame pf = presentation.slides[0].shapes.AddPictureFrame(ShapeType.Rectangle, 50, 50, 100, 100, image)

                # Setting relative scale width and height
                pf.RelativeScaleHeight = 0.8f
                pf.RelativeScaleWidth = 1.35f

                # Save presentation
                presentation.save(dataDir + "Adding Picture Frame with Relative Scale_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddRelativeScaleHeightPictureFrame
        }
    }
}

