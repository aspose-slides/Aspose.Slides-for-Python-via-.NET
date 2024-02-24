import aspose.slides as slides


def access_smart_art_particular_layout(global_opts):
    with slides.Presentation(global_opts.data_dir + "smart_art_access_shape.pptx") as presentation:
        # Traverse through every shape inside first slide
        for shape in presentation.slides[0].shapes:
            # Check if shape is of SmartArt type
            if type(shape) is slides.smartart.SmartArt:
                # Typecast shape to SmartArt
                if shape.layout == slides.smartart.SmartArtLayoutType.BASIC_BLOCK_LIST:
                    print("Do some thing here....")
