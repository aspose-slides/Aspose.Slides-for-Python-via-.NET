import aspose.slides as slides

def convert_to_ppt():  
    #ExStart:PPTtoPPTX
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        pres.save(outDir + "convert_to_ppt_out.ppt", slides.export.SaveFormat.PPT)

    with slides.Presentation(outDir + "convert_to_ppt_out.ppt") as pres:
        pres.save(outDir + "convert_to_ppt_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:PPTtoPPTX