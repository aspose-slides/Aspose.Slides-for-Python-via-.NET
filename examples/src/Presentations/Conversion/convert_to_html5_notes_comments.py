import aspose.slides as slides


def convert_to_html5_notes_comments(global_opts):
    with slides.Presentation(global_opts.data_dir + "ConvertWithNote.pptx") as pres:
        notes_comments_layouting = slides.export.NotesCommentsLayoutingOptions()
        notes_comments_layouting.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        html5_options = slides.export.Html5Options()
        html5_options.output_path = global_opts.out_dir + "Html5NotesResult"
        html5_options.notes_comments_layouting = notes_comments_layouting

        # Save a result
        pres.save(global_opts.out_dir + "Html5NotesResult.html", slides.export.SaveFormat.HTML5, html5_options)
