import aspose.slides as slides


def rule_based_fonts_replacement(global_opts):
    # Load presentation
    with slides.Presentation(global_opts.data_dir + "text_fonts.pptx") as presentation:
        # Load source font to be replaced
        source_font = slides.FontData("SomeRareFont")

        # Load the replacing font
        dest_font = slides.FontData("Arial")

        # Add font rule for font replacement
        font_subst_rule = slides.FontSubstRule(source_font, dest_font, slides.FontSubstCondition.WHEN_INACCESSIBLE)

        # Add rule to font substitute rules collection
        font_subst_rule_collection = slides.FontSubstRuleCollection()
        font_subst_rule_collection.add(font_subst_rule)

        # Add font rule collection to rule list
        presentation.fonts_manager.font_subst_rule_list = font_subst_rule_collection

        # Arial font will be used instead of SomeRareFont when inaccessible
        img = presentation.slides[0].get_image(1, 1)

        # Save the image to disk in JPEG format
        img.save(global_opts.out_dir + "text_rule_based_font_replacement_out.jpg", slides.ImageFormat.JPEG)
