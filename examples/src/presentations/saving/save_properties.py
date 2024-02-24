import aspose.slides as slides


def save_properties(global_opts):
    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as presentation:
        # ....do some work here.....

        # Setting access to document properties in password protected mode
        presentation.protection_manager.encrypt_document_properties = False

        # Setting Password
        presentation.protection_manager.encrypt("pass")

        # Save your presentation to a file
        presentation.save(global_opts.out_dir + "save_properties_out.pptx", slides.export.SaveFormat.PPTX)
