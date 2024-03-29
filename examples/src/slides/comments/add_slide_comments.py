﻿import aspose.pydrawing as drawing
import aspose.slides as slides
from datetime import date


def add_slide_comments(global_opts):
    # Instantiate Presentation class
    with slides.Presentation() as presentation:
        # Adding Empty slide
        presentation.slides.add_empty_slide(presentation.layout_slides[0])

        # Adding Author
        author = presentation.comment_authors.add_author("Jawad", "MF")

        # Position of comments
        point = drawing.PointF()
        point.x = 0.2
        point.y = 0.2

        # Adding slide comment for an author on slide 1
        author.comments.add_comment("Hello Jawad, this is slide comment", presentation.slides[0], point, date.today())

        # Adding slide comment for an author on slide 1
        author.comments.add_comment("Hello Jawad, this is second slide comment", presentation.slides[1], point, date.today())

        # Accessing 1
        slide = presentation.slides[0]

        # if None is passed as an argument then it will bring comments from all authors on selected slide
        comments = slide.get_slide_comments(author)

        if len(comments) > 0:
            # Select comments collection of Author at index 0
            comment = comments[0].author.comments
            comment_text = comment[0].text

        presentation.save(global_opts.out_dir + "comments_add_comment_out.pptx", slides.export.SaveFormat.PPTX)
