import aspose.slides as slides


def save_convert_svg_to_group_of_shapes(global_opts):
    with slides.Presentation(global_opts.data_dir + "save_convert_svg_to_group_of_shapes.pptx") as pres:
        picture_frame = pres.slides[0].shapes[0]
        svg_image = picture_frame.picture_format.picture.image.svg_image
        if svg_image is not None:
            # Convert svg image into group of shapes
            group_shape = pres.slides[0].shapes.add_group_shape(svg_image, picture_frame.frame.x, picture_frame.frame.y, picture_frame.frame.width, picture_frame.frame.height)
            # remove source svg image from presentation
            pres.slides[0].shapes.remove(picture_frame)

        pres.save(global_opts.out_dir + "save_convert_svg_to_group_of_shapes_out.pptx", slides.export.SaveFormat.PPTX)
