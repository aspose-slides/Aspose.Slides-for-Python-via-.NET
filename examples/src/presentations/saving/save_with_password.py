import aspose.slides as slides


def save_with_password(global_opts):
    # Instantiate a Presentation object that represents a PPT file
    with slides.Presentation() as pres:
        # ....do some work here.....

        # Setting Password
        pres.protection_manager.encrypt("pass")

        # Save your presentation to a file
        pres.save(global_opts.out_dir + "save_with_password_out.pptx", slides.export.SaveFormat.PPTX)
