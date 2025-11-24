import aspose.slides as slides


def convert_to_html5_notes_comments(global_opts):
    with slides.Presentation(global_opts.data_dir + "ConvertWithNote.pptx") as pres:
        slides_layout_options = slides.export.NotesCommentsLayoutingOptions()
        slides_layout_options.notes_position = slides.export.NotesPositions.BOTTOM_TRUNCATED

        html5_options = slides.export.Html5Options()
        html5_options.output_path = global_opts.out_dir + "Html5NotesResult"
        html5_options.slides_layout_options = slides_layout_options

        # Save a result
        pres.save(global_opts.out_dir + "Html5NotesResult.html", slides.export.SaveFormat.HTML5, html5_options)
