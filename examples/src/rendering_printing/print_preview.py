import aspose.slides as slides


def printing_preview():
    with slides.Presentation() as pres:
        printer_settings = slides.PrinterSettings()
        printer_settings.copies = 2
        printer_settings.default_page_settings.landscape = True
        printer_settings.default_page_settings.margins.left = 10

        pres.print(printer_settings)
