import aspose.slides as slides


def convert_to_pdf_compliance(global_opts):
    with slides.Presentation(global_opts.data_dir + "ConvertToPDF.pptx") as presentation:
        pdf_options = slides.export.PdfOptions()
        pdf_options.compliance = slides.export.PdfCompliance.PDF_A2A
        presentation.save(global_opts.out_dir + "ConvertToPDF-Comp.pdf", slides.export.SaveFormat.PDF, pdf_options)
