import aspose.slides as slides


def open_presentation(global_opts):
    # Opening the presentation file by passing the file path to the constructor of Presentation class
    pres = slides.Presentation(global_opts.data_dir + "open_presentation.pptx")

    # Printing the total number of slides present in the presentation
    print("Count of slides in presentation:", len(pres.slides))
