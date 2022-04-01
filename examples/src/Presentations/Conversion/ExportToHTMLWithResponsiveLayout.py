import aspose.slides as slides

def convert_to_html_with_responsive_layout():
    #ExStart:ExportToHTMLWithResponsiveLayout
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"

    with slides.Presentation(dataDir + "welcome-to-powerpoint.pptx") as presentation:
        saveOptions = slides.export.HtmlOptions()
        saveOptions.svg_responsive_layout = True
        presentation.save(outDir+"convert_to_html_with_responsive_layout_out.html", slides.export.SaveFormat.HTML, saveOptions)
    #ExEnd:ExportToHTMLWithResponsiveLayout
