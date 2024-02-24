import aspose.slides as slides


def save_as_read_only(global_opts):
    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as presentation:
        # ....do some work here.....

        # Setting Write protection Password
        presentation.protection_manager.set_write_protection("test")

        # Save your presentation to a file
        presentation.save(global_opts.out_dir + "save_as_read_only_out.pptx", slides.export.SaveFormat.PPTX)
