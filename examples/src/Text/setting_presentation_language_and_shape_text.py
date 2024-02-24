import aspose.slides as slides


def setting_presentation_language_and_shape_text(global_opts):
    with slides.Presentation() as pres:
        shape = pres.slides[0].shapes.add_auto_shape(slides.ShapeType.RECTANGLE, 50, 50, 200, 50)
        shape.add_text_frame("Text to apply spellcheck language")
        shape.text_frame.paragraphs[0].portions[0].portion_format.language_id = "en-EN"

        pres.save(global_opts.out_dir + "text_SettingPresentationLanguageAndShapeText_out.pptx",
                  slides.export.SaveFormat.PPTX)
