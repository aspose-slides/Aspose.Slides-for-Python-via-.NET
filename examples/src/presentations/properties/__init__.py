from .access_builtin_properties import props_access_builtin_properties
from .access_layout_formats import props_access_layout_formats
from .access_modifying_properties import props_access_modifying_properties
from .access_properties import props_access_properties
from .add_blob_to_presentation import props_add_blob_to_presentation
from .add_custom_document_properties import props_add_custom_document_properties
from .check_password_example import props_check_password
from .check_presentation_protection import props_check_presentation_protection
from .extended_presentation_properties import extended_presentation_properties
from .grid_properties import grid_properties
from .guides_properties import guides_properties
from .insert_svg_into_presentation import insert_svg
from .modify_builtin_properties import props_modify_builtin_properties
from .read_only_recommended import props_read_only_recommended
from .update_presentation_properties import props_update_presentation_properties
from .update_presentation_properties_using_new_template import props_update_properties_using_template


def run_presentation_properties_examples(global_opts):
    print("======= Presentation Properties =======")
    props_access_builtin_properties(global_opts)
    props_access_layout_formats(global_opts)
    props_access_modifying_properties(global_opts)
    props_access_properties()
    props_add_blob_to_presentation(global_opts)
    props_add_custom_document_properties(global_opts)
    props_check_password(global_opts)
    props_check_presentation_protection(global_opts)
    extended_presentation_properties(global_opts)
    grid_properties(global_opts)
    guides_properties(global_opts)
    insert_svg(global_opts)
    props_modify_builtin_properties(global_opts)
    props_read_only_recommended(global_opts)
    props_update_presentation_properties(global_opts)
    props_update_properties_using_template(global_opts)
