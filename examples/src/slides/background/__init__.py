from .get_background_effective_values import get_background_effective_values
from .set_background_to_gradient import set_background_to_gradient
from .set_image_as_background import set_image_as_background
from .set_slide_background_master import set_slide_background_master
from .set_slide_background_normal import set_slide_background_normal


def run_slides_background_examples(global_opts):
    get_background_effective_values(global_opts)
    set_background_to_gradient(global_opts)
    set_image_as_background(global_opts)
    set_slide_background_master(global_opts)
    set_slide_background_normal(global_opts)
