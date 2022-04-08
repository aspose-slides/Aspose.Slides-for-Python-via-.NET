import aspose.slides as slides


#ExStart:ChangeTextOnSmartArtNode
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:

    # Add SmartArt BasicProcess 
    smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.BASIC_CYCLE)

    # Obtain the reference of a node by using its Index  
    node = smart.nodes[1] # select second root node

    # Setting the text of the TextFrame 
    node.text_frame.text = "Second root node"

    # Saving Presentation
    presentation.save(outDir + "smart_art_change_frame_text_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:ChangeTextOnSmartArtNode
