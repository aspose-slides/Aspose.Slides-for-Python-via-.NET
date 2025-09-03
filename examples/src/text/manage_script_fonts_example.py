import aspose.slides as slides


def manage_script_fonts_example():
    with slides.Presentation() as pres:
        # Get all script mapping
        script_font_map = pres.master_theme.font_scheme.major.get_script_font_map()
        for kvp in script_font_map:
            print(kvp.key, "=", kvp.value)

        # Get script font
        print("Font for \"Thaa\" tag is" + pres.master_theme.font_scheme.major.get_script_font("Thaa"))

        # Set script font
        pres.master_theme.font_scheme.major.set_script_font("Thaa", "Super Thaa")
        pres.master_theme.font_scheme.minor.remove_script_font("Geor")

        # Check script font
        print("Font for \"Thaa\" tag is" + pres.master_theme.font_scheme.major.get_script_font("Thaa"))
