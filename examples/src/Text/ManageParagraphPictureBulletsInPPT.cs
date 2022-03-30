using System
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

namespace Aspose.slides.Examples.CSharp.text
{
    class ManageParagraphPictureBulletsInPPT
    {
        public static void Run()
        {
            #ExStart:ManageParagraphPictureBulletsInPPT
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Text()

            with slides.Presentation() as presentation:

            # Accessing the first slide
            slide = presentation.slides[0]

            # Instantiate the image for bullets
            Image image = drawing.Bitmap(dataDir + "bullets.png")
            ippxImage = presentation.images.add_image(image)

            # Adding and accessing Autoshape
            autoShape = slide.shapes.add_auto_shape(ShapeType.Rectangle, 200, 200, 400, 200)

            # Accessing the text frame of created autoshape
            ITextFrame textFrame = autoShape.text_frame

            # Removing the default exisiting paragraph
            textFrame.Paragraphs.remove_at(0)

            # Creating new paragraph
            Paragraph paragraph = new Paragraph()
            paragraph.text = "Welcome to Aspose.Slides"

            # Setting paragraph bullet style and image
            paragraph.ParagraphFormat.Bullet.type = BulletType.picture
            paragraph.ParagraphFormat.Bullet.picture.image = ippxImage

            # Setting Bullet Height
            paragraph.ParagraphFormat.Bullet.height = 100

            # Adding Paragraph to text frame
            textFrame.Paragraphs.add(paragraph)

            # Writing the presentation as a PPTX file
            presentation.save(dataDir + "ParagraphPictureBulletsPPTX_out.pptx", slides.export.SaveFormat.PPTX)
            # Writing the presentation as a PPT file
            presentation.save(dataDir + "ParagraphPictureBulletsPPT_out.ppt", SaveFormat.Ppt)
            #ExEnd:ManageParagraphPictureBulletsInPPT
        }
    }
}