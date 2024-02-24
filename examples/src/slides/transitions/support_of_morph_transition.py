import aspose.slides as slides


def support_of_morph_transition(global_opts):
    with slides.Presentation() as presentation:
        auto_shape = presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 400, 100)
        auto_shape.text_frame.text = "Test text"

        presentation.slides.add_clone(presentation.slides[0])

        presentation.slides[1].shapes[0].x += 100
        presentation.slides[1].shapes[0].y += 50
        presentation.slides[1].shapes[0].width -= 200
        presentation.slides[1].shapes[0].height -= 10

        presentation.slides[1].slide_show_transition.type = slides.slideshow.TransitionType.MORPH

        presentation.save(global_opts.out_dir + "transition_SupportOfMorphTransition_out.pptx",
                          slides.export.SaveFormat.PPTX)
