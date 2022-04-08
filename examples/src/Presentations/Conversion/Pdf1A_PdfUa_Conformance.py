import aspose.slides as slides

def convert_to_pdf_with_compliance():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        options = slides.export.PdfOptions()

        options.compliance = slides.export.PdfCompliance.PDF_A1A
        presentation.save(outDir + "convert_to_pdf_a1a__out.pdf", slides.export.SaveFormat.PDF, options)

        options.compliance = slides.export.PdfCompliance.PDF_A1B
        presentation.save(outDir + "convert_to_pdf_a1b_out.pdf", slides.export.SaveFormat.PDF, options)

        options.compliance = slides.export.PdfCompliance.PDF_UA
        presentation.save(outDir + "convert_to_pdf_ua_out.pdf", slides.export.SaveFormat.PDF, options)
