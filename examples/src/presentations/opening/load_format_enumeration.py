import aspose.slides as slides


def load_format_enumeration(global_opts):
    is_old_format = slides.PresentationFactory.instance.get_presentation_info(
        global_opts.data_dir + "open_presentation.ppt").load_format == slides.LoadFormat.PPT95
    print("load_format_enumeration:", is_old_format)
