import aspose.slides as slides


def convert_to_swf(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        swf_options = slides.export.SwfOptions()
        swf_options.viewer_included = False

        notes_options = swf_options.notes_comments_layouting
        notes_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL

        # Saving presentation and notes pages
        presentation.save(global_opts.out_dir + "convet_to_swf_out.swf", slides.export.SaveFormat.SWF, swf_options)

        swf_options.viewer_included = True
        presentation.save(global_opts.out_dir + "convet_to_swf_with_notes_out.swf", slides.export.SaveFormat.SWF,
                          swf_options)
