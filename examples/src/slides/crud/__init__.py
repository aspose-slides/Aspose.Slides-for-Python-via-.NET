from .access_slide_by_id import access_slide_by_id
from .access_slide_by_index import access_slide_by_index
from .access_slides import access_slides
from .add_notes_slide_with_notes_style import add_notes_slide_with_notes_style
from .add_slides import add_slides
from .change_position import change_position
from .clone_another_presentation_at_specified_position import clone_another_presentation_at_specified_position
from .clone_at_end_of_another import clone_at_end_of_another
from .clone_slide_into_specified_section import clone_slide_into_specified_section
from .clone_to_another_presentation_with_master import clone_to_another_presentation_with_master
from .clone_within_same_presentation_to_end import clone_within_same_presentation_to_end
from .clone_within_same_presentation import clone_within_same_presentation
from .create_slides_svg_image import create_slides_svg_image
from .remove_slide_using_index import remove_slide_using_index
from .remove_slide_using_reference import remove_slides_using_reference
from .section_collection import section_collection


def run_slides_crud_examples(global_opts):
    access_slide_by_id(global_opts)
    access_slide_by_index(global_opts)
    access_slides(global_opts)
    add_notes_slide_with_notes_style(global_opts)
    add_slides(global_opts)
    change_position(global_opts)
    clone_another_presentation_at_specified_position(global_opts)
    clone_at_end_of_another(global_opts)
    clone_slide_into_specified_section(global_opts)
    clone_to_another_presentation_with_master(global_opts)
    clone_within_same_presentation_to_end(global_opts)
    clone_within_same_presentation(global_opts)
    create_slides_svg_image(global_opts)
    remove_slide_using_index(global_opts)
    remove_slides_using_reference(global_opts)
    section_collection(global_opts)
