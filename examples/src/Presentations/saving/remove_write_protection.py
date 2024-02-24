import aspose.slides as slides


def save_remove_write_protection(global_opts):
    # Opening the presentation file
    with slides.Presentation(global_opts.data_dir + "save_remove_write_protection.pptx") as presentation:
        # Checking if presentation is write-protected
        if presentation.protection_manager.is_write_protected:
            # Removing Write protection                
            presentation.protection_manager.remove_write_protection()

        # Saving presentation
        presentation.save(global_opts.out_dir + "save_remove_write_protection_out.pptx", slides.export.SaveFormat.PPTX)
