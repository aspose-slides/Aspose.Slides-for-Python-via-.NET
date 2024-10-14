import aspose.slides as slides


def animation_faded_zoom_subtype(global_opts):
    with slides.Presentation() as pres:
        # Create shapes for demonstration
        shp1 = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 0, 0, 50, 50)
        shp2 = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 0, 50, 50)

        # Added FadedZoom effects
        ef1 = pres.slides[0].timeline.main_sequence.add_effect(shp1, slides.animation.EffectType.FADED_ZOOM,
                                                               slides.animation.EffectSubtype.OBJECT_CENTER,
                                                               slides.animation.EffectTriggerType.ON_CLICK)
        ef2 = pres.slides[0].timeline.main_sequence.add_effect(shp2, slides.animation.EffectType.FADED_ZOOM,
                                                               slides.animation.EffectSubtype.SLIDE_CENTER,
                                                               slides.animation.EffectTriggerType.ON_CLICK)

        pres.save(global_opts.out_dir + "AnimationFadedZoom-out.pptx", slides.export.SaveFormat.PPTX)
