import aspose.slides as slides


def external_url_original(global_opts):
    with slides.Presentation(global_opts.data_dir + "ExternalUrlOriginal.pptx") as presentation:
        portion = presentation.slides[0].shapes[1].text_frame.paragraphs[0].portions[0]

        external_url = portion.portion_format.hyperlink_click.external_url
        external_url_original = portion.portion_format.hyperlink_click.external_url_original

        print("Fake External Hyperlink :", external_url)
        print("Real External Hyperlink :", external_url_original)
