from .default_printer_printing import printing_default_settings
from .print_preview import printing_preview
from .render_comments import rendering_comments
from .render_options import rendering_options
from .rendering_3d import rendering_3d
from .rendering_emoji import rendering_emoji
from .set_slide_number import rendering_set_slide_number
from .set_zoom import rendering_set_zoom


def run_rendering_printing_examples(global_opts):
    # Commented because of access to printer
    # printing_default_settings(global_opts)
    # printing_preview()
    rendering_comments(global_opts)
    rendering_options(global_opts)
    rendering_3d(global_opts)
    rendering_emoji(global_opts)
    rendering_set_slide_number(global_opts)
    rendering_set_zoom(global_opts)
