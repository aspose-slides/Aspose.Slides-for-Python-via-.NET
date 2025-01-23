import aspose.slides as slides


def convert_svg_to_emf(global_opts):
    # Creates the new SVG image
    with open(global_opts.data_dir + "content.svg", "rb") as f1, open(global_opts.out_dir + "SvgAsEmf.emf", "wb") as f2:
        svg_image = slides.SvgImage(f1)
        svg_image.write_as_emf(f2)
