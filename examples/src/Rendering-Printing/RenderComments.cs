using Aspose.slides.Export
import aspose.slides as slides
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.IO

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.Rendering.Printing
{
    class RenderComments
    {
        public static void Run()
        {
            #ExStart:RenderComments
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Rendering()
            resultPath = Path.Combine(RunExamples.OutPath, "OutPresBitmap_Comments.png")

            Presentation pres = new Presentation(dataDir + "presentation.pptx")
            bmp = drawing.Bitmap(740, 960)

            IRenderingOptions renderOptions = new RenderingOptions()
            renderOptions.NotesCommentsLayouting.CommentsAreaColor = drawing.Color.red
            renderOptions.NotesCommentsLayouting.CommentsAreaWidth = 200
            renderOptions.NotesCommentsLayouting.CommentsPosition = CommentsPositions.Right
            renderOptions.NotesCommentsLayouting.NotesPosition = NotesPositions.BottomTruncated

            using (graphics = drawing.Graphics.from_image(bmp))
            {
                pres.slides[0].RenderToGraphics(renderOptions, graphics)
            }

            bmp.save(resultPath, ImageFormat.Png)
            System.Diagnostics.Process.Start(resultPath)

        }

    }

    #ExEnd:RenderComments
}
    

