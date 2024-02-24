import aspose.slides as slides


def charts_animating_series_elements(global_opts):
    # Load a presentation
    with slides.Presentation(global_opts.data_dir + "charts_existing_chart.pptx") as presentation:
        # Get reference of the chart object
        slide = presentation.slides[0]
        shapes = slide.shapes
        chart = shapes[0]

        # Animate series elements
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectType.FADE, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 0, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 0, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 0, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 0, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 1, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 1, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 1, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 1, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 2, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 2, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 2, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_SERIES, 2, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        # Write the presentation file to disk 
        presentation.save(global_opts.out_dir + "charts_animating_series_elements_out.pptx", slides.export.SaveFormat.PPTX)
