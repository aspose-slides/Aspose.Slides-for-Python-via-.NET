from .thumbnail_from_slide import thumbnail_from_slide
from .thumbnail_from_slide_in_notes import thumbnail_from_slide_in_notes
from .thumbnail_with_user_defined_dimensions import thumbnail_with_user_defined_dimensions


def run_slides_thumbnail_examples(global_opts):
    thumbnail_from_slide(global_opts)
    thumbnail_from_slide_in_notes(global_opts)
    thumbnail_with_user_defined_dimensions(global_opts)
