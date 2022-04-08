import aspose.slides as slides


#ExStart:ImportingHTMLText
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Create Empty presentation instance# Create Empty presentation instance
with slides.Presentation() as pres:
    # Acesss the default first slide of presentation
    slide = pres.slides[0]

    # Adding the AutoShape to accomodate the HTML content
    ashape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 10, 10, pres.slide_size.size.width - 20, pres.slide_size.size.height - 10)

    ashape.fill_format.fill_type = slides.FillType.NO_FILL

    # Adding text frame to the shape
    ashape.add_text_frame("")

    # Clearing all paragraphs in added text frame
    ashape.text_frame.paragraphs.clear()

    # Loading the HTML file using stream reader
    with open(dataDir + "file.html", "rt") as stream:
        data = stream.read()

    # Adding text from HTML stream reader in text frame
    ashape.text_frame.paragraphs.add_from_html(data)

    # Saving Presentation
    pres.save(outDir + "text_import_from_html_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ImportingHTMLText