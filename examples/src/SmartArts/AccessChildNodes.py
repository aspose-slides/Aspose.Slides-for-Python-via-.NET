import aspose.slides as slides
            
#ExStart:AccessChildNodes
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

with slides.Presentation(dataDir + "smart_art_access_child_nodes.pptx") as pres:
    # Traverse through every shape inside first slide
    for shape in pres.slides[0].shapes:
        # Check if shape is of SmartArt type
        if type(shape) is slides.smartart.SmartArt:
            # Traverse through all nodes inside SmartArt
            for node0 in shape.all_nodes:
                # Traversing through the child nodes in SmartArt node at index i
                for node in node0.child_nodes:
                    # Printing the SmartArt child node parameters
                    outString = "Text = {0},  Level = {1}, Position = {2}".format(node.text_frame.text, node.level, node.position)
                    print(outString)
#ExEnd:AccessChildNodes