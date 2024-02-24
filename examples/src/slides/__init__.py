from .background import *
from .comments import *
from .crud import *
from .hyperlinks import *
from .layout import *
from .media import *
from .notes import *
from .thumbnail import *
from .transitions import *
from .views import *


def run_slides_examples(global_opts):
    run_slides_background_examples(global_opts)
    run_slides_comments_examples(global_opts)
    run_slides_crud_examples(global_opts)
    run_slides_hyperlinks_examples(global_opts)
    run_slides_layout_examples(global_opts)
    run_slides_media_examples(global_opts)
    run_slides_notes_examples(global_opts)
