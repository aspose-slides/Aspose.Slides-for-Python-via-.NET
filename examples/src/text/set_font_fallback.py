import aspose.slides as slides


def set_font_fallback(global_opts):
    start_unicode_index = 0x0B80
    end_unicode_index = 0x0BFF

    first_rule = slides.FontFallBackRule(start_unicode_index, end_unicode_index, "Vijaya")
    second_rule = slides.FontFallBackRule(0x3040, 0x309F, "MS Mincho, MS Gothic")

    # Also the fonts list can be added in several ways:
    font_names = ["Segoe UI Emoji, Segoe UI Symbol", "Arial"]

    third_rule = slides.FontFallBackRule(0x1F300, 0x1F64F, font_names)
