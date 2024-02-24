import aspose.slides as slides


def access_slide_comments(global_opts):
    # Instantiate Presentation class
    with slides.Presentation(global_opts.data_dir + "comments.pptx") as presentation:
        for author in presentation.comment_authors:
            for comment in author.comments:
                print("Slide {0} has comment '{1}' with author '{2}' posted on time {3}".format(
                    comment.slide.slide_number, comment.text, comment.author.name, comment.created_time))
