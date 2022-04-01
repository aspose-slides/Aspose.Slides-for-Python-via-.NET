import aspose.slides as slides

def convert_to_odp():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        pres.save(outDir + "convert_to_odp_out.odp", slides.export.SaveFormat.ODP)

    with slides.Presentation(outDir + "convert_to_odp_out.odp") as pres:
        pres.save(outDir + "convert_to_odp_out.pptx", slides.export.SaveFormat.PPTX)