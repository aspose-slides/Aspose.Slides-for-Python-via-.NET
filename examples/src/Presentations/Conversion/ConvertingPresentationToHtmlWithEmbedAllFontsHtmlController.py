import aspose.slides as slides


def convert_to_html_with_embed_all_fonts():
    #ExStart:ConvertingPresentationToHtmlWithEmbedAllFontsHtmlController
    dataDir = "./examples/data/"
    outDir = "./examples/out/"
    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as pres:
        # exclude default presentation fonts
        fontNameExcludeList = []

        para = slides.Paragraph()

        embedFontsController = slides.export.EmbedAllFontsHtmlController(fontNameExcludeList)

        htmlOptionsEmbed = slides.export.HtmlOptions()
        htmlOptionsEmbed.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(embedFontsController)

        pres.save(outDir + "convert_to_html_with_embed_all_fonts_out.html", slides.export.SaveFormat.HTML, htmlOptionsEmbed)
    #ExEnd:ConvertingPresentationToHtmlWithEmbedAllFontsHtmlController