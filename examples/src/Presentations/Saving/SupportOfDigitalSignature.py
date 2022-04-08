import aspose.slides as slides

def save_add_digital_signature():
    #ExStart:SupportOfDigitalSignature

    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation() as pres:
        signature = slides.DigitalSignature(dataDir + "cert.pfx", "testpass1")
        signature.comments = "Aspose.Slides digital signing test."
        pres.digital_signatures.add(signature)
        pres.save(outDir + "save_add_digital_signature_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:SupportOfDigitalSignature
