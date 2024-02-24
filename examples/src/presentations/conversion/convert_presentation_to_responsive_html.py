import aspose.slides as slides


def convert_to_responsive_html(global_opts):
    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation:
        controller = slides.export.ResponsiveHtmlController()
        html_options = slides.export.HtmlOptions()
        html_options.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(controller)

        # Saving the presentation to HTML
        presentation.save(global_opts.out_dir + "convert_to_responsive_html_out.html", slides.export.SaveFormat.HTML, html_options)
