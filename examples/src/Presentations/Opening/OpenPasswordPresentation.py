import aspose.slides as slides

def open_password_presentation():
    #ExStart:OpenPasswordPresentation
    # The path to the documents directory.
    dataDir = "./examples/data/"

    # creating instance of load options to set the presentation access password
    loadOptions = slides.LoadOptions()

    # Setting the access password
    loadOptions.password = "pass"

    # Opening the presentation file by passing the file path and load options to the constructor of Presentation class
    pres = slides.Presentation(dataDir + "OpenPasswordPresentation.pptx", loadOptions)

    # Printing the total number of slides present in the presentation
    print(len(pres.slides))
    #ExEnd:OpenPasswordPresentation

