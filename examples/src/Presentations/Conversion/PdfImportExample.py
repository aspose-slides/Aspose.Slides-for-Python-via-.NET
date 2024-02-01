import aspose.slides as slides

dataDir = "./examples/data/"
outDir = "./examples/out/"

def import_from_pdf():
    with slides.Presentation() as pres:
        pres.slides.add_from_pdf(dataDir + "welcome-to-powerpoint.pdf")
        pres.save(outDir + "import_from_pdf_out.pptx", slides.export.SaveFormat.PPTX)
