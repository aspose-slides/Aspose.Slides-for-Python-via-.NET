import aspose.slides as slides


def change_smart_art_layout(global_opts):
    with slides.Presentation() as presentation:
        # Add SmartArt BasicProcess
        smart = presentation.slides[0].shapes.add_smart_art(10, 10, 400, 300,
                                                            slides.smartart.SmartArtLayoutType.BASIC_BLOCK_LIST)

        # Change LayoutType to BasicProcess
        smart.layout = slides.smartart.SmartArtLayoutType.BASIC_PROCESS

        # Saving Presentation
        presentation.save(global_opts.out_dir + "smart_art_change_layout_out.pptx", slides.export.SaveFormat.PPTX)
