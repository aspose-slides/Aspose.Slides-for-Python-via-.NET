import aspose.slides as slides
using Aspose.slides.Examples.CSharp
using Aspose.slides.Export
using System
using System.Collections.Generic
import aspose.pydrawing as drawing
using System.Linq
using System.text
using System.Threading.Tasks

namespace CSharp.slides.Comments
{
    class AddParentComments
    {
        public static void Run() {

            #ExStart:AddParentComments
            # The path to the output directory.
            outPptxFile = RunExamples.OutPath

            with slides.Presentation() as pres:
            {
                # Add comment
                ICommentAuthor author1 = pres.CommentAuthors.AddAuthor("Author_1", "A.A.")
                IComment comment1 = author1.Comments.AddComment("comment1", pres.slides[0], new PointF(10, 10), DateTime.Now)

                # Add reply for comment1
                ICommentAuthor author2 = pres.CommentAuthors.AddAuthor("Autror_2", "B.B.")
                IComment reply1 = author2.Comments.AddComment("reply 1 for comment 1", pres.slides[0], new PointF(10, 10), DateTime.Now)
                reply1.ParentComment = comment1

                # Add reply for comment1
                IComment reply2 = author2.Comments.AddComment("reply 2 for comment 1", pres.slides[0], new PointF(10, 10), DateTime.Now)
                reply2.ParentComment = comment1

                # Add reply to reply
                IComment subReply = author1.Comments.AddComment("subreply 3 for reply 2", pres.slides[0], new PointF(10, 10), DateTime.Now)
                subReply.ParentComment = reply2

                IComment comment2 = author2.Comments.AddComment("comment 2", pres.slides[0], new PointF(10, 10), DateTime.Now)
                IComment comment3 = author2.Comments.AddComment("comment 3", pres.slides[0], new PointF(10, 10), DateTime.Now)

                IComment reply3 = author1.Comments.AddComment("reply 4 for comment 3", pres.slides[0], new PointF(10, 10), DateTime.Now)
                reply3.ParentComment = comment3

                # Display hierarchy on console
                slide = pres.slides[0]
                comments = slide.GetSlideComments(None)
                for (i = 0 i < comments.Length i++)
                {
                    IComment comment = comments[i]
                    while (comment.ParentComment != None)
                    {
                        Console.Write("\t")
                        comment = comment.ParentComment
                    }

                    Console.Write("{0} : {1}", comments[i].Author.Name, comments[i].text)
                    print()
                }

                pres.save(outPptxFile + "parent_comment.pptx", slides.export.SaveFormat.PPTX)

                # Remove comment1 and all its replies
                comment1.Remove()

                pres.save(outPptxFile + "remove_comment.pptx", slides.export.SaveFormat.PPTX)
            }
            #ExEnd:AddParentComments
        }
    }
}
