import aspose.slides as slides


def fallback_rules_collection():
    with slides.Presentation() as presentation:
        user_rules_list = slides.FontFallBackRulesCollection()

        user_rules_list.add(slides.FontFallBackRule(
            0x0B80, 0x0BFF, "Vijaya"))
        user_rules_list.add(slides.FontFallBackRule(
            0x3040, 0x309F, "MS Mincho, MS Gothic"))

        presentation.fonts_manager.font_fall_back_rules_collection = user_rules_list
