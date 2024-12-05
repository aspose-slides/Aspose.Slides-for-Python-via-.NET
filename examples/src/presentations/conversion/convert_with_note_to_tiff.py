import aspose.slides as slides


def convert_to_tiff_with_notes(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "presentation_with_notes.pptx") as pres:
        tiff_options = slides.export.TiffOptions()
        slides_layout_options = slides.export.NotesCommentsLayoutingOptions()
        slides_layout_options.notes_position = slides.export.NotesPositions.BOTTOM_FULL
        tiff_options.slides_layout_options = slides_layout_options
        # Saving the presentation to TIFF notes
        pres.save(global_opts.out_dir + "convert_to_tiff_with_notes_out.tiff", slides.export.SaveFormat.TIFF, tiff_options)
