import aspose.slides as slides


#ExStart:CheckSmartArtHiddenProperty
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation() as presentation:
    # Add SmartArt BasicProcess 
    smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.RADIAL_CYCLE)

    # Add node on SmartArt 
    node = smart.all_nodes.add_node()

    # Check isHidden property
    print (str(node.is_hidden))

    # Saving Presentation
    presentation.save(dataDir + "smart_art_check_hidden_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:CheckSmartArtHiddenProperty
