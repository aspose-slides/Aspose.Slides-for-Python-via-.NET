import aspose.slides as slides

def props_read_only_recommended():
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        pres.protection_manager.read_only_recommended = True
        pres.save(outDir + "props_read_only_recommended_out.pptx", slides.export.SaveFormat.PPTX)
