from .add_image_inside_table_cell import add_image_inside_table_cell
from .add_image_inside_table_cell_and_crop import add_image_inside_table_cell_and_crop
from .cell_split import cell_split
from .cloning_in_table import cloning_in_table
from .create_table import create_table
from .create_table_from_scratch_in_slide import create_table_from_scratch_in_slide
from .get_effective_values_of_table import get_effective_values_of_table
from .identifying_the_merged_cells_in_table import identifying_the_merged_cells_in_table
from .lock_aspect_ratio import lock_aspect_ratio
from .merge_cell import merge_cell
from .removing_row_column import removing_row_column
from .resize_slide_with_table import resize_slide_with_table
from .set_first_row_as_header import set_first_row_as_header
from .set_text_formatting_inside_table import set_text_formatting_inside_table
from .standard_tables import standard_tables
from .table_from_scratch import table_from_scratch
from .table_transparency import table_transparency
from .table_with_cell_borders import table_with_cell_borders
from .text_formatting_inside_table_column import text_formatting_inside_table_column
from .text_formatting_inside_table_row import text_formatting_inside_table_row
from .vertically_align_text import vertically_align_text


def run_tables_examples(global_opts):
    add_image_inside_table_cell(global_opts)
    add_image_inside_table_cell_and_crop(global_opts)
    cell_split(global_opts)
    cloning_in_table(global_opts)
    create_table(global_opts)
    create_table_from_scratch_in_slide(global_opts)
    get_effective_values_of_table(global_opts)
    identifying_the_merged_cells_in_table(global_opts)
    lock_aspect_ratio(global_opts)
    merge_cell(global_opts)
    removing_row_column(global_opts)
    resize_slide_with_table(global_opts)
    set_first_row_as_header(global_opts)
    set_text_formatting_inside_table(global_opts)
    standard_tables(global_opts)
    table_from_scratch(global_opts)
    table_transparency(global_opts)
    table_with_cell_borders(global_opts)
    text_formatting_inside_table_column(global_opts)
    text_formatting_inside_table_row(global_opts)
    vertically_align_text(global_opts)
