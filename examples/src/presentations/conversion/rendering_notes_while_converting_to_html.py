import aspose.slides as slides


def convert_to_html_with_notes(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        html_options = slides.export.HtmlOptions()

        slides_layout_options = slides.export.NotesCommentsLayoutingOptions()
        slides_layout_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL
        html_options.slides_layout_options = slides_layout_options

        # Saving notes pages
        pres.save(global_opts.out_dir + "convert_to_html_with_notes_out.html", slides.export.SaveFormat.HTML,
                  html_options)
