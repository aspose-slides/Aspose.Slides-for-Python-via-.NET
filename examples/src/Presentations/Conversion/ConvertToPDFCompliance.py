import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def convert_to_pdf_compliance():
    presentation_name = dataDir + "ConvertToPDF.pptx"
    out_path = outDir + "ConvertToPDF-Comp.pdf"
    
    with slides.Presentation(presentation_name) as presentation:
        pdf_options = slides.export.PdfOptions() 
        pdf_options.compliance = slides.export.PdfCompliance.PDF_A2A                 
        presentation.save(out_path, slides.export.SaveFormat.PDF, pdf_options)
