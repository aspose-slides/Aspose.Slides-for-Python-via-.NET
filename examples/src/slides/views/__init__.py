from .gradient_style_rendering import gradient_style_rendering
from .manage_presentation_normal_view_state import manage_presentation_normal_view_state


def run_slides_views_examples(global_opts):
    gradient_style_rendering(global_opts)
    manage_presentation_normal_view_state(global_opts)
