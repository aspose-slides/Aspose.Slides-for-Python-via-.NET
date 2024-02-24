import aspose.slides as slides


def props_check_password(global_opts):
    # The example below demonstrates how to check a password to open a presentation

    # Check the Password via IPresentationInfo Interface
    presentation_info = slides.PresentationFactory.instance.get_presentation_info(
        global_opts.data_dir + "props_ppt_with_password.ppt")
    is_password_correct = presentation_info.check_password("my_password")
    print("The password \"my_password\" for the presentation is " + str(is_password_correct))

    is_password_correct = presentation_info.check_password("pass1")
    print("The password \"pass1\" for the presentation is " + str(is_password_correct))
