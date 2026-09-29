from .convert_to_image import convert_to_image
from .convert_to_svg_example import convert_to_svg_example
from .for_each_example import for_each_example
from .merger_example import merger_example

def run_presentation_lowcode_examples(global_opts):
    convert_to_image(global_opts)
    convert_to_svg_example(global_opts)
    for_each_example(global_opts)
    merger_example(global_opts)
