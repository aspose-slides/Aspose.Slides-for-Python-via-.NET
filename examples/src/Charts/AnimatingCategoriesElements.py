import aspose.slides as slides

def charts_animating_categories_elements():
    #ExStart:AnimatingCategoriesElements
    # The path to the documents directory.
    dataDir = "./examples/data/"
    outDir = "./examples/out/"
    
    with slides.Presentation(dataDir + "charts_existing_chart.pptx") as presentation:
        # Get reference of the chart object
        slide = presentation.slides[0]
        shapes = slide.shapes
        chart = shapes[0]

        # Animate categories' elements
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectType.FADE, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 0, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 0, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 0, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 0, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 1, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 1, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 1, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 1, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 2, 0, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 2, 1, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 2, 2, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)
        slide.timeline.main_sequence.add_effect(chart, slides.animation.EffectChartMinorGroupingType.BY_ELEMENT_IN_CATEGORY, 2, 3, slides.animation.EffectType.APPEAR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.AFTER_PREVIOUS)

        # Write the presentation file to disk
        presentation.save(outDir + "charts_animating_categories_elements_out.pptx", slides.export.SaveFormat.PPTX)

    #ExEnd:AnimatingCategoriesElements

