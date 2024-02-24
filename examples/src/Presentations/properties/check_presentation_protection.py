import aspose.slides as slides


def props_check_presentation_protection(global_opts):
    # Check the Write Protection Password via IPresentationInfo Interface
    presentation_info = slides.PresentationFactory.instance.get_presentation_info(
        global_opts.data_dir + "props_check_presentation_protection.pptx")
    is_write_protected_by_password = presentation_info.is_write_protected == slides.NullableBool.TRUE and \
        presentation_info.check_write_protection("pass2")
    print("Is presentation write protected by password = " + str(is_write_protected_by_password))

    # Check the Write Protection Password via IProtectionManager Interface
    with slides.Presentation(global_opts.data_dir + "props_check_presentation_protection.pptx") as presentation:
        is_write_protected = presentation.protection_manager.check_write_protection("pass2")
        print("Is presentation write protected = " + str(is_write_protected))

    # Check Presentation Open Protection via IPresentationInfo Interface
    presentation_info = slides.PresentationFactory.instance.get_presentation_info(
        global_opts.data_dir + "props_ppt_with_password.ppt")
    if presentation_info.is_password_protected:
        print("The presentation 'props_ppt_with_password.ppt' is protected by password to open.")
