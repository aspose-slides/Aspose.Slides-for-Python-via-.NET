import aspose.slides as slides


def check_slides_comparison(global_opts):
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as presentation1:
        with slides.Presentation(global_opts.data_dir + "background.pptx") as presentation2:
            for i in range(len(presentation1.masters)):
                for j in range(len(presentation2.masters)):
                    if presentation1.masters[i] == presentation2.masters[j]:
                        text = "SomePresentation1 MasterSlide#{0} is equal to SomePresentation2 MasterSlide#{1}".format(
                            i, j)
                        print(text)
