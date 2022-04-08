import aspose.slides as slides

def convert_to_html_with_notes():
    #ExStart:RenderingNotesWhileConvertingToHTML
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        opt = slides.export.HtmlOptions()

        options = opt.notes_comments_layouting
        options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        # Saving notes pages
        pres.save(outDir + "convert_to_html_with_notes_out.html", slides.export.SaveFormat.HTML, opt)
    #ExEnd:RenderingNotesWhileConvertingToHTML