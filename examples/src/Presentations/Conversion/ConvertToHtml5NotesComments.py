import aspose.slides as slides


def convert_to_html5_notes_comments():
    # The path to the documents directory
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "ConvertWithNote.pptx") as pres:
        notes_comments_layouting = slides.export.NotesCommentsLayoutingOptions()
        notes_comments_layouting.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        html5options = slides.export.Html5Options()
        html5options.output_path = outDir + "Html5NotesResult"
        html5options.notes_comments_layouting = notes_comments_layouting

        # Save a result
        pres.save(outDir + "Html5NotesResult.html", slides.export.SaveFormat.HTML5, html5options)
