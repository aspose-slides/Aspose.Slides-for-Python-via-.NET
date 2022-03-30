using Aspose.slides.Export
import aspose.slides as slides
import aspose.pydrawing as drawing
using System.Drawing.Imaging
using System.IO

namespace Aspose.slides.Examples.CSharp.Rendering.Printing
{
    # This example demonstrates one of the possible use cases of IRenderingOptions interface
    #(getting slide thumbnails with different default font and slide's notes shown)

    class RenderOptions
    {
        public static void Run()
        {
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Rendering()
            presPath = Path.Combine(dataDir, "RenderingOptions.pptx")

            using (Presentation pres = new Presentation(presPath))
            {
                IRenderingOptions renderingOpts = new RenderingOptions()
                renderingOpts.NotesCommentsLayouting.NotesPosition = NotesPositions.BottomTruncated

                pres.slides[0].GetThumbnail(renderingOpts, 4 / 3f, 4 / 3f).save(Path.Combine(RunExamples.OutPath, "RenderingOptions-Slide1-Original.png"), ImageFormat.Png)

                renderingOpts.NotesCommentsLayouting.NotesPosition = NotesPositions.NONE
                renderingOpts.DefaultRegularFont = "Arial Black"
                pres.slides[0].GetThumbnail(renderingOpts, 4 / 3f, 4 / 3f).save(Path.Combine(RunExamples.OutPath, "RenderingOptions-Slide1-ArialBlackDefault.png"), ImageFormat.Png)

                renderingOpts.DefaultRegularFont = "Arial Narrow"
                pres.slides[0].GetThumbnail(renderingOpts, 4 / 3f, 4 / 3f).save(Path.Combine(RunExamples.OutPath, "RenderingOptions-Slide1-ArialNarrowDefault.png"), ImageFormat.Png)
            }
        }
    }
}


