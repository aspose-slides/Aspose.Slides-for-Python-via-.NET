import aspose.slides as slides


def animation_duration_slide(global_opts):
    with slides.Presentation(global_opts.data_dir + "AnimationDurationSlides.pptx") as pres:
        for slide in pres.slides:
            slide.slide_show_transition.duration = 250

        pres.save(global_opts.out_dir + "AnimationDurationSlides-out.pptx", slides.export.SaveFormat.PPTX)
