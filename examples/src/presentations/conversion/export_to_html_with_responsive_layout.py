import aspose.slides as slides


def convert_to_html_with_responsive_layout(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        html_options = slides.export.HtmlOptions()
        html_options.svg_responsive_layout = True
        presentation.save(global_opts.out_dir + "convert_to_html_with_responsive_layout_out.html",
                          slides.export.SaveFormat.HTML, html_options)
