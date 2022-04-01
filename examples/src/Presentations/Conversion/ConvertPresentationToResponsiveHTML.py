import aspose.slides as slides

def convert_to_responsive_html():
    #ExStart:ConvertPresentationToResponsiveHTML
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    # Instantiate a Presentation object that represents a presentation file
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        controller = slides.export.ResponsiveHtmlController()
        htmlOptions = slides.export.HtmlOptions()
        htmlOptions.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(controller)

        # Saving the presentation to HTML
        presentation.save(outDir + "convert_to_responsive_html_out.html", slides.export.SaveFormat.HTML, htmlOptions)
    #ExEnd:ConvertPresentationToResponsiveHTML
