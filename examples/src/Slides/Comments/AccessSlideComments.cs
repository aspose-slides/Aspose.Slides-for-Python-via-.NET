using System
import aspose.slides as slides

/*
This project uses Automatic Package Restore feature of NuGet to resolve Aspose.Slides for .NET API reference 
when the project is build. Please check https:#docs.nuget.org/consume/nuget-faq for more information. 
If you do not wish to use NuGet, you can manually download Aspose.Slides for .NET API from http:#www.aspose.com/downloads, 
install it and then add its reference to this project. For any issues, questions or suggestions 
please feel free to contact us using http:#www.aspose.com/community/forums/default.aspx
*/

namespace Aspose.slides.Examples.CSharp.slides.Comments
{
    class AccessSlideComments
    {
        public static void Run()
        {
            #ExStart:AccessSlideComments
            # The path to the documents directory.
            dataDir = RunExamples.GetDataDir_Slides_Presentations_Comments()

            # Instantiate Presentation class
            using (Presentation presentation = new Presentation(dataDir + "Comments1.pptx"))
            {
                foreach (commentAuthor in presentation.CommentAuthors)
                {
                    author = (CommentAuthor) commentAuthor
                    foreach (comment1 in author.Comments)
                    {
                        comment = (Comment) comment1
                        print(":" + comment.Slide.SlideNumber + " has comment: " + comment.text + " with Author: " + comment.Author.Name + " posted on time :" + comment.CreatedTime + "\n")
                    }
                }
            }
            #ExEnd:AccessSlideComments
        }
    }
}