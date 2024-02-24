import aspose.slides as slides


def convert_to_fodp(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        pres.save(global_opts.out_dir + "convert_to_fodp_out.fodp", slides.export.SaveFormat.FODP)

    with slides.Presentation(global_opts.out_dir + "convert_to_fodp_out.fodp") as pres:
        pres.save(global_opts.out_dir + "convert_to_fodp_out.pptx", slides.export.SaveFormat.PPTX)
