import aspose.slides as slides


def access_smart_art(global_opts):
    # Load the desired the presentation
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as pres:
        # Traverse through every shape inside first slide
        for shape in pres.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Typecast shape to SmartArt
                smart = shape

                # Traverse through all nodes inside SmartArt
                for node in smart.all_nodes:
                    # Printing the SmartArt node parameters
                    print("Text = {0}, Level = {1}, Position = {2}".format(node.text_frame.text, node.level,
                                                                           node.position))
