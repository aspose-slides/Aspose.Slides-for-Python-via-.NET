import aspose.slides as slides
import aspose.pydrawing as drawing


def set_transparency_of_text_in_shadow(global_opts):
    with slides.Presentation(global_opts.data_dir + "text_transparency.pptx") as pres:
        shape = pres.slides[0].shapes[0]
        effects = shape.text_frame.paragraphs[0].portions[0].portion_format.effect_format

        outer_shadow_effect = effects.outer_shadow_effect

        shadow_color = outer_shadow_effect.shadow_color.color
        print("{0} - transparency is: {1}".format(shadow_color, (shadow_color.a / 255) * 100))

        # set transparency to zero percent
        outer_shadow_effect.shadow_color.color = drawing.Color.from_argb(255, shadow_color)

        pres.save(global_opts.out_dir + "text_transparency_out.pptx", slides.export.SaveFormat.PPTX)
