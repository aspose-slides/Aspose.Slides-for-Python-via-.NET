import aspose.slides as slides


def convert_to_odp(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        pres.save(global_opts.out_dir + "convert_to_odp_out.odp", slides.export.SaveFormat.ODP)

    with slides.Presentation(global_opts.out_dir + "convert_to_odp_out.odp") as pres:
        pres.save(global_opts.out_dir + "convert_to_odp_out.pptx", slides.export.SaveFormat.PPTX)
