import aspose.slides as slides


def convert_to_tiff(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        # Saving the presentation to TIFF document
        presentation.save(global_opts.out_dir + "convert_to_tiff_out.tiff", slides.export.SaveFormat.TIFF)
