import aspose.slides as slides


def get_file_format(global_opts):
    info = slides.PresentationFactory.instance.get_presentation_info(global_opts.data_dir + "welcome-to-powerpoint.pptx")
    if info.load_format == slides.LoadFormat.PPTX:
        print("pptx")
    elif info.load_format == slides.LoadFormat.UNKNOWN:
        print("unknown")
