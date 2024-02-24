import aspose.slides as slides


def save_add_blob_image(global_opts):
    # create a new presentation which will contain this image
    with slides.Presentation() as pres, open(global_opts.data_dir + "large_image.jpg", "br") as file_stream:
        # let's add the image to the presentation - we choose KeepLocked behavior, because we not
        # have an intent to access the "large_image.jpg" file.
        img = pres.images.add_image(file_stream, slides.LoadingStreamBehavior.KEEP_LOCKED)
        pres.slides[0].shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 0, 0, 300, 200, img)

        # save the presentation. Despite that the output presentation will be
        # large, the memory consumption will be low the whole lifetime of the pres object
        pres.save(global_opts.out_dir + "save_add_blob_image_out.pptx", slides.export.SaveFormat.PPTX)
