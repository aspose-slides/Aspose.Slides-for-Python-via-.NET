import aspose.slides as slides


def tile_picture_fill_format_example(global_opts):
    with slides.Presentation() as pres:
        first_slide = pres.slides[0]

        with slides.Images.from_file(global_opts.data_dir + "Image.png") as new_image:
            pp_image = pres.images.add_image(new_image)

        # Adds the new Rectangle shape
        new_shape = first_slide.shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 0, 0, 350, 350)

        # Sets the fill type of the new shape to Picture
        new_shape.fill_format.fill_type = slides.FillType.PICTURE

        # Sets the shape's fill image
        picture_fill_format = new_shape.fill_format.picture_fill_format
        picture_fill_format.picture.image = pp_image

        # Sets the picture fill mode to Tile and changes the properties
        picture_fill_format.picture_fill_mode = slides.PictureFillMode.TILE
        picture_fill_format.tile_offset_x = -275
        picture_fill_format.tile_offset_y = -247
        picture_fill_format.tile_scale_x = 120
        picture_fill_format.tile_scale_y = 120
        picture_fill_format.tile_alignment = slides.RectangleAlignment.BOTTOM_RIGHT
        picture_fill_format.tile_flip = slides.TileFlip.FLIP_BOTH

        pres.save(global_opts.out_dir + "ImageTileExample.pptx", slides.export.SaveFormat.PPTX)
