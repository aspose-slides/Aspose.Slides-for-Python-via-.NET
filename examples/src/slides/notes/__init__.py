from .header_and_footer_in_notes_slide import header_and_footer_in_notes_slide
from .remove_notes_at_specific_slide import remove_notes_at_specific_slide


def run_slides_notes_examples(global_opts):
    header_and_footer_in_notes_slide(global_opts)
    remove_notes_at_specific_slide(global_opts)
