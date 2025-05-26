import aspose.slides as slides


def picture_frame_is_cameo_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "PresCameo.pptx") as pres:
        # Check if first picture frame is Cameo
        shape = pres.slides[0].shapes[0]
        if type(shape) is slides.PictureFrame:
            print("First picture is Cameo:", shape.is_cameo)

        # Check if third picture frame is Cameo
        shape = pres.slides[0].shapes[2]
        if type(shape) is slides.PictureFrame:
            print("Third picture is Cameo:", shape.is_cameo)
