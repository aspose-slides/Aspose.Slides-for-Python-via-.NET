from .convert_to_image import convert_to_image
from .merger_example import merger_example

def run_presentation_lowcode_examples(global_opts):
    convert_to_image(global_opts)
    merger_example(global_opts)
