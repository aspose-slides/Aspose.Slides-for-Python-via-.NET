import aspose.slides as slides


def set_image_as_background(global_opts):
    # Instantiate the Presentation class that represents the presentation file
    with slides.Presentation() as pres:
        # Set the background with Image
        pres.slides[0].background.type = slides.BackgroundType.OWN_BACKGROUND
        pres.slides[0].background.fill_format.fill_type = slides.FillType.PICTURE
        pres.slides[0].background.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH

        # Set the picture
        img = slides.Images.from_file(global_opts.data_dir + "image1.jpg")

        # Add image to presentation's images collection
        imgx = pres.images.add_image(img)

        pres.slides[0].background.fill_format.picture_fill_format.picture.image = imgx

        # Write the presentation to disk
        pres.save(global_opts.out_dir + "background_picture_fill_format_out.pptx", slides.export.SaveFormat.PPTX)
