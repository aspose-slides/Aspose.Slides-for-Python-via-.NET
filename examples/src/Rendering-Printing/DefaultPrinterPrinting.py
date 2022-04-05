import aspose.slides as slides

def printing_default_settings():
    #ExStart:DefaultPrinterPrinting
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Load the presentation
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:

        # Call the print method to print whole presentation to the default printer
        presentation.print()
    #ExEnd:DefaultPrinterPrinting


