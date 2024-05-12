import aspose.slides as slides


def add_relative_scale_height_picture_frame(global_opts):
    # Instantiate presentation object
    with slides.Presentation() as presentation:
        # Load Image to be added in presentation image collection
        img = slides.Images.from_file(global_opts.data_dir + "image1.jpg")
        image = presentation.images.add_image(img)

        # Add picture frame to slide
        pf = presentation.slides[0].shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 50, 50, 100, 100, image)

        # Setting relative scale width and height
        pf.relative_scale_height = 0.8
        pf.relative_scale_width = 1.35

        # Save presentation
        presentation.save(global_opts.out_dir + "shapes_add_relative_scale_height_picture_frame_out.pptx",
                          slides.export.SaveFormat.PPTX)
