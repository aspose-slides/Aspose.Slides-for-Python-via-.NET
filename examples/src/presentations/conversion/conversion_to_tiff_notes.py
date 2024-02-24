import aspose.slides as slides


def convert_to_tiff_notes(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "presentation_with_notes.pptx") as presentation:
        # Saving the presentation to TIFF notes
        presentation.save(global_opts.out_dir + "convert_to_tiff_notes_out.tiff", slides.export.SaveFormat.TIFF)
