from .add_layout_slides import add_layout_slides
from .check_slides_comparison import check_slides_comparison
from .get_base_placeholder_example import get_base_placeholder_example
from .header_footer_manager_example import header_footer_manager_example
from .layout_placeholder_manager_example import layout_placeholder_manager_example
from .manage_header_footer_text import manage_header_footer_text
from .set_child_footer import set_child_footer
from .set_pdf_page_size import set_pdf_page_size
from .set_size_and_type import set_size_and_type
from .set_slide_size_scale import set_slide_size_scale


def run_slides_layout_examples(global_opts):
    add_layout_slides(global_opts)
    check_slides_comparison(global_opts)
    get_base_placeholder_example(global_opts)
    header_footer_manager_example(global_opts)
    layout_placeholder_manager_example(global_opts)
    manage_header_footer_text(global_opts)
    set_child_footer(global_opts)
    set_pdf_page_size(global_opts)
    set_size_and_type(global_opts)
    set_slide_size_scale(global_opts)
