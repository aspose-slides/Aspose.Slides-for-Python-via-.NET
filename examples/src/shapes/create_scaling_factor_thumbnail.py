import aspose.slides as slides


def create_scaling_factor_thumbnail(global_opts):
    # Instantiate a Presentation class that represents the presentation file
    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Create a full scale image
        with pres.slides[0].shapes[0].get_image(slides.ShapeThumbnailBounds.SHAPE, 2, 2) as image:
            # Save the image to disk in PNG format
            image.save(global_opts.out_dir + "shapes_create_scaling_thumbnail_out.png",
                        slides.ImageFormat.PNG)
