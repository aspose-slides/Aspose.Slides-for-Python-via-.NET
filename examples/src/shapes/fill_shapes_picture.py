import aspose.slides as slides


def fill_shapes_picture(global_opts):
    # Instantiate Presentation class that represents the PPTX
    with slides.Presentation() as pres:
        # Get the first slide
        slide = pres.slides[0]

        # Add autoshape of rectangle type
        shape = slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 150, 75, 150)

        # Set the fill type to Picture
        shape.fill_format.fill_type = slides.FillType.PICTURE

        # Set the picture fill mode
        shape.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.TILE

        # Set the picture
        img = slides.Images.from_file(global_opts.data_dir + "image2.jpg")
        imgx = pres.images.add_image(img)
        shape.fill_format.picture_fill_format.picture.image = imgx

        # Write the PPTX file to disk
        pres.save(global_opts.out_dir + "shapes_filltype_picture_out.pptx", slides.export.SaveFormat.PPTX)
