using System
import aspose.pydrawing as drawing
using System.IO
using Aspose.slides.Export

/*
This example demonstrates the addition of a modern comment to a slide
*/

namespace Aspose.slides.Examples.CSharp.slides.Comments
{
    class ModernComments
    {
        public static void Run()
        {
            # The path to the output file.
            outPptxFile = Path.Combine(RunExamples.OutPath, "ModernComments_out.pptx")

            with slides.Presentation() as pres:
            {
                # Add author
                ICommentAuthor newAuthor = pres.CommentAuthors.AddAuthor("Some Author", "SA")

                # Add comment
                IModernComment modernComment = newAuthor.Comments.AddModernComment("This is a modern comment", pres.slides[0], None, new PointF(100, 100), DateTime.Now)

                # Save presentation
                pres.save(outPptxFile, slides.export.SaveFormat.PPTX)
            }
        }
    }
}