import aspose.slides as slides


def save_in_zip64_mode(global_opts):
    with slides.Presentation() as presentation:
        pptx_options = slides.export.PptxOptions()
        pptx_options.zip_64_mode = slides.export.Zip64Mode.ALWAYS
        presentation.save(global_opts.out_dir + "PresentationZip64.pptx", slides.export.SaveFormat.PPTX, pptx_options)
