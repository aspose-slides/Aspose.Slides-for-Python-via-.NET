import aspose.slides as slides


def convert_to_xps(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Saving the presentation to XPS document
        pres.save(global_opts.out_dir + "convert_to_xps_out.xps", slides.export.SaveFormat.XPS)
