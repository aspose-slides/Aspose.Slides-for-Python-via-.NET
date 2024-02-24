import aspose.slides as slides


def convert_to_xps_with_options(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Instantiate the XpsOptions class
        xps_options = slides.export.XpsOptions()

        # Save MetaFiles as PNG
        xps_options.save_metafiles_as_png = True

        # Save the presentation to XPS document
        pres.save(global_opts.out_dir + "convert_to_xps_with_options_out.xps", slides.export.SaveFormat.XPS,
                  xps_options)
