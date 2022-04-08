import aspose.slides as slides

#ExStart:FallBackRulesCollection

with slides.Presentation() as presentation:
    userRulesList = slides.FontFallBackRulesCollection()

    userRulesList.add(slides.FontFallBackRule(0x0B80, 0x0BFF, "Vijaya"))
    userRulesList.add(slides.FontFallBackRule(0x3040, 0x309F, "MS Mincho, MS Gothic"))

    presentation.fonts_manager.font_fall_back_rules_collection = userRulesList
#ExEnd:FallBackRulesCollection