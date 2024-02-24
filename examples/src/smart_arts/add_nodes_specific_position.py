import aspose.slides as slides
            
            
def add_nodes_specific_position(global_opts):
    # Creating a presentation instance
    with slides.Presentation() as pres:
        # Access the presentation slide
        slide = pres.slides[0]

        # Add Smart Art IShape
        smart = slide.shapes.add_smart_art(0, 0, 400, 400, slides.smartart.SmartArtLayoutType.STACKED_LIST)

        # Accessing the SmartArt node at index 0
        node = smart.all_nodes[0]

        # Adding new child node at position 2 in parent node
        child_node = node.child_nodes.add_node_by_position(2)

        # Add Text
        child_node.text_frame.text = "Sample Text Added"

        # Save Presentation
        pres.save(global_opts.out_dir + "smart_art_add_node_by_position_out.pptx", slides.export.SaveFormat.PPTX)
