import aspose.slides as slides


def change_text_on_smart_art_node(global_opts):
    with slides.Presentation() as presentation:
        # Add SmartArt BasicProcess
        smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.BASIC_CYCLE)

        # Obtain the reference of a node by using its Index
        # select second root node
        node = smart.nodes[1]

        # Setting the text of the TextFrame
        node.text_frame.text = "Second root node"

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_change_frame_text_out.pptx", slides.export.SaveFormat.PPTX)
