import aspose.slides as slides


#ExStart:RemoveNodeSpecificPosition
# The path to the documents directory.
dataDir = "./examples/data/"
outDir = "./examples/out/"

# Load the desired the presentation             
with slides.Presentation(dataDir + "smart_art_access.pptx") as pres:
    # Traverse through every shape inside first slide
    for shape in pres.slides[0].shapes:
        # Check if shape is of SmartArt type
        if type(shape) is slides.smartart.SmartArt:
            # Typecast shape to SmartArt
            if len(shape.all_nodes) > 0:
                # Accessing SmartArt node at index 0
                node = shape.all_nodes[0]

                if len(node.child_nodes) >= 2:
                    # Removing the child node at position 1
                    node.child_nodes.remove_node(1)

    # Save Presentation
    pres.save(outDir + "smart_art_remove_node_pos_out.pptx", slides.export.SaveFormat.PPTX)
#ExEnd:RemoveNodeSpecificPosition