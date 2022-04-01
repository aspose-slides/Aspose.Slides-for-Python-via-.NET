import aspose.slides as slides

def convert_to_fodp():
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        pres.save(outDir + "convert_to_fodp_out.fodp", slides.export.SaveFormat.FODP)

    with slides.Presentation(outDir + "convert_to_fodp_out.fodp") as pres:
        pres.save(outDir + "convert_to_fodp_out.pptx", slides.export.SaveFormat.PPTX)

