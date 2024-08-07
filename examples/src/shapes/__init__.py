from .access_ole_object_frame import shapes_accessing_ole_object_frame
from .accessing_alt_text_in_group_shapes import shapes_accessing_alt_text
from .add_arrow_shaped_line import shapes_add_arrow_shaped_line
from .add_audio_frame import shapes_add_audio_frame
from .add_ole_object_frame import shapes_add_ole_object_frame
from .add_plain_line_to_slide import add_plain_line_to_slide
from .add_relative_scale_height_picture_frame import add_relative_scale_height_picture_frame
from .add_stretch_offset_for_image_fill import add_stretch_offset_for_image_fill
from .add_video_frame_from_web_source import add_video_frame_from_web_source
from .add_video_frame import add_video_frame
from .animation_target_shapes import animation_target_shapes
from .animations_on_shapes import animation_on_shapes
from .apply_3d_rotation_effect_on_shape import apply_3d_rotation_effect_on_shape
from .apply_bevel_effects import apply_bevel_effects
from .change_shape_order import change_shape_order
from .clone_shapes import clone_shapes
from .connect_shape_using_connection_site import connect_shape_using_connection_site
from .connect_shapes_using_connectors import connect_shapes_using_connectors
from .connector_line_angle import connector_line_angle
from .create_bounds_shape_thumbnail import create_bounds_shape_thumbnail
from .create_group_shape import create_group_shape
from .create_scaling_factor_thumbnail import create_scaling_factor_thumbnail
from .create_section_zoom import create_section_zoom
from .create_shape_thumbnail import create_shape_thumbnail
from .create_smart_art_child_note_thumbnail import create_smart_art_child_note_thumbnail
from .create_summary_zoom import create_summary_zoom
from .create_zoom_frame import create_zoom_frame
from .delete_picture_cropped_areas_example import delete_picture_cropped_areas_example
from .duotone_effects_pvi import duotone_effects_pvi
from .embedded_video_frame import embedded_video_frame
from .extract_embedded_file_data_from_ole_object import extract_embedded_file_data_from_ole_object
from .fill_shapes_gradient import fill_shapes_gradient
from .fill_shapes_pattern import fill_shapes_pattern
from .fill_shapes_picture import fill_shapes_picture
from .fill_shapes_with_solid_color import fill_shapes_with_solid_color
from .find_shape_in_slide import find_shape_in_slide
from .format_join_styles import format_join_styles
from .format_lines import format_lines
from .formatted_eclipse import formatted_eclipse
from .formatted_rectangle import formatted_rectangle
from .geometry_shape_add_segment import geometry_shape_add_segment
from .geometry_shape_composite_objects import geometry_shape_composite_objects
from .geometry_shape_creates_custom_geometry import geometry_shape_creates_custom_geometry
from .geometry_shape_remove_segment import geometry_shape_remove_segment
from .geometry_shape_using_shape_util import geometry_shape_using_shape_util
from .get_camera_effective_data import get_camera_effective_data
from .get_light_rig_effective_data import get_light_rig_effective_data
from .get_shape_bevel_effective_data import get_shape_bevel_effective_data
from .hiding_shapes import hiding_shapes
from .ink_management_example import ink_management_example
from .interop_shape_id import interop_shape_id
from .math_shape_get_children import math_shape_get_children
from .mathematical_shape import mathematical_shape
from .picture_frame_formatting import picture_frame_formatting
from .remove_shape import remove_shape
from .rotating_shapes import rotating_shapes_example
from .set_alternative_text import set_alternative_text
from .set_file_type_for_an_embedding_object import set_file_type_for_an_embedding_object
from .set_video_trim_from_end import set_video_trim_from_end
from .shape_is_decorative_property_example import shape_is_decorative_property_example
from .shapes_alignment import shapes_alignment
from .simple_ellipse import simple_ellipse
from .simple_rectangle import simple_rectangle
from .sketched_shapes import sketched_shapes
from .stretch_offset_left_for_picture_frame import stretch_offset_left_for_picture_frame
from .substitute_picture_title_of_ole_object_frame import substitute_picture_title_of_ole_object_frame
from .tile_picture_fill_format_example import tile_picture_fill_format_example


def run_shapes_examples(global_opts):
    shapes_accessing_ole_object_frame(global_opts)
    shapes_accessing_alt_text(global_opts)
    shapes_add_arrow_shaped_line(global_opts)
    shapes_add_audio_frame(global_opts)
    shapes_add_ole_object_frame(global_opts)
    add_plain_line_to_slide(global_opts)
    add_relative_scale_height_picture_frame(global_opts)
    add_stretch_offset_for_image_fill(global_opts)
    # Exception with HTTP error 404 on image link
    # add_video_frame_from_web_source(global_opts)
    add_video_frame(global_opts)
    animation_target_shapes(global_opts)
    animation_on_shapes(global_opts)
    apply_3d_rotation_effect_on_shape(global_opts)
    apply_bevel_effects(global_opts)
    change_shape_order(global_opts)
    clone_shapes(global_opts)
    connect_shape_using_connection_site(global_opts)
    connect_shapes_using_connectors(global_opts)
    connector_line_angle(global_opts)
    create_bounds_shape_thumbnail(global_opts)
    create_group_shape(global_opts)
    create_scaling_factor_thumbnail(global_opts)
    create_section_zoom(global_opts)
    create_shape_thumbnail(global_opts)
    create_smart_art_child_note_thumbnail(global_opts)
    create_summary_zoom(global_opts)
    create_zoom_frame(global_opts)
    delete_picture_cropped_areas_example(global_opts)
    duotone_effects_pvi(global_opts)
    embedded_video_frame(global_opts)
    extract_embedded_file_data_from_ole_object(global_opts)
    fill_shapes_gradient(global_opts)
    fill_shapes_pattern(global_opts)
    fill_shapes_picture(global_opts)
    fill_shapes_with_solid_color(global_opts)
    find_shape_in_slide(global_opts)
    format_join_styles(global_opts)
    format_lines(global_opts)
    formatted_eclipse(global_opts)
    formatted_rectangle(global_opts)
    geometry_shape_add_segment(global_opts)
    geometry_shape_composite_objects(global_opts)
    geometry_shape_creates_custom_geometry(global_opts)
    geometry_shape_remove_segment(global_opts)
    geometry_shape_using_shape_util(global_opts)
    get_camera_effective_data(global_opts)
    get_light_rig_effective_data(global_opts)
    get_shape_bevel_effective_data(global_opts)
    hiding_shapes(global_opts)
    ink_management_example(global_opts)
    interop_shape_id(global_opts)
    math_shape_get_children(global_opts)
    mathematical_shape(global_opts)
    picture_frame_formatting(global_opts)
    remove_shape(global_opts)
    rotating_shapes_example(global_opts)
    set_alternative_text(global_opts)
    set_file_type_for_an_embedding_object(global_opts)
    set_video_trim_from_end(global_opts)
    shape_is_decorative_property_example(global_opts)
    shapes_alignment(global_opts)
    simple_ellipse(global_opts)
    simple_rectangle(global_opts)
    sketched_shapes(global_opts)
    stretch_offset_left_for_picture_frame(global_opts)
    substitute_picture_title_of_ole_object_frame(global_opts)
    tile_picture_fill_format_example(global_opts)
