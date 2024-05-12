import aspose.slides as slides


def thumbnail_from_slide(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Access the first slide
        slide = pres.slides[0]

        # Create a full scale image
        bmp = slide.get_image(1, 1)

        # Save the image to disk in JPEG format
        bmp.save(global_opts.out_dir + "thumbnail_from_slide_out.jpg", slides.ImageFormat.JPEG)
