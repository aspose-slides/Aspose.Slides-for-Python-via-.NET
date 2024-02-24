from .access_slide_comments import access_slide_comments
from .add_parent_comments import add_parent_comments
from .add_slide_comments import add_slide_comments
from .modern_comments import modern_comments


def run_slides_comments_examples(global_opts):
    access_slide_comments(global_opts)
    add_parent_comments(global_opts)
    add_slide_comments(global_opts)
    modern_comments(global_opts)
