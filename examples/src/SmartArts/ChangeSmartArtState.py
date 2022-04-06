import aspose.slides as slides


#ExStart:ChangeSmartArtState
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Add SmartArt BasicProcess 
    smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.BASIC_PROCESS)

    # Get or Set the state of SmartArt Diagram
    smart.is_reversed = True
    flag = smart.is_reversed

    # Saving Presentation
    presentation.save(outDir + "smart_art_change_state_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangeSmartArtState
