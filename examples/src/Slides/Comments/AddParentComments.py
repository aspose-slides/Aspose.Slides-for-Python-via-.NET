import aspose.slides as slides
import aspose.pydrawing as drawing
from datetime import date


#ExStart:AddParentComments
# The path to the output directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Add comment
    author1 = pres.comment_authors.add_author("Author_1", "A.A.")
    comment1 = author1.comments.add_comment("comment1", pres.slides[0], drawing.PointF(10, 10), date.today())

    # Add reply for comment1
    author2 = pres.comment_authors.add_author("Autror_2", "B.b.")
    reply1 = author2.comments.add_comment("reply 1 for comment 1", pres.slides[0], drawing.PointF(10, 10), date.today())
    reply1.parent_comment = comment1

    # Add reply for comment1
    reply2 = author2.comments.add_comment("reply 2 for comment 1", pres.slides[0], drawing.PointF(10, 10), date.today())
    reply2.parent_comment = comment1

    # Add reply to reply
    subReply = author1.comments.add_comment("subreply 3 for reply 2", pres.slides[0], drawing.PointF(10, 10), date.today())
    subReply.parent_comment = reply2

    comment2 = author2.comments.add_comment("comment 2", pres.slides[0], drawing.PointF(10, 10), date.today())
    comment3 = author2.comments.add_comment("comment 3", pres.slides[0], drawing.PointF(10, 10), date.today())

    reply3 = author1.comments.add_comment("reply 4 for comment 3", pres.slides[0], drawing.PointF(10, 10), date.today())
    reply3.parent_comment = comment3

    # Display hierarchy on console
    slide = pres.slides[0]
    comments = slide.get_slide_comments(None)
    for i in range(len(comments)):
        comment = comments[i]
        while comment.parent_comment != None:
            print("\t")
            comment = comment.parent_comment

        print("{0} : {1}".format(comments[i].author.name, comments[i].text))
        print()

    pres.save(outDir + "comments_parent_comment_out.pptx", slides.export.SaveFormat.PPTX)

    # Remove comment1 and all its replies
    comment1.remove()

    pres.save(outDir + "comments_remove_comment_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:AddParentComments