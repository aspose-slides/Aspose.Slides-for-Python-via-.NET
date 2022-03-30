import aspose.slides as slides

def open_presentation():
    #ExStart:OpenPresentation
    # The path to the documents directory.
    dataDir = "./examples/data/"

    # Opening the presentation file by passing the file path to the constructor of Presentation class
    pres = slides.Presentation(dataDir + "OpenPresentation.pptx")

    # Printing the total number of slides present in the presentation
    print(len(pres.slides))
    #ExEnd:OpenPresentation
