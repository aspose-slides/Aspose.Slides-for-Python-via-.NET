import aspose.slides as slides


#ExStart:CreateSmartArtShape
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Instantiate the presentation
with slides.Presentation() as pres:
    # Access the presentation slide
    slide = pres.slides[0]

    # Add Smart Art Shape
    smart = slide.shapes.add_smart_art(0, 0, 400, 400, slides.smartart.SmartArtLayoutType.BASIC_BLOCK_LIST)

    # Saving presentation
    pres.save(outDir + "smart_art_add_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CreateSmartArtShape