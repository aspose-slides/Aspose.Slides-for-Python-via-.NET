from .conversion_to_tiff_notes import convert_to_tiff_notes
from .convert_html_embedding_images import convert_html_embedding_images
from .convert_notes_slide_view_to_pdf import convert_notes_to_pdf
from .convert_presentation_to_password_protected_pdf import convert_to_password_protected_pdf
from .convert_presentation_to_responsive_html import convert_to_responsive_html
from .convert_slides_to_pdf_notes import convert_to_pdf_notes
from .convert_specific_slide_to_pdf import convert_specific_slide_to_pdf
from .convert_svg_to_emf import convert_svg_to_emf
from .convert_to_black_white_tiff import convert_to_black_white_tiff
from .convert_to_emf import convert_to_emf
from .convert_to_gif import convert_to_gif
from .convert_to_handout import convert_to_handout
from .convert_to_html5_notes_comments import convert_to_html5_notes_comments
from .convert_to_html5 import convert_to_html5
from .convert_to_markdown import convert_to_markdown
from .convert_to_pdf_compliance import convert_to_pdf_compliance
from .convert_to_pdf_unsupported_font_styles import convert_to_pdf_unsupported_font_styles
from .convert_to_pdf_with_hidden_slides import convert_to_pdf_hidden_slides
from .convert_to_pdf_with_pdf_compliance_a1a_a1b_ua import convert_to_pdf_with_compliance
from .convert_to_pdf import convert_to_pdf
from .convert_to_swf import convert_to_swf
from .convert_to_xml import convert_to_xml
from .convert_whole_presentation_to_html_with_media_files import convert_to_html_with_media
from .convert_with_custom_size import convert_to_tiff_custom_size
from .convert_with_note_to_tiff import convert_to_tiff_with_notes
from .convert_with_xps_options import convert_to_xps_with_options
from .convert_without_xps_options import convert_to_xps
from .converting_presentation_to_html_with_embed_all_fonts_html_controller import convert_to_html_with_embed_all_fonts
from .converting_presentation_to_html_with_preserving_original_fonts import \
    convert_to_html_with_preserving_original_fonts
from .create_new_presentation import create_new_presentation
from .custom_options_pdf_conversion import convert_to_pdf_custom_options
from .export_ink_example import export_ink_example
from .export_math_paragraph_to_latex import export_math_paragraph_to_latex
from .export_math_paragraph_to_math_ml import export_math_paragraph_to_math_ml
from .export_ole_example import export_ole_example
from .export_shape_to_svg import export_shape_to_svg
from .export_to_html_with_responsive_layout import convert_to_html_with_responsive_layout
from .fodp_format_conversion import convert_to_fodp
from .odp_to_pptx import convert_to_odp
from .pdf_import_example import import_from_pdf
from .ppt_to_pptx import convert_to_ppt
from .presentation_to_tiff_with_custom_image_pixel_format import convert_to_tiff_image_pixel_format
from .presentation_to_tiff_with_default_size import convert_to_tiff
from .rendering_notes_while_converting_to_html import convert_to_html_with_notes
from .slide_show_media_controls import slide_show_media_controls


def run_presentation_conversion_examples(global_opts):
    convert_to_tiff_notes(global_opts)
    # convert_html_embedding_images(global_opts)
    convert_notes_to_pdf(global_opts)
    convert_to_password_protected_pdf(global_opts)
    convert_to_responsive_html(global_opts)
    convert_to_pdf_notes(global_opts)
    convert_specific_slide_to_pdf(global_opts)
    convert_svg_to_emf(global_opts)
    convert_to_black_white_tiff(global_opts)
    convert_to_emf(global_opts)
    convert_to_gif(global_opts)
    convert_to_handout(global_opts)
    convert_to_html5_notes_comments(global_opts)
    convert_to_html5(global_opts)
    convert_to_markdown(global_opts)
    convert_to_pdf_compliance(global_opts)
    convert_to_pdf_hidden_slides(global_opts)
    convert_to_pdf_with_compliance(global_opts)
    convert_to_pdf_unsupported_font_styles(global_opts)
    convert_to_pdf(global_opts)
    convert_to_swf(global_opts)
    convert_to_xml(global_opts)
    convert_to_html_with_media(global_opts)
    convert_to_tiff_custom_size(global_opts)
    convert_to_tiff_with_notes(global_opts)
    convert_to_xps_with_options(global_opts)
    convert_to_xps(global_opts)
    convert_to_html_with_embed_all_fonts(global_opts)
    convert_to_html_with_preserving_original_fonts(global_opts)
    create_new_presentation(global_opts)
    convert_to_pdf_custom_options(global_opts)
    export_ink_example(global_opts)
    export_math_paragraph_to_latex()
    export_math_paragraph_to_math_ml(global_opts)
    export_ole_example(global_opts)
    export_shape_to_svg(global_opts)
    convert_to_html_with_responsive_layout(global_opts)
    convert_to_fodp(global_opts)
    convert_to_odp(global_opts)
    import_from_pdf(global_opts)
    convert_to_ppt(global_opts)
    convert_to_tiff_image_pixel_format(global_opts)
    convert_to_tiff(global_opts)
    convert_to_html_with_notes(global_opts)
    slide_show_media_controls(global_opts)
