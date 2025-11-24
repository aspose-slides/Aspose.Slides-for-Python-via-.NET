import platform

from .add_column_in_text_boxes import add_column_in_text_boxes
from .add_columns_in_text_frame import add_columns_in_text_frame
from .add_custom_prompt_text import add_custom_prompt_text
from .add_embedded_fonts import add_embedded_fonts
from .adding_superscript_and_subscript_text_in_text_frame import adding_superscript_and_subscript_text_in_text_frame
from .animate_text_type_example import animate_text_type_example
from .animation_effect_in_paragraph import animation_effect_in_paragraph
from .apply_inner_shadow import apply_inner_shadow
from .apply_outer_shadow import apply_outer_shadow
from .bullet_fill_format_effective import bullet_fill_format_effective
from .custom_rotation_angle_text_frame import custom_rotation_angle_text_frame
from .default_fonts_example import default_fonts_example
from .disable_font_ligatures_example import disable_font_ligatures_example
from .effect_text_box_paragraph import effect_text_box_paragraph
from .end_para_graph_properties import end_para_graph_properties
from .exporting_html_text import exporting_html_text
from .fallback_rules_collection import fallback_rules_collection
from .find_and_replace_text import find_and_replace_text
from .find_text_options import find_text_options
from .font_binary_data_example import font_binary_data_example
from .font_embedding_level_example import font_embedding_level_example
from .font_family_example import font_family_example
from .font_properties_example import font_properties_example
from .get_effective_values import get_effective_values
from .get_fonts_folder import get_fonts_folder
from .get_fonts_slide_substitution import get_fonts_slide_substitution
from .get_placeholder_text_example import get_placeholder_text_example
from .get_text_style_effective_data import get_text_style_effective_data
from .get_text_from_smart_art_node import get_text_from_smart_art_node
from .get_text_style_effective_data import get_text_style_effective_data
from .highlight_text import highlight_text
from .highlight_text_using_regex import highlight_text_using_regex
from .importing_html_text import importing_html_text
from .keep_text_flat import keep_text_flat
from .line_spacing import line_spacing
from .load_external_font_example import load_external_font_example
from .manage_embedded_fonts import manage_embedded_fonts
from .manage_paragraph_font_properties import manage_paragraph_font_properties
from .manage_paragraph_picture_bullets_in_ppt import manage_paragraph_picture_bullets_in_ppt
from .manage_script_fonts_example import manage_script_fonts_example
from .multiple_paragraphs import multiple_paragraphs
from .multi_level_bullets import multi_level_bullets
from .number_lines_in_paragraph import number_lines_in_paragraph
from .paragraph_bullets import paragraph_bullets
from .paragraph_indent import paragraph_indent
from .paragraphs_alignment import paragraphs_alignment
from .portion_get_rect import portion_get_rect
from .rendering_with_fallback_font import rendering_with_fallback_font
from .replace_fonts_explicitly import replace_fonts_explicitly
from .replacing_text import replacing_text
from .rotating_text import rotating_text
from .rule_based_fonts_replacement import rule_based_fonts_replacement
from .save_with_default_regular_font import save_with_default_regular_font
from .set_anchor_of_text_frame import set_anchor_of_text_frame
from .set_autofit_of_text_frame import set_autofit_of_text_frame
from .set_custom_bullets_number import set_custom_bullets_number
from .set_local_font_height_values import set_local_font_height_values
from .set_text_font_properties import set_text_font_properties
from .set_transparency_of_text_in_shadow import set_transparency_of_text_in_shadow
from .setting_presentation_language_and_shape_text import setting_presentation_language_and_shape_text
from .shadow_effects import shadow_effects
from .specify_default_text_language import specify_default_text_language
from .split_text_by_columns_example import split_text_by_columns_example
from .text_box_hyperlink import text_box_hyperlink
from .text_box_on_slide_program import text_box_on_slide_program
from .use_custom_fonts import use_custom_fonts
from .word_art_example import word_art_example


def run_text_examples(global_opts):
    print("===== Text examples =====")
    add_column_in_text_boxes(global_opts)
    add_columns_in_text_frame(global_opts)
    add_custom_prompt_text(global_opts)
    if platform.system() == "Windows": add_embedded_fonts(global_opts)
    adding_superscript_and_subscript_text_in_text_frame(global_opts)
    animate_text_type_example(global_opts)
    animation_effect_in_paragraph(global_opts)
    apply_inner_shadow(global_opts)
    apply_outer_shadow(global_opts)
    bullet_fill_format_effective(global_opts)
    custom_rotation_angle_text_frame(global_opts)
    default_fonts_example(global_opts)
    disable_font_ligatures_example(global_opts)
    effect_text_box_paragraph(global_opts)
    end_para_graph_properties(global_opts)
    exporting_html_text(global_opts)
    fallback_rules_collection()
    find_and_replace_text(global_opts)
    find_text_options(global_opts)
    if platform.system() != "Linux":
        font_binary_data_example(global_opts)
        font_embedding_level_example(global_opts)
    font_family_example(global_opts)
    font_properties_example(global_opts)
    get_effective_values(global_opts)
    get_fonts_folder()
    get_fonts_slide_substitution(global_opts)
    get_placeholder_text_example()
    get_text_style_effective_data(global_opts)
    get_text_from_smart_art_node(global_opts)
    get_text_style_effective_data(global_opts)
    highlight_text(global_opts)
    highlight_text_using_regex(global_opts)
    importing_html_text(global_opts)
    keep_text_flat(global_opts)
    line_spacing(global_opts)
    load_external_font_example(global_opts)
    manage_embedded_fonts(global_opts)
    manage_paragraph_font_properties(global_opts)
    manage_paragraph_picture_bullets_in_ppt(global_opts)
    manage_script_fonts_example()
    multiple_paragraphs(global_opts)
    multi_level_bullets(global_opts)
    number_lines_in_paragraph()
    paragraph_bullets(global_opts)
    paragraph_indent(global_opts)
    paragraphs_alignment(global_opts)
    portion_get_rect(global_opts)
    rendering_with_fallback_font(global_opts)
    replace_fonts_explicitly(global_opts)
    replacing_text(global_opts)
    rotating_text(global_opts)
    rule_based_fonts_replacement(global_opts)
    save_with_default_regular_font(global_opts)
    set_anchor_of_text_frame(global_opts)
    set_autofit_of_text_frame(global_opts)
    set_custom_bullets_number(global_opts)
    set_local_font_height_values(global_opts)
    set_text_font_properties(global_opts)
    set_transparency_of_text_in_shadow(global_opts)
    setting_presentation_language_and_shape_text(global_opts)
    shadow_effects(global_opts)
    specify_default_text_language()
    split_text_by_columns_example(global_opts)
    text_box_hyperlink(global_opts)
    text_box_on_slide_program(global_opts)
    use_custom_fonts(global_opts)
    word_art_example(global_opts)
