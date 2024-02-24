import aspose.slides as slides


def open_password_presentation(global_opts):
    # creating instance of load options to set the presentation access password
    load_options = slides.LoadOptions()

    # Setting the access password
    load_options.password = "pass"

    # Opening the presentation file by passing the file path and load options to the constructor of Presentation class
    pres = slides.Presentation(global_opts.data_dir + "open_password.pptx", load_options)

    # Printing the total number of slides present in the presentation
    print("Count of slides in password protected presentation:", len(pres.slides))
