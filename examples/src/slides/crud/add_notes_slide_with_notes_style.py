import aspose.slides as slides


def add_notes_slide_with_notes_style(global_opts):
    # Create an instance of Presentation class
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        notes_master = presentation.master_notes_slide_manager.master_notes_slide

        if notes_master is not None:
            # Get MasterNotesSlide text style
            notes_style = notes_master.notes_style

            # Set symbol bullet for the first level paragraphs
            paragraph_format = notes_style.get_level(0)
            paragraph_format.bullet.type = slides.BulletType.SYMBOL

        # Save the PPTX file to the Disk
        presentation.save(global_opts.out_dir + "crud_AddNotesSlideWithNotesStyle_out.pptx", slides.export.SaveFormat.PPTX)
