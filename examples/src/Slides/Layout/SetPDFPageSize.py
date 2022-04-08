import aspose.slides as slides


#ExStart:SetPDFPageSize
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate a Presentation object that represents a presentation file 
with slides.Presentation() as presentation:
    # Set SlideSize.type Property 
    presentation.slide_size.set_size(slides.SlideSizeType.A4_PAPER,slides.SlideSizeScaleType.ENSURE_FIT)

    # Set different properties of PDF Options
    opts = slides.export.PdfOptions()
    opts.sufficient_resolution = 600

    # Save presentation to disk
    presentation.save(outDir + "layout_set_pdf_page_size_out.pdf", slides.export.SaveFormat.PDF, opts)
#ExEnd:SetPDFPageSize