import aspose.slides as slides

#ExStart:ChangeSmartArtLayout
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Add SmartArt BasicProcess 
    smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.BASIC_BLOCK_LIST)

    # Change LayoutType to BasicProcess
    smart.layout = slides.smartart.SmartArtLayoutType.BASIC_PROCESS

    # Saving Presentation
    presentation.save(outDir + "smart_art_change_layout_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangeSmartArtLayout
