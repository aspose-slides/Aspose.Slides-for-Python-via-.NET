import aspose.slides as slides

#ExStart:AccessSlideComments
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate Presentation class
with slides.Presentation(dataDir + "comments.pptx") as presentation:
    for author in presentation.comment_authors:
        for comment in author.comments:
            print(":" + str(comment.slide.slide_number) + " has comment: " + comment.text + " with Author: " + comment.author.name + " posted on time :" + str(comment.created_time) + "\n")
#ExEnd:AccessSlideComments