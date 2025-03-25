from .render_options import rendering_options
from .rendering_3d import rendering_3d
from .rendering_emoji import rendering_emoji
from .set_slide_number import rendering_set_slide_number
from .set_zoom import rendering_set_zoom


def run_rendering_printing_examples(global_opts):
    print("===== Rendering & Printing examples =====")
    rendering_options(global_opts)
    rendering_3d(global_opts)
    #rendering_emoji(global_opts)
    rendering_set_slide_number(global_opts)
    rendering_set_zoom(global_opts)
