import aspose.slides as slides
import os


def convert_to_html_with_media(global_opts):
    html_document_file_name = global_opts.out_dir + "convert_to_html_with_media_out.html"
    content_dir = global_opts.out_dir + "convert_to_html_with_media_out"

    with slides.Presentation(global_opts.data_dir + "presentation_with_media.pptx") as pres:
        try:
            os.rmdir(content_dir)
        except OSError:
            pass

        os.makedirs(content_dir, exist_ok=True)
        controller = slides.export.VideoPlayerHtmlController(content_dir, html_document_file_name, "http://www.example.com/")

        html_options = slides.export.HtmlOptions(controller)
        svg_options = slides.export.SVGOptions(controller)

        html_options.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(controller)
        html_options.slide_image_format = slides.export.SlideImageFormat.svg(svg_options)

        pres.save(html_document_file_name, slides.export.SaveFormat.HTML, html_options)
