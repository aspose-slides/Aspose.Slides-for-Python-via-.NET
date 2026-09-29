import os
import aspose.slides as slides


def convert_to_svg_example(global_opts):
    svg_dir = os.path.join(global_opts.out_dir, "convert_to_svg")
    os.makedirs(svg_dir, exist_ok=True)

    # The callback returns the output path for each slide
    def get_out_path(slide, index):
        return os.path.join(svg_dir, "slide_{0}.svg".format(index + 1))

    with slides.Presentation(global_opts.data_dir + "ConvertExample.pptx") as pres:
        slides.lowcode.Convert.to_svg(pres, get_out_path)
