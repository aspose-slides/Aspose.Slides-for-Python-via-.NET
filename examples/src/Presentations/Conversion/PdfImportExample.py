import aspose.slides as slides

def import_from_pdf():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        pres.slides.add_from_pdf(dataDir + "welcome-to-powerpoint.pdf")
        pres.save(outDir + "import_from_pdf_out.pptx", slides.export.SaveFormat.PPTX)