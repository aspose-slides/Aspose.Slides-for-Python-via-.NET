import aspose.slides as slides


def convert_to_pdf_with_compliance(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        pdf_options = slides.export.PdfOptions()

        pdf_options.compliance = slides.export.PdfCompliance.PDF_A1A
        presentation.save(global_opts.out_dir + "convert_to_pdf_a1a__out.pdf", slides.export.SaveFormat.PDF,
                          pdf_options)

        pdf_options.compliance = slides.export.PdfCompliance.PDF_A1B
        presentation.save(global_opts.out_dir + "convert_to_pdf_a1b_out.pdf", slides.export.SaveFormat.PDF, pdf_options)

        pdf_options.compliance = slides.export.PdfCompliance.PDF_UA
        presentation.save(global_opts.out_dir + "convert_to_pdf_ua_out.pdf", slides.export.SaveFormat.PDF, pdf_options)
