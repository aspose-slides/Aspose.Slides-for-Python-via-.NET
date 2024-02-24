import aspose.slides as slides


def remove_notes_at_specific_slide(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Removing notes of first slide
        notes_slide_manager = presentation.slides[0].notes_slide_manager
        notes_slide_manager.remove_notes_slide()

        # Save presentation to disk
        presentation.save(global_opts.out_dir + "notes_remove_notes_slide_out.pptx", slides.export.SaveFormat.PPTX)
