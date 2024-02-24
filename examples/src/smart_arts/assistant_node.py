import aspose.slides as slides


def assistant_node(global_opts):
    # Creating a presentation instance
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as pres:
        # Traverse through every shape inside first slide
        for shape in pres.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Traversing through all nodes of SmartArt shape
                for node in shape.all_nodes:
                    tc = node.text_frame.text
                    # Check if node is Assitant node
                    if node.is_assistant:
                        # Setting Assitant node to False and making it normal node
                        node.is_assistant = False

        # Save Presentation
        pres.save(global_opts.out_dir + "smart_art_change_assitant_out.pptx", slides.export.SaveFormat.PPTX)
