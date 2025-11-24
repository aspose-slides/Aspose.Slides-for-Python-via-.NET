from .after_animation_type_example import after_animation_type_example
from .animation_duration_slide import animation_duration_slide
from .animation_faded_zoom_subtype import animation_faded_zoom_subtype
from .animation_rewind import animation_rewind
from .better_slide_transitions import better_slide_transitions
from .manage_simple_slide_transitions import manage_simple_slide_transitions
from .managing_better_slide_transitions import managing_better_slide_transitions
from .set_transition_effects import set_transition_effects
from .set_transition_morph_type import set_transition_morph_type
from .simple_slide_transitions import simple_slide_transitions
from .support_of_morph_transition import support_of_morph_transition


def run_slides_transition_examples(global_opts):
    after_animation_type_example(global_opts)
    animation_duration_slide(global_opts)
    animation_faded_zoom_subtype(global_opts)
    animation_rewind(global_opts)
    better_slide_transitions(global_opts)
    manage_simple_slide_transitions(global_opts)
    managing_better_slide_transitions(global_opts)
    set_transition_effects(global_opts)
    set_transition_morph_type(global_opts)
    simple_slide_transitions(global_opts)
    support_of_morph_transition(global_opts)
