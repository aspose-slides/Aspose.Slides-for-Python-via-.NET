import aspose.slides as slides


def add_nodes(global_opts):
    # Load the desired the presentation# Load the desired the presentation
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as pres:
        # Traverse through every shape inside first slide
        for shape in pres.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Typecast shape to SmartArt
                smart = shape

                # Adding a new SmartArt Node
                temp_node = smart.all_nodes.add_node()

                # Adding text
                temp_node.text_frame.text = "Test"

                # Adding new child node in parent node. It  will be added in the end of collection
                new_node = temp_node.child_nodes.add_node()

                # Adding text
                new_node.text_frame.text = "New Node Added"

        # Saving Presentation
        pres.save(global_opts.out_dir + "smart_art_add_node_out.pptx", slides.export.SaveFormat.PPTX)
