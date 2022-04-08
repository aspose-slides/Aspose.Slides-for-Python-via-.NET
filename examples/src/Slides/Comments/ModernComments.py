import aspose.pydrawing as drawing
import aspose.slides as slides
from datetime import date

"""
This example demonstrates the addition of a modern comment to a slide
"""

# The path to the output file.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as pres:
    # Add author
    newAuthor = pres.comment_authors.add_author("Some Author", "SA")

    # Add comment
    modernComment = newAuthor.comments.add_modern_comment("This is a modern comment", pres.slides[0], None, drawing.PointF(100, 100), date.today())

    # Save presentation
    pres.save(outDir + "comments_add_modern_comment_out.pptx", slides.export.SaveFormat.PPTX)