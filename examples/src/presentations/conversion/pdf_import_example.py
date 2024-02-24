import aspose.slides as slides


def import_from_pdf(global_opts):
    with slides.Presentation() as pres:
        pres.slides.add_from_pdf(global_opts.data_dir + "welcome-to-powerpoint.pdf")
        pres.save(global_opts.out_dir + "import_from_pdf_out.pptx", slides.export.SaveFormat.PPTX)
