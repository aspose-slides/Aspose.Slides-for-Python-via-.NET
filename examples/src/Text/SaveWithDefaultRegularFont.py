import aspose.pydrawing as drawing
import aspose.slides as slides

dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "text_default_fonts.pptx") as pres:
    htmlOpts = slides.export.HtmlOptions()
    htmlOpts.default_regular_font = "Arial Black"
    pres.save(outDir + "text_Presentation-out-ArialBlack.html", slides.export.SaveFormat.HTML, htmlOpts)
    
    htmlOpts.default_regular_font = "Lucida Console"
    pres.save(outDir + "text_Presentation-out-LucidaConsole.html", slides.export.SaveFormat.HTML, htmlOpts)

    pdfOpts = slides.export.PdfOptions()
    pdfOpts.default_regular_font = "Arial Black"
    pres.save(outDir + "text_Presentation-out-ArialBlack.pdf", slides.export.SaveFormat.PDF, pdfOpts)