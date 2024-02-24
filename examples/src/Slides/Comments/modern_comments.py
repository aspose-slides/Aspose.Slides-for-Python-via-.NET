import aspose.pydrawing as drawing
import aspose.slides as slides
from datetime import date


def modern_comments(global_opts):
    """This example demonstrates the addition of a modern comment to a slide"""
    with slides.Presentation() as pres:
        # Add author
        new_author = pres.comment_authors.add_author("Some Author", "SA")

        # Add comment
        modern_comment = new_author.comments.add_modern_comment("This is a modern comment", pres.slides[0], None,
                                                                drawing.PointF(100, 100), date.today())

        # Save presentation
        pres.save(global_opts.out_dir + "comments_add_modern_comment_out.pptx", slides.export.SaveFormat.PPTX)
