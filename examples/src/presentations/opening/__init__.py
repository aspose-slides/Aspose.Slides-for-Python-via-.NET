from .get_file_format import get_file_format
from .get_position_coordinates_of_portion import get_position_coordinates_of_portion
from .get_rectangular_coordinates_of_paragraph import get_rectangular_coordinates_of_paragraph
from .load_format_enumeration import load_format_enumeration
from .open_password_presentation import open_password_presentation
from .open_presentation import open_presentation
from .open_very_large_presentation import open_very_large_presentation
from .set_access_permissions_to_pdf import open_set_access_permissions_to_pdf


def run_presentation_opening_examples(global_opts):
    get_file_format(global_opts)
    get_position_coordinates_of_portion(global_opts)
    get_rectangular_coordinates_of_paragraph(global_opts)
    load_format_enumeration(global_opts)
    open_password_presentation(global_opts)
    open_presentation(global_opts)
    open_very_large_presentation(global_opts)
    open_set_access_permissions_to_pdf(global_opts)
