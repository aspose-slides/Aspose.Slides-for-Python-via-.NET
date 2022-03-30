import aspose.slides as slides


def set_access_permissions_to_pdf():
    #ExStart:SetAccessPermissionsToPDF

    outDir = "./examples/out/"

    pdfOptions = slides.export.PdfOptions()
    pdfOptions.password = "my_password"
    pdfOptions.access_permissions = slides.export.PdfAccessPermissions.PRINT_DOCUMENT | slides.export.PdfAccessPermissions.HIGH_QUALITY_PRINT

    with slides.Presentation() as presentation:
        presentation.save(outDir + "PDFWithPermissions.pdf", slides.export.SaveFormat.PDF, pdfOptions)
    #ExEnd:SetAccessPermissionsToPDF

