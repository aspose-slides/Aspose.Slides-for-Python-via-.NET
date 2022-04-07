from encodings import utf_8
import aspose.slides as slides

#ExStart:ExportingHTMLText
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load the presentation file
with slides.Presentation(dataDir + "text_export_text_frame_to_html.pptx") as pres:
    # Acesss the default first slide of presentation
    slide = pres.slides[0]

    # Desired index
    index = 0

    # Accessing the added shape
    ashape = slide.shapes[index]

    with open(outDir + "text_export_text_frame_to_html_out.html", "wt") as sw:
        data = ashape.text_frame.paragraphs.export_to_html(0, ashape.text_frame.paragraphs.count, None)
        sw.write(data)
#ExEnd:ExportingHTMLText