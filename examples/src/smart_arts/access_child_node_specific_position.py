import aspose.slides as slides


def access_child_node_specific_position():
    # Instantiate the presentation
    with slides.Presentation() as pres:
        # Accessing the first slide
        slide = pres.slides[0]

        # Adding the SmartArt shape in first slide
        smart = slide.shapes.add_smart_art(0, 0, 400, 400, slides.smartart.SmartArtLayoutType.STACKED_LIST)

        # Accessing the SmartArt node at index 0
        node = smart.all_nodes[0]

        # Accessing the child node at position 1 in parent node
        position = 1
        child_node = node.child_nodes[position]

        # Printing the SmartArt child node parameters
        print("j = {0}, Text = {1}, Level = {2}, Position = {3}".format(position, child_node.text_frame.text,
                                                                        child_node.level, child_node.position))
