import aspose.slides as slides

# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

def convert_to_handout():
    with slides.Presentation(dataDir + "HandoutExample.pptx") as pres:
        # Set convertion options
        options = slides.export.PdfOptions()
        options.show_hidden_slides = True
        slides_layout_options = slides.export.HandoutLayoutingOptions()
        slides_layout_options.handout = slides.export.HandoutType.HANDOUTS_4_HORIZONTAL
        options.slides_layout_options = slides_layout_options
        
        # Save result
        pres.save(outDir + "HandoutExample.pdf", slides.export.SaveFormat.PDF, options)
