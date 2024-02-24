import aspose.slides as slides


def remove_node_example(global_opts):
    # Load the desired the presentation
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as pres:
        # Traverse through every shape inside first slide
        for shape in pres.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Typecast shape to SmartArt
                if len(shape.all_nodes) > 0:
                    # Accessing SmartArt node at index 0
                    node = shape.all_nodes[0]

                    # Removing the selected node
                    shape.all_nodes.remove_node(node)

        # Save Presentation
        pres.save(global_opts.out_dir + "smart_art_remove_node_out.pptx", slides.export.SaveFormat.PPTX)
