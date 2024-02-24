import aspose.slides as slides


def check_smart_art_hidden_property(global_opts):
    with slides.Presentation() as presentation:
        # Add SmartArt BasicProcess
        smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300, slides.smartart.SmartArtLayoutType.RADIAL_CYCLE)

        # Add node on SmartArt
        node = smart.all_nodes.add_node()

        # Check isHidden property
        print("is_hidden: " + str(node.is_hidden))

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_check_hidden_out.pptx", slides.export.SaveFormat.PPTX)
