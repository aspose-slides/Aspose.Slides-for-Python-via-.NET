import aspose.slides as slides


def printing_preview():
    #ExStart:PrintPreview
    # The path to the documents directory.

    with slides.Presentation() as pres:
        printerSettings = slides.PrinterSettings()
        printerSettings.copies = 2
        printerSettings.default_page_settings.landscape = True
        printerSettings.default_page_settings.margins.left = 10
        #...etc
        pres.print(printerSettings)
    #ExEnd:PrintPreview


