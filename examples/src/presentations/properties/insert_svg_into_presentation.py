import aspose.slides as slides


def insert_svg(global_opts):
    with slides.Presentation() as p:
        with open(global_opts.data_dir + "image3.svg", "rb") as file:
            svg_content = file.read()

        svg_image = slides.SvgImage(svg_content)
        pp_image = p.images.add_image(svg_image)
        p.slides[0].shapes.add_picture_frame(slides.ShapeType.RECTANGLE, 0, 0, pp_image.width, pp_image.height, pp_image)
        p.save(global_opts.out_dir + "insert_svg_out.pptx", slides.export.SaveFormat.PPTX)
