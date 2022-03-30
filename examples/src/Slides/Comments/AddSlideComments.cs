using System
import aspose.pydrawing as drawing
using System.IO
using Aspose.slides.Export

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Comments
{
    class AddSlideComments
    {
        public static void Run()
        {
            #ExStart:AddSlideComments
            # The path to the output file.
            outPptxFile = Path.Combine(RunExamples.OutPath, "Comments_out.pptx")
            # Instantiate Presentation class

            with slides.Presentation() as presentation:
            {
                # Adding Empty slide
                presentation.slides.AddEmptySlide(presentation.LayoutSlides[0])

                # Adding Author
                ICommentAuthor author = presentation.CommentAuthors.AddAuthor("Jawad", "MF")

                # Position of comments
                PointF point = new PointF()
                point.x = 0.2f
                point.y = 0.2f

                # Adding slide comment for an author on slide 1
                author.Comments.AddComment("Hello Jawad, this is slide comment", presentation.slides[0], point, DateTime.Now)

                # Adding slide comment for an author on slide 1
                author.Comments.AddComment("Hello Jawad, this is second slide comment", presentation.slides[1], point, DateTime.Now)

                # Accessing 1
                slide = presentation.slides[0]

                # if None is passed as an argument then it will bring comments from all authors on selected slide
                IComment[] Comments = slide.GetSlideComments(author)

                # Accessin the comment at index 0 for slide 1
                str = Comments[0].text

                presentation.save(outPptxFile, slides.export.SaveFormat.PPTX)

                if (Comments.GetLength(0) > 0)
                {
                    # Select comments collection of Author at index 0
                    ICommentCollection commentCollection = Comments[0].Author.Comments
                    Comment = commentCollection[0].text
                }
            }
            #ExEnd:AddSlideComments
        }
    }
}