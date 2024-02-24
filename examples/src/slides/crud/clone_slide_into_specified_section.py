import aspose.slides as slides


def clone_slide_into_specified_section(global_opts):
    with slides.Presentation() as presentation:
        presentation.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 200, 50, 300, 100)
        presentation.sections.add_section("Section 1", presentation.slides[0])

        section2 = presentation.sections.append_empty_section("Section 2")
        presentation.slides.add_clone(presentation.slides[0], section2)

        presentation.save(global_opts.out_dir + "crud_append_empty_section_out.pptx", slides.export.SaveFormat.PPTX)
