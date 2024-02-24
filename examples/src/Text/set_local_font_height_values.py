import aspose.slides as slides


def set_local_font_height_values(global_opts):
    with slides.Presentation() as pres:
        new_shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 100, 100, 400, 75, False)
        new_shape.add_text_frame("")
        new_shape.text_frame.paragraphs[0].portions.clear()

        portion0 = slides.Portion("Sample text with first portion")
        portion1 = slides.Portion(" and second portion.")

        new_shape.text_frame.paragraphs[0].portions.add(portion0)
        new_shape.text_frame.paragraphs[0].portions.add(portion1)

        print("Effective font height just after creation:")
        print("Portion #0: " + str(portion0.portion_format.get_effective().font_height))
        print("Portion #1: " + str(portion1.portion_format.get_effective().font_height))

        pres.default_text_style.get_level(0).default_portion_format.font_height = 24

        print("Effective font height after setting entire presentation default font height:")
        print("Portion #0: " + str(portion0.portion_format.get_effective().font_height))
        print("Portion #1: " + str(portion1.portion_format.get_effective().font_height))

        new_shape.text_frame.paragraphs[0].paragraph_format.default_portion_format.font_height = 40

        print("Effective font height after setting paragraph default font height:")
        print("Portion #0: " + str(portion0.portion_format.get_effective().font_height))
        print("Portion #1: " + str(portion1.portion_format.get_effective().font_height))

        new_shape.text_frame.paragraphs[0].portions[0].portion_format.font_height = 55

        print("Effective font height after setting portion #0 font height:")
        print("Portion #0: " + str(portion0.portion_format.get_effective().font_height))
        print("Portion #1: " + str(portion1.portion_format.get_effective().font_height))

        new_shape.text_frame.paragraphs[0].portions[1].portion_format.font_height = 18

        print("Effective font height after setting portion #1 font height:")
        print("Portion #0: " + str(portion0.portion_format.get_effective().font_height))
        print("Portion #1: " + str(portion1.portion_format.get_effective().font_height))

        pres.save(global_opts.out_dir + "text_SetLocalFontHeightValues_out.pptx", slides.export.SaveFormat.PPTX)
