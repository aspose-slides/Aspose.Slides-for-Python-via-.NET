import aspose.pydrawing as drawing
using System.Drawing.Imaging
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
    class CreateBoundsShapeThumbnail
    {
        public static void Run()
        {
            #ExStart:CreateBoundsShapeThumbnail
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Shapes()

            # Instantiate a Presentation class that represents the presentation file
            using (Presentation presentation = new Presentation(dataDir + "HelloWorld.pptx"))
            {
                # Create a Appearance bound shape image
                using (bitmap = presentation.slides[0].shapes[0].get_thumbnail(ShapeThumbnailBounds.Appearance, 1, 1))
                {
                    # Save the image to disk in PNG format
                    bitmap.save(dataDir + "Shape_thumbnail_Bound_Shape_out.png", drawing.imaging.ImageFormat.png)
                }
            }
            #ExEnd:CreateBoundsShapeThumbnail
        }
    }
}



