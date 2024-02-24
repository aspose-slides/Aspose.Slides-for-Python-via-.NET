import aspose.slides as slides


def save_add_digital_signature(global_opts):
    with slides.Presentation() as pres:
        signature = slides.DigitalSignature(global_opts.data_dir + "cert.pfx", "testpass1")
        signature.comments = "Aspose.Slides digital signing test."
        pres.digital_signatures.add(signature)
        pres.save(global_opts.out_dir + "save_add_digital_signature_out.pptx", slides.export.SaveFormat.PPTX)
