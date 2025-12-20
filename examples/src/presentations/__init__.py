from .conversion import *
from .lowcode import *
from .opening import *
from .properties import *
from .saving import *


def run_presentation_examples(global_opts):
    print("===== Presentation examples =====")
    run_presentation_conversion_examples(global_opts)
    run_presentation_lowcode_examples(global_opts)
    run_presentation_opening_examples(global_opts)
    run_presentation_properties_examples(global_opts)
    run_presentation_saving_examples(global_opts)
