import aspose.pydrawing as drawing
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Background
{
    public class SetImageAsBackground
    {
        public static void Run()
        {
            #ExStart:SetImageAsBackground
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Background()

            # Instantiate the Presentation class that represents the presentation file
            using (Presentation pres = new Presentation(dataDir + "SetImageAsBackground.pptx"))
            {

                # Set the background with Image
                pres.slides[0].Background.type = BackgroundType.OwnBackground
                pres.slides[0].Background.FillFormat.fill_type = slides.FillType.PICTURE
                pres.slides[0].Background.FillFormat.picture_fill_format.PictureFillMode = PictureFillMode.Stretch

                # Set the picture
                img = drawing.Bitmap(dataDir + "Tulips.jpg")

                # Add image to presentation's images collection
                imgx = pres.images.add_image(img)

                pres.slides[0].Background.FillFormat.picture_fill_format.picture.image = imgx

                # Write the presentation to disk
                pres.save(dataDir + "ContentBG_Img_out.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:SetImageAsBackground
        }
    }
}