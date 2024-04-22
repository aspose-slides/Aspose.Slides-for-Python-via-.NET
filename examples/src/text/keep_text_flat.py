import aspose.slides as slides


def keep_text_flat(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_keep_text_flat.pptx") as pres:
        shape1 = pres.slides[0].shapes[0]
        shape2 = pres.slides[0].shapes[1]

        shape1.text_frame.text_frame_format.keep_text_flat = False
        shape2.text_frame.text_frame_format.keep_text_flat = True

        pres.slides[0].get_image(4 / 3, 4 / 3).save(global_opts.out_dir + "text_keep_text_flat_out.png", slides.ImageFormat.PNG)
