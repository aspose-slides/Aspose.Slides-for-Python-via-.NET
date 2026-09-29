import aspose.slides as slides


def for_each_example(global_opts):
    with slides.Presentation(global_opts.data_dir + "ForEachPortion.pptx") as pres:
        # Visit every slide
        slides.lowcode.ForEach.slide(pres, lambda slide, index:
            print("Slide {0}: {1} shape(s)".format(index, len(slide.shapes))))

        # Visit every shape on the first slide
        slides.lowcode.ForEach.shape(pres.slides[0], lambda shape, slide, index:
            print("  Shape {0}: {1}".format(index, shape.name)))

        # Make every text portion bold and red (True = include notes slides too).
        # ForEach walks layout and master slides as well, not only normal slides.
        def highlight(portion, paragraph, slide, index):
            portion.portion_format.font_bold = slides.NullableBool.TRUE
            portion.portion_format.fill_format.fill_type = slides.FillType.SOLID
            portion.portion_format.fill_format.solid_fill_color.color = slides.Color.red

        slides.lowcode.ForEach.portion(pres, True, highlight)

        pres.save(global_opts.out_dir + "for_each_portion_out.pptx", slides.export.SaveFormat.PPTX)
