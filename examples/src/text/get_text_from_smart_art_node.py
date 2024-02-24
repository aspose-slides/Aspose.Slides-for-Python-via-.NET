import aspose.slides as slides


def get_text_from_smart_art_node(global_opts):
    with slides.Presentation(global_opts.data_dir + "smart_art_access.pptx") as presentation:
        slide = presentation.slides[0]
        smart_art = slide.shapes[0]

        smart_art_nodes = smart_art.all_nodes
        for smart_art_node in smart_art_nodes:
            for node_shape in smart_art_node.shapes:
                if node_shape.text_frame is not None:
                    print(node_shape.text_frame.text)
