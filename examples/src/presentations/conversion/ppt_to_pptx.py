import aspose.slides as slides


def convert_to_ppt(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        pres.save(global_opts.out_dir + "convert_to_ppt_out.ppt", slides.export.SaveFormat.PPT)

    with slides.Presentation(global_opts.out_dir + "convert_to_ppt_out.ppt") as pres:
        pres.save(global_opts.out_dir + "convert_to_ppt_out.pptx", slides.export.SaveFormat.PPTX)
