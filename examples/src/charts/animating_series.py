import aspose.slides as slides


def charts_animating_series(options):
    # Instantiate Presentation class that represents a presentation file
    with slides.Presentation(options.data_dir + "charts_existing_chart.pptx") as presentation:
        # Get reference of the chart object
        slide = presentation.slides[0]
        shapes = slide.shapes
        chart = shapes[0]

        # Animate the series
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectType.FADE, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMajorGroupingType.BY_SERIES, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMajorGroupingType.BY_SERIES, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMajorGroupingType.BY_SERIES, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMajorGroupingType.BY_SERIES, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        # Write the modified presentation to disk 
        presentation.save(options.out_dir + "charts_animating_series_out.pptx", slides.export.SaveFormat.PPTX)
