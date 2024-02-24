import aspose.slides as slides


def open_set_access_permissions_to_pdf(global_opts):
    pdf_options = slides.export.PdfOptions()
    pdf_options.password = "my_password"
    pdf_options.access_permissions = slides.export.PdfAccessPermissions.PRINT_DOCUMENT | slides.export.PdfAccessPermissions.HIGH_QUALITY_PRINT

    with slides.Presentation() as presentation:
        presentation.save(global_opts.out_dir + "open_set_access_permissions_to_pdf_out.pdf",
                          slides.export.SaveFormat.PDF, pdf_options)
