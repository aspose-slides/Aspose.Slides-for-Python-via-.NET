import aspose.slides as slides
import aspose.pydrawing as drawing


def rendering_with_fallback_font(global_opts):
    # Create new instance of a rules collection
    rules_list = slides.FontFallBackRulesCollection()

    # create a number of rules
    rules_list.add(slides.FontFallBackRule(0x400, 0x4FF, "Times New Roman"))

    for fallback_rule in rules_list:
        # Trying to remove FallBack font "Tahoma" from loaded rules
        fallback_rule.remove("Tahoma")

        # And to update of rules for specified range
        if fallback_rule.range_end_index >= 0x4000 and fallback_rule.range_start_index < 0x5000:
            fallback_rule.add_fallBack_fonts("Verdana")

    # Also we can remove any existing rules from list
    if len(rules_list) > 0:
        rules_list.remove(rules_list[0])

    with slides.Presentation(global_opts.data_dir + "welcome-to-powerpoint.pptx") as pres:
        # Assigning a prepared rules list for using
        pres.fonts_manager.font_fall_back_rules_collection = rules_list

        # Rendering of thumbnail with using of initialized rules collection and saving to PNG
        pres.slides[0].get_thumbnail(1, 1).save(global_opts.out_dir + "text_font_fall_back_out.png", drawing.imaging.ImageFormat.png)
