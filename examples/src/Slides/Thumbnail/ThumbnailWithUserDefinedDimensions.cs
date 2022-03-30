import aspose.pydrawing as drawing

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Thumbnail
{
    public class ThumbnailWithUserDefinedDimensions
    {
        public static void Run()
        {
            #ExStart:ThumbnailWithUserDefinedDimensions
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Thumbnail()

            # Instantiate a Presentation class that represents the presentation file
            using (Presentation pres = new Presentation(dataDir + "ThumbnailWithUserDefinedDimensions.pptx"))
            {

                # Access the first slide
                sld = pres.slides[0]

                # User defined dimension
                desiredX = 1200
                desiredY = 800

                # Getting scaled value  of X and Y
                ScaleX = (float)(1.0 / pres.SlideSize.size.width) * desiredX
                ScaleY = (float)(1.0 / pres.SlideSize.size.height) * desiredY


                # Create a full scale image
                bmp = sld.get_thumbnail(ScaleX, ScaleY)

                # Save the image to disk in JPEG format
                bmp.save(dataDir + "Thumbnail2_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg)
            }
            #ExEnd:ThumbnailWithUserDefinedDimensions
        }
    }
}