from .add_blob_image_to_presentation import save_add_blob_image
from .convert_svg_image_object_info_group_of_shapes import save_convert_svg_to_group_of_shapes
from .image_quality_example import image_quality_example
from .java_script_link_example import java_script_link_example
from .refresh_thumbnail_presentation import refresh_thumbnail_presentation
from .remove_write_protection import save_remove_write_protection
from .save_as_predefined_view_type import save_as_predefined_view_type
from .save_as_read_only import save_as_read_only
from .save_properties import save_properties
from .save_to_file import save_to_file
from .save_to_stream import save_to_stream
from .save_with_password import save_with_password
from .support_of_digital_signature import save_add_digital_signature
from .to_save_format_example import to_save_format_example


def run_presentation_saving_examples(global_opts):
    print("======= Presentation Saving =======")
    save_add_blob_image(global_opts)
    save_convert_svg_to_group_of_shapes(global_opts)
    image_quality_example(global_opts)
    java_script_link_example(global_opts)
    refresh_thumbnail_presentation(global_opts)
    save_remove_write_protection(global_opts)
    save_as_predefined_view_type(global_opts)
    save_as_read_only(global_opts)
    save_properties(global_opts)
    save_to_file(global_opts)
    save_to_stream(global_opts)
    save_with_password(global_opts)
    save_add_digital_signature(global_opts)
    to_save_format_example(global_opts)
