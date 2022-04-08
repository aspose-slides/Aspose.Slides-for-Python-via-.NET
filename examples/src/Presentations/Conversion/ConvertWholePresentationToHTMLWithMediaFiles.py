import aspose.slides as slides


def convert_to_html_with_media():
    #ExStart:ConvertWholePresentationToHTMLWithMediaFiles
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    htmlDocumentFileName = outDir + "convert_to_html_with_media_out.html"

    with slides.Presentation(dataDir + "presentation_with_media.pptx") as pres:
        controller = slides.export.VideoPlayerHtmlController("", htmlDocumentFileName, "http://www.example.com/")

        htmlOptions = slides.export.HtmlOptions(controller)
        svgOptions = slides.export.SVGOptions(controller)

        htmlOptions.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(controller)
        htmlOptions.slide_image_format = slides.export.SlideImageFormat.svg(svgOptions)

        pres.save(htmlDocumentFileName, slides.export.SaveFormat.HTML, htmlOptions)
    #ExEnd:ConvertWholePresentationToHTMLWithMediaFiles