import aspose.slides as slides


def props_read_only_recommended(global_opts):
    with slides.Presentation() as pres:
        pres.protection_manager.read_only_recommended = True
        pres.save(global_opts.out_dir + "props_read_only_recommended_out.pptx", slides.export.SaveFormat.PPTX)
